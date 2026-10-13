"""CampusMarks: a small command-line student performance analysis project."""
from pathlib import Path
import pandas as pd
from functions import SUBJECTS, prepare_results, class_summary, top_students

ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "students.csv"
OUTPUT_DIR = ROOT / "output"


def load_students():
    """Load records and check the columns needed for analysis."""
    data = pd.read_csv(DATA_FILE)
    required = {"student_id", "name", "department", "attendance_percent", *SUBJECTS}
    missing = required.difference(data.columns)
    if missing:
        raise ValueError("Missing required column(s): " + ", ".join(sorted(missing)))
    if data.empty:
        raise ValueError("The student CSV contains no records.")
    if data[SUBJECTS + ["attendance_percent"]].isna().any().any():
        raise ValueError("Marks or attendance contain blank values. Please correct students.csv.")
    for column in SUBJECTS + ["attendance_percent"]:
        if not data[column].between(0, 100).all():
            raise ValueError(f"Values in {column} must be between 0 and 100.")
    return data


def show_report(results):
    summary = class_summary(results)
    print("\n" + "=" * 64)
    print(" CAMPUSMARKS | STUDENT PERFORMANCE REPORT")
    print("=" * 64)
    print(f"Students analysed : {summary['student_count']}")
    print(f"Class average     : {summary['class_average']} / 100")
    print(f"Highest average   : {summary['highest_average']} / 100")
    print(f"Lowest average    : {summary['lowest_average']} / 100")
    print(f"Passed / failed   : {summary['pass_count']} / {summary['fail_count']}")

    print("\nSUBJECT AVERAGES")
    for subject, average in summary["subject_averages"].items():
        print(f"  {subject.replace('_', ' ').title():<18} {average:>6.2f}")

    print("\nTOP 5 STUDENTS")
    display_cols = ["student_id", "name", "department", "average_marks", "grade"]
    print(top_students(results)[display_cols].to_string(index=False))

    print("\nSTUDENT RESULTS")
    result_cols = ["student_id", "name", "total_marks", "average_marks", "grade", "result", "attendance_status"]
    print(results[result_cols].to_string(index=False))


def save_outputs(results):
    OUTPUT_DIR.mkdir(exist_ok=True)
    results.to_csv(OUTPUT_DIR / "student_results.csv", index=False)
    subject_averages = results[SUBJECTS].mean().rename_axis("subject").reset_index(name="average_marks")
    subject_averages.to_csv(OUTPUT_DIR / "subject_averages.csv", index=False)
    print(f"\nSaved detailed results to: {OUTPUT_DIR / 'student_results.csv'}")
    print(f"Saved subject averages to: {OUTPUT_DIR / 'subject_averages.csv'}")


def main():
    try:
        students = load_students()
        results = prepare_results(students)
        show_report(results)
        save_outputs(results)
    except (OSError, ValueError, pd.errors.ParserError) as error:
        print(f"Could not complete the analysis: {error}")
        print("Check that students.csv is in the project folder and its values are valid.")


if __name__ == "__main__":
    main()
