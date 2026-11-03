# University Management System

The system models university operations including department organization, course catalog management, faculty assignments, student enrollments, weighted grade calculations (midterm, final exam, assignments), and cumulative GPA tracking on a 10.0 scale.

Data is stored on a local JSON database. The project provides a Tkinter-based Desktop Graphical User Interface (GUI).

## Project Structure

```text
University-Management-System/
├── university_system/          # Core package
│   ├── __init__.py             # Public package exports
│   ├── __main__.py             # Package execution entry point
│   ├── config.py               # System constants (10.0 GPA scale, weights, thresholds)
│   ├── models.py               # Person, Student, and Instructor classes
│   ├── courses.py              # Department and Course classes
│   ├── enrollment.py           # Enrollment and Grade classes
│   ├── university.py           # UniversitySystem central manager and JSON persistence
│   └── demo.py                 # Automated demonstration test suite
├── utils/                      # Helper utilities
│   ├── __init__.py
│   └── helpers.py              # Formatting helpers (currency, GPA conversion)
├── data/                       # Local JSON storage
│   └── university_data.json    # Persistent JSON database (contains 20 student records)
├── reports/                    # Exported outputs and CSV reports
├── app.py                      # Desktop GUI application (Tkinter)
├── __init__.py                 # Root package export
└── README.md                   # Project documentation
```

## Features

- **Desktop GUI**: Built with Tkinter and Matplotlib. Includes tabbed views for students, instructors, courses, enrollments, grades, graphical analytics charts, and CSV data export.
- **Automatic JSON Persistence**: Loads saved state from `data/university_data.json` at startup. Every edit operation (add, update, delete, enroll, record grade) writes directly to the local JSON file.
- **Data Export**: Generates standardized CSV exports for students, instructors, courses, and grade reports.

## Requirements

- Python 3.10 or higher
- Standard library modules: `json`, `csv`, `os`, `sys`, `abc`, `re`, `datetime`
- Optional for GUI and charts: `matplotlib`

## Running the Application

###  Desktop GUI
Launch the graphical interface:
```bash
python main.py --gui
```
Or run directly:
```bash
python gui.py
```


## Acknowledgments

Developed as an academic project demonstrating Object-Oriented Programming, multi-file package design, and persistent software architecture in Python.

Semester V, Advanced Programing Concepts.