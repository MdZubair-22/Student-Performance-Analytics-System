"""Basic checks for the main calculations. Run with: python -m unittest test_project.py"""
import unittest
import pandas as pd
from functions import grade_from_average, prepare_results

class CampusMarksTests(unittest.TestCase):
    def test_grade_boundaries(self):
        self.assertEqual(grade_from_average(95), "A+")
        self.assertEqual(grade_from_average(85), "A")
        self.assertEqual(grade_from_average(75), "B")
        self.assertEqual(grade_from_average(65), "C")
        self.assertEqual(grade_from_average(55), "D")
        self.assertEqual(grade_from_average(49), "F")

    def test_result_columns(self):
        row = pd.DataFrame([{
            "student_id": "T1", "name": "Test Student", "department": "AIML",
            "python": 80, "mathematics": 70, "statistics": 60,
            "data_analysis": 90, "attendance_percent": 80
        }])
        result = prepare_results(row).iloc[0]
        self.assertEqual(result["total_marks"], 300)
        self.assertEqual(result["average_marks"], 75)
        self.assertEqual(result["result"], "Pass")
        self.assertEqual(result["attendance_status"], "Eligible")

if __name__ == "__main__":
    unittest.main()
