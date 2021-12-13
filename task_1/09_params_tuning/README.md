## 09 Parameters Tuning

In this section, we first use ·cross_validate· to tune the number of features selected from RandomForest. Then, we use GrindSearchCV to perform parameters searching for C, gamma, and class_weight of the SVM.

Since the data tend to be balanced under SMOTE, the class_weight is set between 0.1 and 2. The search range for Weight is set between 1.5 and 3.

- `data.csv`: Generated data files that have been desensitized.
- `SMOTE_tuning.ipynb`: MinMaxScaler + SMOTE + RandomForest + SVM.
- `Weight_tuning.ipynb`: MinMaxScaler + RandomForest + SVM + Class weight.

### Results

#### SMOTE_tuning.ipynb

- Total features: `10`
- Best score: `0.9488`
- C: `446.41588833612777`
- gamma: `0.021544346900318822`
- class_weight: `{1: 0.19743589743589746}`

#### Weight_tuning.ipynb

- Total features: `16`
- Best score: `0.9418`
- C: `1291549.6650148828`
- gamma: `4.641588833612782e-07`
- class_weight: `{1: 2.6}`

---

[Next section](../10_results)

[Back to Task 1](../../task_1)
