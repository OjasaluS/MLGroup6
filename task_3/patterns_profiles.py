import pandas as pd
import matplotlib.pyplot as plt 

# make a dictionary out of grades file: key = name, value = list of potentially useful data
names_scores = dict()
# make a dictionary out of grades file: key = name, value = final grade
student_and_grade = dict()

def getGrade(score):
    if 90 <= float(score):
        return "A"
    elif 80 <= float(score) < 90:
        return "B"
    elif 70 <= float(score) < 80:
        return "C"
    elif 60 <= float(score) < 70:
        return "D"
    elif 50 <= float(score) < 60:
        return "E"
    else:
        return "F"
grades_data = pd.read_excel("02-05 Hinded.xlsx")
columns = grades_data.columns
columns_normal_list = [c for c in columns]
data_shape = grades_data.shape
number_of_lines = data_shape[0]
for i in range(number_of_lines):
    data_line = grades_data.loc[i]  
    name = data_line[columns_normal_list[0]] + " " + data_line[columns_normal_list[1]]
    scores = [data_line[columns_normal_list[j]] for j in range(4, len(columns_normal_list))]
    names_scores[name] = scores
    student_and_grade[name] = getGrade(data_line[columns_normal_list[-3]])

# make a dictionary out of preprocessed data file: key = names, value = list of activity names (Sündmuse nimi, can be duplicates) 
# for testfile.csv see task_0/preprocessing folder
student_and_activities = dict()
with open("testfile.csv", "r", encoding = "utf8") as f:
    for line in f:
        line_splitted = line.split('","')
        student = line_splitted[1]
        activity = line_splitted[5]
        if student not in student_and_activities:
            student_and_activities[student] = [activity]
        else:
            current_list = student_and_activities[student]
            current_list.append(activity)
            student_and_activities[student] = current_list

# make a dictionary of activities and their occurrences: : key = activity, value = occurrence 
all_occurences = dict()
print("Examples of certain grade with all occurrences of activities:")
print("----------------------------------------------------------------------------------------------------\n")
possible_grades = []
for s in student_and_grade.keys():
    if s in student_and_activities:
        final_grade = student_and_grade[s]
        activities = student_and_activities[s]
        activities_occurences = dict((a, activities.count(a)) for a in set(activities))
        activities_occurences_sorted = {k: v for k, v in sorted(activities_occurences.items(), key=lambda item: item[1], reverse = True)}
        activities_occurences_sorted_list = list(activities_occurences_sorted)
        for activity_element in activities_occurences_sorted_list:
            number_occurred = activities_occurences_sorted[activity_element]
            if activity_element not in all_occurences:
                all_occurences[activity_element] = number_occurred
            else:
                new_number_occurrence = all_occurences[activity_element] + number_occurred
                all_occurences[activity_element] = new_number_occurrence
        if final_grade not in possible_grades:
            print('A student who got the grade "{}", had the following activities:'.format(final_grade), activities_occurences_sorted)
            print("----------------------------------------------------------------------------------------------------")
            possible_grades.append(final_grade)

all_occurences_sorted = {k: v for k, v in sorted(all_occurences.items(), key=lambda item: item[1], reverse = True)}
#print(all_occurences_sorted)

# Plot out all the occurrences of activities to see which are the most common activities.
# The decision was to show only the top 5 and bottom 5 occurrences as otherwise it's hard to understand the plotting.
# There are two types of plots: pie chart plot and bar plot.
# Close the previous plot to see the next (didn't combine both into one plot as it would have been difficult to understand again).
def plotPieChart(x, y, title):    
    plt.figure(figsize = (10, 7))
    plt.pie(x, labels = y)
    plt.title(title) 
    plt.show()

def plotBar(x, y, title):
    plt.figure(figsize = (15, 7))
    plt.bar(x, y, color=['black', 'red', 'green', 'blue', 'cyan'])
    plt.title(title) 
    plt.xlabel("Activities", fontweight ='bold', fontsize = 12)
    plt.ylabel("Occurrences of activity", fontweight ='bold', fontsize = 12)
    plt.show()

plotPieChart(list(all_occurences_sorted.values())[:5], list(all_occurences_sorted.keys())[:5], "Top 5 activities")
plotPieChart(list(all_occurences_sorted.values())[-5:], list(all_occurences_sorted.keys())[-5:], "Bottom 5 activities")
plotBar(list(all_occurences_sorted.keys())[:5], list(all_occurences_sorted.values())[:5], "Top 5 activities")
plotBar(list(all_occurences_sorted.keys())[-5:], list(all_occurences_sorted.values())[-5:], "Bottom 5 activities")
