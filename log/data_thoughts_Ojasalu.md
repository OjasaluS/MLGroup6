# First thoughts and comments

## Answering questions

### Regarding all the logs
I think what Zhaosi wrote was very informative. Just to answer some questions from my perspective:
- We can notice that in the description, `Kirjeldus`, some information such as `user id` can be used as a unique identifier. Do we need to distinguish users based on `user id` when we distinguish them? Or is it just by name?
I think that the way we distinguish does not really matter as long as it can be traced backed to a certain person. 
Numerical data is always easier to work with and if the IDs are unique, which they should be, it is easier to work with that instead of having to deal with processing the names aswell.
- There is an overlap of information between `Sündmuse kontekst`, `Komponent` and `Kirjeldus`, which data should we use?
I think that there is too much information in these cells. By that I mean, if we want to feed such data to a model it will get very confusing. There are just so many different little things. 
For me personally it feels that the 'Sündmuste nimi' is most important. As what the person actually did - did he/she complete a test or revise something. 
Otherwise there is a ton of data noise in the files and including it all feels like a really bad overfit. What if the test names change or something like that? How would the model predict then?

### Hinded
Again answering the questions Zhaosi brought out.
- As can be seen, each week there are corresponding quizzes and assignments involved that affect the final score. 
    - When the model predicts future student performance, it is provided with logs from before the time of the prediction.
    - Question: In addition to the existing logs, does the partner allow for real scores on past assignments and quizzes to be provided as part of the characteristics of the input data?
    I think that should be the case, otherwise it's quite hard to predict any result. One might redo a test 10 times but still fail 50% of the questions. Some actual results should be required for predictions.
	- For example, if we want to predict student performance in the fourth week, we have logs data from the last four weeks, but can we also have real scores from assignments and quizzes from these four weeks?
	Highly likely, yes. At least in my opinion. Otherwise we can predict which student works hard and spends a lot of time on moodle but not much else?
  
### Requirements
- For requirement 3, do we need to summarize user patterns and manually annotate the data manually? Or should we use unsupervised learning to classify user behavior initially and then manually analyze and annotate it?
That's a tough one. Maybe we do not need to do anything manually. If we can predict the final grade we could compare it to amount of time spent solving test exercises for example. 
And from there identify hard workers and lazy people or something like that?

### Processing
I completely agree with the fact that if we consider every action as a feature it will just overwhelm the model. 
It does not make sense and I think it would not benefit us aswell.

- The final grade, however, is influenced by the final exam and projects and is not simply the sum of weekly homework and lecture grades.
We could use this to maybe be able to predict the exam points? If a student does well on all tests then it's more likely that they do well on the exam aswell?
We basically have to predict on something. It can not be perfect but if we want to predict lecture grades then we can't just expect the input to be all the points.
The model should perform better with more input information but I think it should be able to make some kind of prediction even with 2 weeks data for example.
A few test results and moodle usage. I think our approach and solution plays a bigger role than the accuracy of the model. But that's my opinion and how I have understood.

## My thoughts on the data
As I brought out in some of my answers above, I think the data is really noisy. There is so much information that is not needed or otherwise it would just overwhelm us.
We need to figure out a way to utilize the logs as simply as possible. I think that simplicity would yield better results here.
### Approaches
For example, count the times a student solves a test on moodle, count the amount of times he/she reviews it. Add up the test results that he/she has gotten so far.

During 4 weeks, student A has practiced 4 tests, in total 19 times. From 4 weekly tests he/she has received a maximum amount of points.
Predict grade based on these results.

Maybe this approach is a bit too simple and certain aspects can be added. But we have to consider the amount of cleaning we have to do on the data. Too many features make it a lot more complex.

Identifying struggling students could actually be quite hard because it depends how one would define struggling student. Is it someone who is just on track for a bad grade?
Or someone who tries really hard but still can not get the desired results? Based on this definition the model will differ a lot.
I think that a struggling student is someone who tries a lot but maybe just does not grasp the concept. Therefore maybe look at moodle logs and compare to results.
So if the student completes a lot of test exercises but still gets a low point amount then he/she might be struggling. If a student doesn't study and gets bad grades, then it is just on them and their laziness.
