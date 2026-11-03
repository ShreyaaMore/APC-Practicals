"""
University System Package
A modular Object-Oriented University Management System.
"""

from .config import APP_NAME, GPA_SCALE, CURRENCY_SYMBOL, DEFAULT_DATA_FILE, GRADE_WEIGHTS, LETTER_GRADE_THRESHOLDS
from .models import Person, Student, Instructor
from .courses import Department, Course
from .enrollment import Grade, Enrollment
from .university import UniversitySystem

__all__ = [
    "APP_NAME",
    "GPA_SCALE",
    "CURRENCY_SYMBOL",
    "DEFAULT_DATA_FILE",
    "GRADE_WEIGHTS",
    "LETTER_GRADE_THRESHOLDS",
    "Person",
    "Student",
    "Instructor",
    "Department",
    "Course",
    "Grade",
    "Enrollment",
    "UniversitySystem",
]
