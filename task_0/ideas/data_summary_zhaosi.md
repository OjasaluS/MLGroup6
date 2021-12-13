# Summary of Data

## Logs

### File Name

- **Prefix:** All log files begin with the prefix `logs_LTAT.03.001_`, which corresponds to the course code for analysis. Due to the fact that all files have the same prefix, this information is invalid.
- **Time:** All files were exported around `20210207-0940`, hence the time the table data was exported should not be used as valid information.
- **Group names:** We can observe from the names that students with varying backgrounds have varying prefixes; for example, `AT`, `Inf`, and `FKM` should represent data from students with different majors. Given that one of the factors determining the effectiveness of learning is one's professional experience, this information should be regarded an influencing factor. Additionally, some groups are marked by `veebirühm`, which may need to be used as a reference factor in the analysis. The number in the group name is for identification purposes only and should not be regarded as valid information.

### File Structure

Using the first set of data in the '1slf.txt' file as an example, the following dict illustrates the structure of a single row of the table: 

```json
{
    "Aeg": "4.02.2021 13:07:58",
    "Kasutaja täisnimi": "███████",
    "Mõjutatud kasutaja": "-",
    "Sündmuse kontekst": "Foorum: Foorum",
    "Komponent": "Foorum",
    "Sündmuse nimi": "Kursusemoodulit on vaadatud.",
    "Kirjeldus": "The user with id '███████' viewed the 'forum' activity with course module id '83875'.",
    "Päritolu": "web",
    "IP-aadress": "███████"
}
```

The dictionary's key represents the data's meaning, whereas the dictionary's value represents the data's specific value. 

Questions：

- We can notice that in the description, `Kirjeldus`, some information such as `user id` can be used as a unique identifier. Do we need to distinguish users based on `user id` when we distinguish them? Or is it just by name?
- There is an overlap of information between `Sündmuse kontekst`, `Komponent` and `Kirjeldus`, which data should we use?

Ideas：

- The `Aeg` may reflect the student's living and study habits.
- The changes in `IP-aadress` may reflect whether the student's study location changes frequently.
- The values of `Päritolu` seem to be all `web`, so this attribute should not be considered valid information.
- The frequency of access to the system may be correlated with motivation to learn.

## Hinded

Using the first set of data in the `logs_LTAT.03.001_20210207-0935-AT_01.xlsx` file as an example, the following dict illustrates the structure of a single row of the table: 

```json
{
    "Eesnimi": "███████",
    "Perenimi": "███████",
    "ID-number": "███████",
    "Meiliaadress": "███████",
    "Test:1. nädala test (Punktid)": 0.5,
    "Test:2. nädala test (Punktid)": 0.5,
    "Test:3. nädala test (Punktid)": 0.5,
    "Test:4. nädala test (Punktid)": 0.5,
    "Test:5. nädala test (Punktid)": 0.5,
    "Test:6. nädala test (Punktid)": 0.5,
    "Test:7. nädala test (Punktid)": 0.5,
    "Test:8. nädala test (Punktid)": 0.5,
    "Test:9. nädala test (Punktid)": 0.5,
    "Test:10. nädala test (Punktid)": 0.5,
    "Test:11. nädala test (Punktid)": 0.5,
    "Test:12. nädala test (Punktid)": 0.5,
    "Test:13. nädala test (Punktid)": 0.5,
    "Test:14. nädala test (Punktid)": 0.5,
    "Test:15. nädala test (Punktid)": 0.5,
    "Test:16. nädala test (Punktid)": 0.5,
    "Videoloengud kokku (Punktid)": 7.0,
    "VPL harjutus:1. nädala kodutöö (Punktid)": 0.5,
    "VPL harjutus:Praktikumitöö esitamine (Punktid)": 0.5,
    "VPL harjutus:2. nädala kodutöö (Punktid)": 0.5,
    "VPL harjutus:3. nädala kodutöö (Punktid)": 0.5,
    "VPL harjutus:4. nädala kodutöö (Punktid)": 0.5,
    "VPL harjutus:5. nädala kodutöö (Punktid)": 0.5,
    "VPL harjutus:7. nädala kodutöö (Punktid)": 0.5,
    "VPL harjutus:8. nädala kodutöö (Punktid)": 0.5,
    "VPL harjutus:9. nädala kodutöö (Punktid)": 0.5,
    "VPL harjutus:10. nädala kodutöö (Punktid)": 0.5,
    "VPL harjutus:11. nädala kodutöö (Punktid)": 0.5,
    "VPL harjutus:13. nädala kodutöö (Punktid)": 0.5,
    "VPL harjutus:14. nädala kodutöö (Punktid)": 0.5,
    "VPL harjutus:15. nädala kodutöö (Punktid)": 0.5,
    "Kodutööd kokku (Punktid)": 12.5,
    "Ülesanne:Esita projekti kirjeldus (Punktid)": "-",
    "Ülesanne:Projekti algversioon (Punktid)": 5.0,
    "Ülesanne:Projekti lõppversioon (Punktid)": 5.0,
    "Projekt kokku (Punktid)": 10.0,
    "Test:1. kontrolltöö arvestuslik osa (Punktid)": 1.0,
    "VPL harjutus:1. kontrolltöö programmide esitamine (Punktid)": 19.9,
    "Test:1. KT järeltöö arvestuslik osa (Punktid)": "-",
    "VPL harjutus:1. KT järeltöö programmide esitamine (Punktid)": "-",
    "Test:1. KT 5.01 lisajäreltöö arvestuslik osa (Punktid)": "-",
    "VPL harjutus:1. KT 5.01 lisajäreltöö programmide esitamine (Punktid)": "-",
    "Ülesanne:1. KT 5.01 lisajäreltöö logide ja video esitamine (Punktid)": NaN,
    "Test:1. KT 25.01 lisajäreltöö arvestuslik osa (Punktid)": "-",
    "VPL harjutus:1. KT 25.01 lisajäreltöö programmide esitamine (Punktid)": "-",
    "Ülesanne:1. KT 25.01 lisajäreltöö logide ja video esitamine (Punktid)": NaN,
    "Test:2. kontrolltöö arvestuslik osa (Punktid)": 1.0,
    "VPL harjutus:2. kontrolltöö programmide esitamine (Punktid)": 20.0,
    "Test:2. KT järeltöö arvestuslik osa (Punktid)": "-",
    "VPL harjutus:2. KT järeltöö programmide esitamine (Punktid)": "-",
    "Test:2. KT 6.01 lisajäreltöö arvestuslik osa (Punktid)": "-",
    "VPL harjutus:2. KT 6.01 lisajäreltöö programmide esitamine (Punktid)": "-",
    "Ülesanne:2. KT 6.01 lisajäreltöö logide ja video esitamine (Punktid)": NaN,
    "Test:2. KT 26.01 lisajäreltöö arvestuslik osa (Punktid)": "-",
    "VPL harjutus:2. KT 26.01 lisajäreltöö programmide esitamine (Punktid)": "-",
    "Ülesanne:2. KT 26.01 lisajäreltöö logide ja video esitamine (Punktid)": NaN,
    "Kontrolltööd kokku (Punktid)": 39.9,
    "Ülesanne:Eeleksamile registreerumine (Punktid)": "-",
    "Test:Eeleksami arvestuslik osa (Punktid)": "-",
    "Ülesanne:Eeleksami punktiline osa (Punktid)": "-",
    "Eksamile pääs (Punktid)": "jah",
    "Test:8.01 eksami arvestuslik osa (Punktid)": "-",
    "Test:8.01 eksami punktilise osa 1. ülesanne (Punktid)": "-",
    "VPL harjutus:8.01 eksami punktilise osa 2. ja 3. ülesande esitamine (Punktid)": "-",
    "Ülesanne:8.01 eksami logide ja video esitamine (Punktid)": NaN,
    "Test:14.01 eksami arvestuslik osa (Punktid)": 1.0,
    "Test:14.01 eksami punktilise osa 1. ülesanne (Punktid)": 10.0,
    "VPL harjutus:14.01 eksami punktilise osa 2. ja 3. ülesande esitamine (Punktid)": 20.0,
    "Ülesanne:14.01 eksami logide ja video esitamine (Punktid)": NaN,
    "Test:27.01 eksami arvestuslik osa (Punktid)": "-",
    "Test:27.01 eksami punktilise osa 1. ülesanne (Punktid)": "-",
    "VPL harjutus:27.01 eksami punktilise osa 2. ja 3. ülesande esitamine (Punktid)": "-",
    "Ülesanne:27.01 eksami logide ja video esitamine (Punktid)": NaN,
    "Eksam kokku (Punktid)": 30.0,
    "VPL harjutus:1. lisaülesanne - Muster (Punktid)": 2.0,
    "VPL harjutus:2. lisaülesanne - Tekstispiraal (Punktid)": 2.0,
    "VPL harjutus:3. lisaülesanne - Salasõna (Punktid)": 2.0,
    "VPL harjutus:4. lisaülesanne - Pakkimine (Punktid)": 2.0,
    "VPL harjutus:5. lisaülesanne - Ristmik (Punktid)": 2.0,
    "VPL harjutus:6. lisaülesanne - Labürint (Punktid)": 1.8,
    "VPL harjutus:7. lisaülesanne - Steganograafia (Punktid)": "-",
    "8. lisaülesanne - Lõppküsitlus (Punktid)": 1.0,
    "Praktikumide lisapunktid (Punktid)": 1.0,
    "Projektikonkursi punktid (Punktid)": "-",
    "Lisapunktid kokku (Punktid)": 10.0,
    "VPL harjutus:Pokkerikäte tuvastamise automaatkontroll (Punktid)": "-",
    "Test:Kontrolltöö harjutustest (Punktid)": 9.0,
    "Test:Näidiseksami arvestuslik osa (Punktid)": 4.0,
    "Test:Näidiseksami punktilise osa 1. ülesanne (Punktid)": 9.6,
    "Ülesanne:Näidiseksami logide ja video esitamine (Punktid)": NaN,
    "Harjutamine kokku (Punktid)": "-",
    "Kogutulemus (Punktid)": 109.4,
    "Hinne (Punktid)": 100.0,
    "Sellest kursusest viimati alla laaditud": "1612512348"
}
```

The dictionary's key represents the data's meaning, whereas the dictionary's value represents the data's specific value. 

Questions:

- As can be seen, each week there are corresponding quizzes and assignments involved that affect the final score. 
    - When the model predicts future student performance, it is provided with logs from before the time of the prediction.
    - Question: In addition to the existing logs, does the partner allow for real scores on past assignments and quizzes to be provided as part of the characteristics of the input data?
	- For example, if we want to predict student performance in the fourth week, we have logs data from the last four weeks, but can we also have real scores from assignments and quizzes from these four weeks?

Ideas：

- The weekly quiz and assignment score data, as y, can be used to train the logs data (as x) for a short period of one week to predict the next week's assignment and quiz scores.
- It should be noted that in the [course description](https://courses.cs.ut.ee/2020/programmeerimine/fall), the score for each item has an upper limit. For example, the upper limit of a `Loengud` score is 7.

## Requirements

Partner has made the following requirements:

1. identify students who may be struggling based on their early activities
2. predict the students' final grades in the course
3. discover common activity patterns of the students and create profiles of typical students.

Questions:

- For requirement 3, do we need to summarize user patterns and manually annotate the data manually? Or should we use unsupervised learning to classify user behavior initially and then manually analyze and annotate it?

Ideas:

- For requirement 1, it seems that training a classifier is more in line with the requirement.
- For requirement 2, regression analysis should be considered.

## How to Process

If we treated each point in time of the student's actions as a feature, we would create a problem of multidimensional features that would make analysis difficult. Considering the behavior of students who have used Moodle for a short interval of time, it makes no chronological sense. As a result, two preliminary approaches are as follows:

1. To serve as input features, the amount and frequency of various operations done by students are calculated. 
    - However, focusing exclusively on the total amount and frequency of data changes over the semester obscures the trend of data changes.
2. Alternatively, some statistics on student behaviors might be used as input features on a weekly basis.
This can be used to create a weekly time series, with the y-values corresponding to a value representing the weekly homework, practice, and classroom performance scores. 
    - The final grade, however, is influenced by the final exam and projects and is not simply the sum of weekly homework and lecture grades.
