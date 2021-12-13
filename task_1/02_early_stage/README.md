## 02 Early Stage Prediction

Since the task requires `predict based on early activities`, 
we cannot use all 16 weeks of data.

This section will extract only the first 6 weeks of data for the `early stage` for subsequent analysis.

- `data.csv`: Generated data files that have been desensitized. Only the first 6 weeks of data were extracted.
- `data.ipynb`: Get the data.
- `train.ipynb`: Train the classifier.

Result:

- Accuracy: `92.21%`
- Recall rate: `13.00%`

Compared to the previous section, 
the classification performance is significantly reduced. 
This is expected, 
as classification recognition becomes difficult due to data reduction.

---

[Next section](../03_graded_data)

[Back to Task 1](../../task_1)
