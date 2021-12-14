# MLGroup6

## About the project

- **Title:** P06 - Student profiling based on Moodle log data
- **Project type:** Based on partner project (P14)
- **Description:** Based on Moodle log file as a dataset of Computer Programming course identify possible struggling students, predict students' final grades, discover common activity patterns and create profiles of typical students.

## About the team

Team members:

- [Siim-Morten Ojasalu](https://github.com/OjasaluS)
- [Martin Reinsalu](https://github.com/MartinUT)
- [Kristiina Hakk](https://github.com/kristiina-h)
- [Zhaosi Qu](https://github.com/chaosrun)

## Tasks

According to the description, we have three tasks:

1. Identify students who may be struggling based on their early activities.
2. Predict the students' final grades in the course.
3. Discover common activity patterns of the students and create profiles
of typical students.

---

### Task 0

*Preparation, understanding the data, and discussion.*

Everyone was involved in the preparation and discussion, and contributed their [ideas](./task_0/ideas). In addition, Siim-Morten Ojasalu answered some technical related questions from other team members, prepared and delivered an intermediate presentation; Martin Reinsalu wrote [the scripts](./task_0/preprocessing) used to process the data; Kristiina Hakk researched some relevant papers and shared them; and Zhaosi Qu tried [modeling experiments](./task_0/first_try).

---

### Task 1

*Identify students who may be struggling based on their early activities.*

- [Zhaosi Qu](https://github.com/chaosrun) is assigned to this task.
- Summary: The model can predict whether a student is struggling in the study based on log data from the first six weeks, scores from the first six weeks of lectures + homework + practice, and scores from the sixth week's test. Through the validation of the test set, the accuracy of the model is above `91%` and the recall rate is above `83%`, up to `100%` (one of the models, performance on test dataset).
- [Details](./task_1)

---

### Task 2

*Predict the students' final grades in the course.*

- [Siim-Morten Ojasalu](https://github.com/OjasaluS) is assigned to this task.
- Summary: We can predict the final grades after the 12th week and with good accuracy and low MSE / MAE, as the magnitude of error is quite low.
- [Details](./task_2)

---

### Task 3

*Discover common activity patterns of the students and create profiles of typical students.*

- [Martin Reinsalu](https://github.com/MartinUT) and [Kristiina Hakk](https://github.com/kristiina-h) are assigned to this task.
- Summary: Made an analyzing script, which groups the activities by final grades and outputs an example of every grade. Also plots top and bottom five activities overall. 
- [Details](./task_3)

In addition, [Zhaosi Qu](https://github.com/chaosrun) provided another profiling method based on KMeans, [details here](./task_3/kmeans).
