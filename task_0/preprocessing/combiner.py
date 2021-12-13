import os, csv, re
import pandas as pd

# Assume all the xlsx-files are in the same directory as combiner.py.
# Running combiner.py will create a bigger CSV-file from all the xlsx-files, so that the last element in each line is the original file's name.
# This gives us the chance to later filter out which line of data came from which xlsx-file.
# This approach to combine all files into one will save significantly amount of time in future, when processing lines from different files for getting relations.
# NB! Running this file will take a couple of minuties of time. Every file currently in progress is outputed. Please be patient!

files = os.listdir(".")
data_columns = ['Aeg', 'Kasutaja täisnimi', 'Mõjutatud kasutaja', 'Sündmuse kontekst', 'Komponent', 'Sündmuse nimi', 'Kirjeldus', 'Päritolu', 'IP-aadress']
columns_dict = dict()
with open("testfile.csv", "w", encoding = "utf8", newline = "") as tf:
    writer = csv.writer(tf, quoting=csv.QUOTE_ALL)
    for file in files:
        if file.startswith("logs"):
            print("FILE:", file)
            data = pd.read_excel(file)
            data_shape = data.shape
            number_of_lines = data_shape[0]
            list_of_lists = []
            for i in range(number_of_lines):
                data_line = data.loc[i]
                line_to_write = [data_line[data_columns[0]], 
                data_line[data_columns[1]], 
                data_line[data_columns[2]], 
                data_line[data_columns[3]].replace("\n", ""), 
                data_line[data_columns[4]],  
                data_line[data_columns[5]],  
                re.sub(' +', ' ', data_line[data_columns[6]].replace("\n", "")),  
                data_line[data_columns[7]],  
                data_line[data_columns[8]], 
                file]
                list_of_lists.append(line_to_write)
            writer.writerows(list_of_lists)