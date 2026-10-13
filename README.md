# Student Performance Analytics

This is a small Python project that reads student marks from a CSV file and
shows a summary of the class. It uses Pandas to work with the table of marks
and NumPy for calculations.

## What it does

- Calculates each student's total and average marks.
- Gives a grade based on the average.
- Shows whether each student passed or failed.
- Calculates the average mark for each subject.
- Prints the class average, highest and lowest averages, and pass/fail counts.
- Lists the five students with the highest averages.
- Saves the results as CSV files in the `output` folder.

## Project files

- `main.py` reads the data, checks it, and prints the results.
- `functions.py` contains the functions for calculating results and summaries.
- `students.csv` is the sample data file. It has 22 fictional student records, including two students who fail one or more subjects.
- `output/` contains the CSV files created when the program runs.

## Rules used

Grades are based on the average of the four subject marks:

| Average | Grade |
|---:|:---|
| 90 or more | A+ |
| 80 to below 90 | A |
| 70 to below 80 | B |
| 60 to below 70 | C |
| 50 to below 60 | D |
| Below 50 | F |

A student passes if they get at least 35 marks in every subject. Attendance
of 75% or more is shown as `Eligible`.

## Run the program

Install Python 3.10 or later, then open a terminal in this folder and run:

```bash
python -m pip install -r requirements.txt
python main.py
```

The program prints the summary and saves `student_results.csv` and
`subject_averages.csv` inside `output/`.

## Using different data

You can replace the rows in `students.csv`. Keep the column names the same,
and enter marks and attendance as numbers from 0 to 100. The sample names and
marks are fictional. Do not use or share real student information without
permission.
