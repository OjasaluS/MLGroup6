## Task 1

This task needs to solve this problem: 

> Identify students who may be struggling based on their early activities.

We will train a classifier model for this task and incrementally optimize the model, 
and here is what is done at each stage.

### Base

Based on previous attempts at SVM training, 
the code was reorganized to serve as the basis for subsequent work.

[Details](./00_base)

### Add More Data 

In this section, we add `veebirühm` student data, 
which was not added before, to improve the model's performance.

[Details](./01_add_more_data)

### Early Stage Prediction

Since the original problem required predicting student learning at the early stage, 
in this section, 
we use only the first 6 weeks of data for training.

[Details](./02_early_stage)

### Use More Available Data

Consider that while using the Moodle log data of 6 weeks, 
we can also use the assignment and test scores for those 6 weeks as input features, 
which also affect the final grade.

[Details](./03_graded_data)

### Visualization

In this section, we visualize the data for subsequent analysis.

[Details](./04_visualization)

### Remove outliers

In the previous section, 
we observed some apparent outliers in the feature space, 
so we removed them to avoid impacting the subsequent operations.

[Details](./05_remove_outliers)

### Make data balancing

Since there is an imbalance in the data, 
we try to make the training samples more balanced.

[Details](./06_balance_data)

### Scaling Methods Selection

We perform tests in this section to determine which feature scaling method works better.

[Details](./07_scaling_selection)

### Dimensionality Reduction

We try to reduce the dimensionality to test whether it is necessary to reduce the dimensionality and to which extent it is better to reduce it.

[Details](./08_dimensionality)

### Parameters Tuning

In this section, we tune the parameters of the model to obtain better performance.

[Details](./09_params_tuning)

### Final Results

We test our model with the test dataset, 
and analyze the final results.

[Details](./10_results)

### References

The references used in this task are documented in a separate file.

[Details](./references.md)

---

[Next task](../task_2)
