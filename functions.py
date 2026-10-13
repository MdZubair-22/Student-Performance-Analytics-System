"""Reusable calculations for the CampusMarks student analysis project."""
import numpy as np
import pandas as pd

SUBJECTS = ["python", "mathematics", "statistics", "data_analysis"]


def grade_from_average(average):
    """Return a grade using the rules documented in README.md."""
    if average >= 90:
        return "A+"
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"
    return "F"


def prepare_results(data):
    """Return a copy of the input DataFrame with calculated result columns."""
    result = data.copy()
    result["total_marks"] = result[SUBJECTS].sum(axis=1)
    result["average_marks"] = np.round(result[SUBJECTS].mean(axis=1), 2)
    result["grade"] = result["average_marks"].apply(grade_from_average)
    # A student must score at least 35 in every subject to pass.
    result["result"] = result[SUBJECTS].ge(35).all(axis=1).map({True: "Pass", False: "Fail"})
    result["attendance_status"] = np.where(result["attendance_percent"] >= 75, "Eligible", "Below 75%")
    return result


def class_summary(results):
    """Build a compact summary using Pandas and NumPy."""
    subject_averages = results[SUBJECTS].mean().round(2)
    pass_count = int((results["result"] == "Pass").sum())
    fail_count = int((results["result"] == "Fail").sum())
    return {
        "student_count": int(len(results)),
        "class_average": round(float(np.mean(results["average_marks"])), 2),
        "highest_average": round(float(results["average_marks"].max()), 2),
        "lowest_average": round(float(results["average_marks"].min()), 2),
        "pass_count": pass_count,
        "fail_count": fail_count,
        "subject_averages": subject_averages,
    }


def top_students(results, count=5):
    """Return the highest scoring students, with ties ordered by name."""
    return results.sort_values(["average_marks", "name"], ascending=[False, True]).head(count)
