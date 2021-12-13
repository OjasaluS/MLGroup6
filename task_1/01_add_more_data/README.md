## 01 Add More Data 

In the previous attempts, 
considering that the students of `veebirühm` might not use Moodle as often as the other groups because they were taught online, 
then the data of `veebirühm` were not added to avoid interference.

However, the poor results of the previous model may also be due to the small sample. 
Therefore, we add data from the `veebirühm` group for testing in this section.

Therefore, the data of all 342 students will be used for training in this section.

The number of samples increased by 54 after adding the data directly. 
At the same time, since the data of the `veebirühm` group may introduce bias after all, 
we add labels `web` to the `veebirühm` group.

- `data.csv`: Generated data files that have been desensitized. And `veebirühm` group data is added.
- `data.ipynb`: Get the data.
- `train.ipynb`: Train the classifier.

Result:

We consider the category with a score below 50 as the positive class.

- Accuracy: `96.18%`
- Recall rate: `53.33%`

### Can we trust the results?

We cannot yet, because the recall rate is low, reflecting that the data may be very unbalanced. 
Therefore, when we do data splitting, how the data is split may impact the results.

---

[Next section](../02_early_stage)

[Back to Task 1](../../task_1)
