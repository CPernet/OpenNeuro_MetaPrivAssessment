import pandas as pd 
import matplotlib.pyplot as plt
from scipy.stats import spearmanr, kendalltau, linregress, rankdata
from rpy2 import robjects
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri
import numpy as np
import piflib 
from piflib import compute_cigs
import warnings


# Suppress SettingWithCopyWarning
warnings.simplefilter(action='ignore', category=pd.core.common.SettingWithCopyWarning)

# Activate pandas <-> R DataFrame conversion
pandas2ri.activate()
from rpy2.robjects.conversion import localconverter


# Import the sdcMicro package
sdcMicro = importr('sdcMicro')



def stats(suda, pif, suda_att, k_combined_field):
    print('\n' + '='*40)
    print('        ROW LEVEL CORRELATION      ')
    print('='*40 + '\n')
    
    # Spearman Rank Correlation
    correlation_spearman, p_value = spearmanr(suda['dis-score'], pif['RIG'])
    print(f"Spearman Rank Correlation between suda & pif: {correlation_spearman:.2f}, P-value: {p_value:.4f}")
    
    # Kendall's Tau Correlation
    tau, p_value_t = kendalltau(suda['dis-score'], pif['RIG'])
    print(f"Kendall's Tau between suda & pif: {tau:.2f}, p-value: {p_value_t:.4f}")
    
    # Pearson Correlation
    correlation_pearson = suda['dis-score'].corr(pif['RIG'])
    print(f"Pearson Correlation between suda & pif: {correlation_pearson:.4f}")
    
    # Field relationship
    sum_df = pif.drop(columns=['RIG']).sum()
    sum_df = pd.DataFrame(list(sum_df.items()), columns=['variable', 'sum'])
    
    # Merge the two DataFrames on 'variable'
    merged_field_values = pd.merge(suda_att, sum_df, on='variable')
    merged_field_values = pd.merge(merged_field_values, k_combined_field, on='variable') 

    # Calculate Pearson correlations
    correlation_pif_suda = merged_field_values['contribution'].corr(merged_field_values['sum'])
    correlation_pif_k = merged_field_values['Normalized Difference'].corr(merged_field_values['sum'])
    correlation_suda_k = merged_field_values['contribution'].corr(merged_field_values['Normalized Difference'])
    
    # Plot Spearman Rank Correlation with Trend Line
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.scatter(rankdata(suda['dis-score']), rankdata(pif['RIG']), alpha=0.3, label='Ranked Data Points')
    
    # Fit and plot the trend line for ranked data
    slope, intercept, _, _, _ = linregress(rankdata(suda['dis-score']), rankdata(pif['RIG']))
    ax.plot(rankdata(suda['dis-score']), slope * rankdata(suda['dis-score']) + intercept, color='red', label='Trend Line')
    
    ax.set_title(f'Spearman Correlation: {correlation_spearman:.2f}')
    ax.set_xlabel('Ranked SUDA (dis-score)')
    ax.set_ylabel('Ranked PIF (RIG)')
    ax.grid(False)
    ax.legend()
    
    plt.show()    
    plt.close(fig)
    print('____________________________________________________________________________________')
    
    print('\n' + '='*40)
    print('      FIELD LEVEL CORRELATIONS     ')
    print('='*40 + '\n')
    
    # Print Pearson correlations for field-level analysis
    print(f"Pearson Correlation between SUDA & PIF field level: {correlation_pif_suda:.2f}")
    print(f"Pearson Correlation between K-combined & PIF field level: {correlation_pif_k:.2f}")
    print(f"Pearson Correlation between SUDA & K-combined field level: {correlation_suda_k:.2f}")
    print('\n')
    
    # Spearman correlations for field-level analysis
    correlation_spearman_pif_suda, p_value = spearmanr(merged_field_values['contribution'], merged_field_values['sum'])
    print(f"Spearman Rank Correlation between PIF & SUDA: {correlation_spearman_pif_suda:.2f}, P-value: {p_value:.4f}")

    correlation_spearman_pif_k, p_value = spearmanr(merged_field_values['Normalized Difference'], merged_field_values['sum'])
    print(f"Spearman Rank Correlation between PIF & K: {correlation_spearman_pif_k:.2f}, P-value: {p_value:.4f}")

    correlation_spearman_suda_k, p_value = spearmanr(merged_field_values['contribution'], merged_field_values['Normalized Difference'])
    print(f"Spearman Rank Correlation between SUDA & K: {correlation_spearman_suda_k:.2f}, P-value: {p_value:.4f}")

    return





def convert_to_numeric(df):
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype('category').cat.codes
    return df



def compute_suda2(dataframe, sample_fraction=0.2, missing_value=np.NaN):
    with localconverter(pandas2ri.converter):
        r_df = robjects.conversion.py2rpy(dataframe)
        
    
    convert_to_numeric(dataframe) 
    
    suda_result = sdcMicro.suda2(r_df, missing=missing_value, DisFraction=sample_fraction)
    contribution_percent = list(suda_result.rx2('contributionPercent'))
    score = list(suda_result.rx2('score'))
    dis_score = list(suda_result.rx2('disScore'))

    return (contribution_percent, score, dis_score,suda_result)





import piflib.pif_calculator as pif
def calculate_summed_dis_scores(k_combined_all, AOMIC, sample_fraction=0.3, missing_value= -999):

    dis_scores = []
    pif_score = []
    
    k_combined_all = k_combined_all[k_combined_all['Combination'].str.count(',') >= 2]
    
    for index, row in k_combined_all.iterrows():
        combination_fields = row['Combination'].split(', ')
       
        df_subset = AOMIC[combination_fields]
        df_subset = df_subset.fillna(-999)
        
        contribution_percent, score, dis_score, attribute_contributions = compute_suda2(
            df_subset, sample_fraction=sample_fraction, missing_value=missing_value)  
        
        summed_dis_score = sum(dis_score)
        dis_scores.append(summed_dis_score)
        
        cigs = piflib.compute_cigs(df_subset)
        pif_95 = pif.compute_pif(cigs, 0.95)
        pif_score.append(pif_95)
        

    k_combined_all['pif_score'] = pif_score
    k_combined_all['suda_score'] = dis_scores
    k_combined_all.fillna(0, inplace=True)
    
    return k_combined_all





def plot_calc(k_combined_all): 
    k_combined_all = k_combined_all.replace([np.inf, -np.inf], 0)

    # SUDA vs. K-Combined
    spearman_corr, _ = spearmanr(k_combined_all['Score'], k_combined_all['suda_score'])
    pearson_corr = k_combined_all['Score'].corr(k_combined_all['suda_score'])
    print(f"Spearman Correlation between Suda sum and K-combined: {spearman_corr:.2f}")
    print(f"Pearson Correlation between Suda sum and K-combined: {pearson_corr:.2f}")
    
    plt.figure(figsize=(8, 4))
    plt.scatter(rankdata(k_combined_all['Score']), rankdata(k_combined_all['suda_score']), alpha=0.6)
    plt.title(f'Scatter Plot of Ranked k-combined Score vs. SUDA Score\n(Spearman Correlation: {spearman_corr:.2f})')
    plt.xlabel('Ranked K-combined Score')
    plt.ylabel('Ranked SUDA Score')
    plt.grid(False)
    plt.show()
    
    print('________________________________________________________________________')
    print('\n')
    
    # PIF vs. K-Combined
    spearman_corr, _ = spearmanr(k_combined_all['Score'], k_combined_all['pif_score'])
    pearson_corr = k_combined_all['Score'].corr(k_combined_all['pif_score'])
    print(f"Spearman Correlation between PIF 95% and K-combined: {spearman_corr:.2f}")
    print(f"Pearson Correlation between PIF 95% and K-combined: {pearson_corr:.2f}")
    
    plt.figure(figsize=(8, 4))
    plt.scatter(rankdata(k_combined_all['Score']), rankdata(k_combined_all['pif_score']), alpha=0.6)
    plt.title(f'Scatter Plot of Ranked k-combined Score vs. PIF Score\n(Spearman Correlation: {spearman_corr:.2f})')
    plt.xlabel('Ranked K-combined Score')
    plt.ylabel('Ranked PIF Score')
    plt.grid(False)
    plt.show()
    
    print('________________________________________________________________________')
    print('\n')
    
    # PIF vs. SUDA
    spearman_corr, _ = spearmanr(k_combined_all['suda_score'], k_combined_all['pif_score'])
    pearson_corr = k_combined_all['suda_score'].corr(k_combined_all['pif_score'])
    print(f"Spearman Correlation between PIF 95% and SUDA: {spearman_corr:.2f}")
    print(f"Pearson Correlation between PIF 95% and SUDA: {pearson_corr:.2f}")
    
    plt.figure(figsize=(8, 4))
    plt.scatter(rankdata(k_combined_all['suda_score']), rankdata(k_combined_all['pif_score']), alpha=0.6)
    plt.title(f'Scatter Plot of Ranked SUDA Score vs. PIF Score\n(Spearman Correlation: {spearman_corr:.2f})')
    plt.xlabel('Ranked SUDA Score')
    plt.ylabel('Ranked PIF Score')
    plt.grid(False)
    plt.show()
    
    return







def rst_outlier_case2(data, column, k=2.2414):
    column_data = data[column]
    column_data_array = np.array(column_data)
    median = np.nanmedian(column_data_array)
    mad = np.nanmedian(np.abs(column_data_array - median))
    madn = mad / 0.6745

    # Calculate z-scores
    z_scores = (column_data_array - median) / madn

    # Identify outliers
    class_outliers = (np.abs(z_scores) > k).astype(int)
    outlier_indices = data[class_outliers == 1].index.tolist()
    above_outliers = (z_scores > k).astype(int)
    above_outlier_indices = data[above_outliers == 1].index.tolist()
    outlier_tuples = [(z_scores[idx], idx) for idx in outlier_indices]

    # Create the box plot
    plt.figure(figsize=(8, 5))
    boxplot = plt.boxplot(
        z_scores,
        vert=False,
        patch_artist=True,
        boxprops=dict(facecolor='lightblue', color='blue'),
        medianprops=dict(color='orange'),
        flierprops=dict(marker='o', color='red', alpha=0.6)
    )
    
    # Adjust whiskers manually to limit them to -k and +k
    for line in boxplot['whiskers']:
        xdata = line.get_xdata()
        capped_xdata = np.clip(xdata, -k, k)  # Cap whisker ends to -k and +k
        line.set_xdata(capped_xdata)
    
    for cap in boxplot['caps']:
        xdata = cap.get_xdata()
        capped_xdata = np.clip(xdata, -k, k)  # Cap caps to -k and +k
        cap.set_xdata(capped_xdata)
    
    # Add threshold lines for -k and +k
    plt.axvline(x=-k, color='red', linestyle='--', label=f'Lower Threshold (-{k})')
    plt.axvline(x=k, color='red', linestyle='--', label=f'Upper Threshold (+{k})')
    
    # Plot customization
    plt.title('Boxplot Based on Z-Scores with Outlier Thresholds')
    plt.xlabel('Z-Score')
    plt.legend(loc='upper left')
    plt.show()

    return class_outliers, madn, mad, outlier_indices, above_outlier_indices, outlier_tuples







