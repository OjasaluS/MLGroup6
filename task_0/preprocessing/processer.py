import pandas as pd
import csv

# processer.py has currently the following purposes:
# 1. It searches for student's id and when it is identifiable, then it will be added at the end of the line. If there's no id, then the value of the id will be and empty string.
# 2. All lines will be written to testfile_with_ids.csv file, which has the same purpose of testfile.csv - to be able to process lines more quickly than accessing all the xlsx-files separately.
# 3. There's a small analysis as well. We compare the number of lines where the id was available and the number of lines where it wasn't. Using sets we find out which lines didn't have an id of a student (currently commented out).
# 4. We make a dictionary of persons (keys) and ids from log data (values).
# 5. Created persons_and_ids.csv file based on grades file. This gives us the possibility to match students from log files with the exact line from grades. TODO part is that the grades file needs to be proecessed.
# Sidenote: it is indeed reasonable to combine this file with combiner.py file into one.

counter = 0
line_counter = 0
all_lines = set()
processed_lines = set()
person_id = dict()
with open("testfile.csv", "r") as t, open("testfle_with_ids.csv", "w") as twi:
    for line in t:
        all_lines.add(line)
        line_counter += 1
        id = None
        line_splitted = line.split('","')
        if line_splitted[1] not in person_id:
            person_id[line_splitted[1]] = set()
        if "with id" in line_splitted[6] or "loodi ID-ga" in line_splitted[6] or "The user id " in line_splitted[6] or " user id id " in line_splitted[6]:
            element_with_id_splitted = line_splitted[6].split()
            for e in range(len(element_with_id_splitted)):
                if element_with_id_splitted[e] == "The" and element_with_id_splitted[e + 1] == "user" and element_with_id_splitted[e + 2] == "with" and element_with_id_splitted[e + 3] == "id":
                    if element_with_id_splitted[e + 4].isdigit():
                        id = element_with_id_splitted[e + 4]
                        counter += 1
                        processed_lines.add(line)
                        break
                    else:
                        possible_digit_without_quotes = element_with_id_splitted[e + 4].replace('"', '').replace("'", '')
                        if possible_digit_without_quotes.isdigit():
                            id = possible_digit_without_quotes
                            counter += 1
                            processed_lines.add(line)
                            break
                elif element_with_id_splitted[e] == "The" and element_with_id_splitted[e + 1] == "user" and element_with_id_splitted[e + 2] == "id":
                    if element_with_id_splitted[e + 3].isdigit():
                        id = element_with_id_splitted[e + 3]
                        counter += 1
                        processed_lines.add(line)
                        break
                    else:
                        possible_digit_without_quotes = element_with_id_splitted[e + 3].replace(".", "").replace('"', '').replace("'", '')
                        if possible_digit_without_quotes.isdigit():
                            id = possible_digit_without_quotes
                            counter += 1
                            processed_lines.add(line)
                            break
                elif element_with_id_splitted[e] == "by" and element_with_id_splitted[e + 1] == "the" and element_with_id_splitted[e + 2] == "user" and element_with_id_splitted[e + 3] == "with" and element_with_id_splitted[e + 4] == "id":
                    if element_with_id_splitted[e + 5].isdigit():
                        id = element_with_id_splitted[e + 5]
                        counter += 1
                        processed_lines.add(line)
                        break
                    else:
                        possible_digit_without_quotes = element_with_id_splitted[e + 5].replace(".", "").replace('"', '').replace("'", '')
                        if possible_digit_without_quotes.isdigit():
                            id = possible_digit_without_quotes
                            counter += 1
                            processed_lines.add(line)
                            break
                elif element_with_id_splitted[e] == "Student" and element_with_id_splitted[e + 1] == "with" and element_with_id_splitted[e + 2] == "id":
                    if element_with_id_splitted[e + 3].isdigit():
                        id = element_with_id_splitted[e + 3]
                        counter += 1
                        processed_lines.add(line)
                        break
                elif element_with_id_splitted[e] == "User" and element_with_id_splitted[e + 1] == "with" and element_with_id_splitted[e + 2] == "id":
                    if element_with_id_splitted[e + 3].isdigit():
                        id = element_with_id_splitted[e + 3]
                        counter += 1
                        processed_lines.add(line)
                        break
                elif element_with_id_splitted[e] == "ID-ga":
                    if element_with_id_splitted[e + 1].isdigit():
                        id = element_with_id_splitted[e + 1]
                        counter += 1
                        processed_lines.add(line)
                        break
                    else:
                        possible_digit_without_quotes = element_with_id_splitted[e + 1].replace(".", "").replace('"', '').replace("'", '')
                        if possible_digit_without_quotes.isdigit():
                            id = possible_digit_without_quotes
                            counter += 1
                            processed_lines.add(line)
                            break
                elif element_with_id_splitted[e] == "user" and element_with_id_splitted[e + 1] == "id":
                    if element_with_id_splitted[e + 2].isdigit():
                        id = element_with_id_splitted[e + 2]
                        counter += 1
                        processed_lines.add(line)
                        break
                elif element_with_id_splitted[e] == "id" and element_with_id_splitted[e + 1] == "id":
                    if element_with_id_splitted[e + 2].isdigit():
                        id = element_with_id_splitted[e + 2]
                        counter += 1
                        processed_lines.add(line)
                        break
                    else:
                        possible_digit_without_quotes = element_with_id_splitted[e + 2].replace(".", "").replace('"', '').replace("'", '')
                        if possible_digit_without_quotes.isdigit():
                            id = possible_digit_without_quotes
                            counter += 1
                            processed_lines.add(line)
                            break
        person_id[line_splitted[1]].add(id)

        line_to_write = line[:-1]
        if id is not None:
            line_to_write += ',"' + id + '"\n'
        else:
            line_to_write += ',""\n'
        twi.write(line_to_write)

# Check how many lines have been processed and how many lines there are.
print(counter, line_counter)
# Determine if every line is unique.
print(len(all_lines))

# Loop through lines, whichc didn't managed to enter the processing.
# unprocessed_lines = all_lines - processed_lines
# for ul in unprocessed_lines:
#    print(ul)

#Dictionary of persons located in grades file.
persons_in_grades_file = dict()
identification_data_columns = ["Eesnimi", "Perenimi", "ID-number"]
grades_data = pd.read_excel("02-05 Hinded.xlsx")
data_shape = grades_data.shape
number_of_lines = data_shape[0]
for i in range(number_of_lines):
    data_line = grades_data.loc[i]  
    name = data_line[identification_data_columns[0]] + " " + data_line[identification_data_columns[1]]
    id_number = data_line[identification_data_columns[2]]
    persons_in_grades_file[id_number] = name

print("Number of persons found in grades file:", len(persons_in_grades_file))
print("Number of persons found in log files:", len(person_id))

logs_persons = set(person_id.keys())

# There are some encoding issues with pandas, so an new file persons_and_ids.csv will be created
with open("persons_and_ids.csv", "w", encoding = "utf8", newline = "") as pf:
    writer = csv.writer(pf, quoting=csv.QUOTE_ALL)
    list_of_lists = []
    for person_idd in persons_in_grades_file:
        list_of_lists.append([persons_in_grades_file[person_idd], person_idd])
    writer.writerows(list_of_lists)

unique_persons_from_grades_file = set()

with open("persons_and_ids.csv", "r") as p:
    for line in p:
        line_splitted = line.split('","')
        name = line_splitted[0].replace('"', '')
        unique_persons_from_grades_file.add(name)

# And now we can make the subtraction of two sets. #FIXME: small difference in expected numbers, need to find out why
print(logs_persons - unique_persons_from_grades_file)

# Let's finally make a file of grades 
#TODO
