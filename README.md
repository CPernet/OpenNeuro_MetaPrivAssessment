# MetaprivBIDS-Assessment
Statistical assessment of  MetaprivBIDS https://github.com/CPernet/metaprivBIDS. 

Assessed datatset: 

1. AOMIC-ID1000-ds003097<br>
link: https://openneuro.org/datasets/ds003097/versions/1.2.1

2. EEG-Study-Alcohol-Imagery-Task-ds004515<br>
link: https://openneuro.org/datasets/ds004515/versions/1.0.0

3. Dallas-Lifespan-Brain-Study-ds004856<br>
link: https://openneuro.org/datasets/ds004856/versions/1.2.0

4. NIMH-Healthy-Research-Volunteer-Data-ds004215<br>
link: https://openneuro.org/datasets/ds004215/versions/2.0.1

5. The-Midnight-Scan-Club-dataset-ds000224<br>
link: https://openneuro.org/datasets/ds000224/versions/1.0.4

6. Stressful experiences are associated with reduced neural responses to naturalistic emotional and social content in children ds004228<br>
link: https://openneuro.org/datasets/ds004228/versions/1.0.1/file-display/phenotype:questionnaires.json

7. Multivariate Assessment of Inhibitory Control in Youth: Links with Psychopathology and Brain Function Dataset ds004935<br>
link: https://openneuro.org/datasets/ds004935/versions/1.0.2

8. BTC_postop<br>
link: https://openneuro.org/datasets/ds002080/versions/4.0.0

### Row level correlation:

| Dataset                 | Pearson Correlation (SUDA vs PIF) | Spearman Correlation (SUDA vs PIF) | Kendall's Tau (SUDA vs PIF)  |
|-------------------------|-----------------------------------|------------------------------------|------------------------------|
| AOMIC ds003097          | 0.74                              | 0.76                               | 0.61                         |
| DALLAS ds004856         | 0.57                              | 0.33                               | 0.40                         |
| EGG ds004515            | 0.52                              | 0.68                               | 0.56                         |
| MIDNIGHT ds000224       | 0.74                              | 0.69                               | 0.63                         |
| NIMH ds004215           | 0.50                              | 0.83                               | 0.63                         |
| STRESSFUL ds004228      | 0.47                              | 0.82                               | 0.63                         |
| MULTIVARIATE ds004935   | 0.82                                | 0.80                                 | 0.67                           |
| BTC*                       | 0.0                                | 0.0                                 | 0.0                           |


*  #BTC: 0 correlation as SUDA set all rows to equal score. 

The average correlation values across the datasets are:

- Average Pearson Correlation: 0.62
- Average Spearman Correlation: 0.70
- Average Kendall's Tau: 0.58 ​​

### Field level correlation:



#### Dataset: AOMIC (Field Level)

| Correlation Type           | Variables             | Correlation Value |
|----------------------------|-----------------------|--------------------|
|**Pearson Correlation**    | SUDA & PIF            | 0.77              |
|                            | K-combined & PIF      | 0.37              |
|                            | SUDA & K-combined     | -0.09             |
|**Spearman Rank Correlation** | PIF & SUDA       | 0.82              |
|                            | PIF & K-combined               | 0.11              |
|                            | SUDA & K-combined              | -0.01             |





#### Dataset: NIMH (Field Level)

| Correlation Type              | Variables             | Correlation Value |
|-------------------------------|-----------------------|--------------------|
| **Pearson Correlation**       | SUDA & PIF           | 0.82              |
|                               | K-combined & PIF     | 0.39              |
|                               | SUDA & K-combined    | 0.09              |
| **Spearman Rank Correlation** | PIF & SUDA           | 0.84              |
|                               | PIF & K              | 0.43              |
|                               | SUDA & K             | 0.31              |



#### Dataset: DALLAS (Field Level)

| Correlation Type              | Variables             | Correlation Value |
|-------------------------------|-----------------------|--------------------|
| **Pearson Correlation**       | SUDA & PIF           | 0.91              |
|                               | K-combined & PIF     | 0.36              |
|                               | SUDA & K-combined    | 0.71              |
| **Spearman Rank Correlation** | PIF & SUDA           | 0.81              |
|                               | PIF & K              | 0.22              |
|                               | SUDA & K             | 0.55              |


#### Dataset: EARLY STRESSFUL (Field Level)

| Correlation Type              | Variables             | Correlation Value |
|-------------------------------|-----------------------|--------------------|
| **Pearson Correlation**       | SUDA & PIF           | 0.63              |
|                               | K-combined & PIF     | 0.11              |
|                               | SUDA & K-combined    | 0.50              |
| **Spearman Rank Correlation** | PIF & SUDA           | 0.32              |
|                               | PIF & K              | 0.00              |
|                               | SUDA & K             | 0.09              |

#### Dataset: MULTI (Field Level)

| Correlation Type          | Variables       | Correlation Value |
|---------------------------|-----------------|-------------------|
| **Pearson Correlation**      | SUDA & PIF      | 0.74              |
|        | K-combined & PIF| 0.73              |
|        | SUDA & K-combined| 0.32             |
| **Spearman Rank Correlation** | PIF & SUDA      | 0.77              |
|  | PIF & K         | 0.17              |
| | SUDA & K        | 0.51              |



#### Dataset: BTC (Field Level)


| Correlation Type            | Variables             | Correlation Value |
|-----------------------------|-----------------------|-------------------|
| **Pearson Correlation**         | SUDA & PIF            | 0.99              |
|          | K-combined & PIF      | 0.12              |
|          | SUDA & K-combined     | 0.11              |
| **Spearman Rank Correlation**   | PIF & SUDA            | 0.89              |
|    | PIF & K               | 0.58              |
|    | SUDA & K              | 0.58              |



#### **Pearson Correlation (AVG)**<br>
SUDA & PIF: 0.81<br>
K-combined & PIF: 0.35<br>
SUDA & K-combined: 0.27<br>

#### **Spearman Rank Correlation(AVG)**<br>
PIF & SUDA: 0.74<br>
PIF & K: 0.25<br>
SUDA & K: 0.34<br>



###  Sum of combined risk for all combination of fields at a minimum of 3 variables:

#### DALLAS Correlation

| Correlation Type            | Variables                 | Correlation Value       |
|-----------------------------|---------------------------|-------------------------|
| Spearman Correlation        | Suda sum & K-combined     | 0.73                    |
| Pearson Correlation         | Suda sum & K-combined     | 0.56      |
| Spearman Correlation        | PIF 95% & K-combined      | 0.80                    |
| Pearson Correlation         | PIF 95% & K-combined      | 0.77      |
| Spearman Correlation        | PIF 95% & SUDA            | 0.84                    |
| Pearson Correlation         | PIF 95% & SUDA            | 0.82      |


#### AOMIC Correlation

| Correlation Type            | Variables                 | Correlation Value       |
|-----------------------------|---------------------------|-------------------------|
| Spearman Correlation        | Suda sum & K-combined     | -0.57                   |
| Pearson Correlation         | Suda sum & K-combined     | -0.16                   |
| Spearman Correlation        | PIF 95% & K-combined      | -0.59                   |
| Pearson Correlation         | PIF 95% & K-combined      | -0.25                   |
| Spearman Correlation        | PIF 95% & SUDA            | 0.91                    |
| Pearson Correlation         | PIF 95% & SUDA            | 0.83                    |


#### EARLY STRESSFUL correlation


| Correlation Type            | Variables                 | Correlation Value       |
|-----------------------------|---------------------------|-------------------------|
| Spearman Correlation        | Suda sum & K-combined     | 0.19                    |
| Pearson Correlation         | Suda sum & K-combined     | 0.10                    |
| Spearman Correlation        | PIF 95% & K-combined      | 0.49                    |
| Pearson Correlation         | PIF 95% & K-combined      | 0.38                    |
| Spearman Correlation        | PIF 95% & SUDA            | 0.71                    |
| Pearson Correlation         | PIF 95% & SUDA            | 0.74                    |


#### MULTI correlation

| Correlation Type            | Variables                 | Correlation Value       |
|-----------------------------|---------------------------|-------------------------|
| Spearman Correlation        | Suda sum & K-combined     | 0.66                    |
| Pearson Correlation         | Suda sum & K-combined     | 0.33                    |
| Spearman Correlation        | PIF 95% & K-combined      | 0.87                    |
| Pearson Correlation         | PIF 95% & K-combined      | 0.70                    |
| Spearman Correlation        | PIF 95% & SUDA            | 0.75                    |
| Pearson Correlation         | PIF 95% & SUDA            | 0.68                    |


#### NIMH correlation

| Correlation Type            | Variables                 | Correlation Value               |
|-----------------------------|---------------------------|---------------------------------|
| Spearman Correlation        | Suda sum & K-combined     | -0.80                           |
| Pearson Correlation         | Suda sum & K-combined     | -0.42            |
| Spearman Correlation        | PIF 95% & K-combined      | -0.67                           |
| Pearson Correlation         | PIF 95% & K-combined      | -0.34            |
| Spearman Correlation        | PIF 95% & SUDA            | 0.88                            |
| Pearson Correlation         | PIF 95% & SUDA            | 0.92       |



#### BTC correlatioon

| Correlation Type            | Variables                 | Correlation Value       |
|-----------------------------|---------------------------|-------------------------|
| Spearman Correlation        | Suda sum & K-combined     | 0.75                    |
| Pearson Correlation         | Suda sum & K-combined     | 0.72       |
| Spearman Correlation        | PIF 95% & K-combined      | 0.86                    |
| Pearson Correlation         | PIF 95% & K-combined      | 0.90      |
| Spearman Correlation        | PIF 95% & SUDA            | 0.81                    |
| Pearson Correlation         | PIF 95% & SUDA            | 0.79      |




