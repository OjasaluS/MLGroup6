## 00 Base 

This section mainly takes the code from previous attempts to train the model using SVM and refines it to make the structure clearer.

The included files in this section can be considered the base for later work.

- `data.csv`: Generated data files that have been desensitized.
- `data.ipynb`: Get the data.
- `same_name_detect.ipynb`: Make sure there are no students with the same name.
- `train.ipynb`: Train the classifier.

### Results

We consider the category with a score below 50 as the positive class.

- Accuracy: `95.50%`
- Recall rate: `49.62%`

With a recall rate below 50%, this is not a good result.

---

[Next section](../01_add_more_data)

[Back to Task 1](../../task_1)
