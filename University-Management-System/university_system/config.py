"""
Configuration constants for University Management System
"""
import os

APP_NAME = "National University Management System"
GPA_SCALE = 10.0
CURRENCY_SYMBOL = "₹"
DEFAULT_DATA_FILE = os.path.join("data", "university_data.json")

GRADE_WEIGHTS = {
    "midterm": 0.30,
    "final": 0.50,
    "assignments": 0.20,
}

LETTER_GRADE_THRESHOLDS = [
    (90, "A"),
    (80, "B"),
    (70, "C"),
    (60, "D"),
    (0,  "F"),
]
