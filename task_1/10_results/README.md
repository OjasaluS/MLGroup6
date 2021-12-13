## 10 Results

In this section, we use the test dataset and test the model. 
For the model parameters, 
we use the values obtained from the search in the previous section.

- `data.csv`: Generated data files that have been desensitized.
- `SMOTE.ipynb`: MinMaxScaler + SMOTE + RandomForest + SVM.
- `Weight.ipynb`: MinMaxScaler + RandomForest + SVM + Class weight.

We consider the category with a score below 50 as the positive class.

### SMOTE.ipynb

- Accuracy: `91.18%`
- Recall rate: `100.00%`
- ROC-AUC: `0.88`

### Weight.ipynb

- Accuracy: `92.65%`
- Recall rate: `83.33%`
- ROC-AUC: `0.85`

### Overview

After continuous adjustment and experimentation, 
the recall rate of the model is continuously improving. 
Also, the AOC RUC scores prove that the model's performance is indeed improving.

Finally, through the validation of the test set, 
the accuracy of the model is above 90% and the recall rate is above 80%, 
up to 100%

---

[Back to Task 1](../../task_1)

[Go to Task 2](../../task_2)
