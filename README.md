# Student Performance Analytics System

This Python project reads student marks from a CSV file and shows a summary
of the class. It uses Pandas to work with the data and NumPy for calculations.

## Features

- Calculates total and average marks for each student.
- Assigns grades based on the average.
- Shows whether each student passed or failed.
- Calculates subject averages and class performance.
- Lists the five students with the highest averages.
- Saves detailed results and subject averages as CSV files in `output/`.

## Project files

- `main.py` reads and validates the data, then prints the report.
- `functions.py` contains reusable calculation and summary functions.
- `students.csv` contains 22 fictional sample records, including two students
  who fail at least one subject.
- `test_project.py` contains tests for the grade and result calculations.
- `requirements.txt` lists the Python packages used.
- [Documentation](Documentation.pdf)

## Grade and result rules

Grades are based on the average mark across the four subjects:

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

## Run the project

Install Python 3.10 or later. In a terminal opened in this folder, run:

```bash
python -m pip install -r requirements.txt
python main.py
```

The program prints the class summary, subject averages, top students, and
individual results. It creates `output/student_results.csv` and
`output/subject_averages.csv`.

To run the tests:

```bash
python -m unittest test_project.py
```

## Use a different dataset

You can replace the rows in `students.csv`, but keep the column names the
same. Marks and attendance must be numbers from 0 to 100. The included names
and marks are fictional. Do not publish real student information without
permission.
