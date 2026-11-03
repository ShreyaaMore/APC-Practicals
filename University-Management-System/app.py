import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
import os
import json
from datetime import date
from collections import Counter

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from university_system.models import Student, Instructor
from university_system.courses import Department, Course
from university_system.university import UniversitySystem
from university_system.config import APP_NAME, GPA_SCALE, CURRENCY_SYMBOL, DEFAULT_DATA_FILE
from utils.helpers import format_currency, gpa_label

BG        = "#f5f5f5"
PANEL     = "#ffffff"
ACCENT    = "#1a73e8"
ACCENT2   = "#188038"
FG        = "#202124"
FG2       = "#5f6368"
BTN_FG    = "#ffffff"
ENTRY_BG  = "#ffffff"
ENTRY_BD  = "#b0b8c1"
HEADER_BG = "#1a73e8"

FONT_HEAD = ("Segoe UI", 16, "bold")
FONT_LBL  = ("Segoe UI", 10)
FONT_BTN  = ("Segoe UI", 10, "bold")


def _lbl_entry(parent, label, row, width=24):
    tk.Label(parent, text=label, bg=PANEL, fg=FG2, font=FONT_LBL,
             anchor="w").grid(row=row, column=0, sticky="w", padx=8, pady=4)
    var = tk.StringVar()
    tk.Entry(parent, textvariable=var, bg=ENTRY_BG, fg=FG,
             insertbackground=FG, relief="flat", width=width,
             font=FONT_LBL,
             highlightthickness=1, highlightbackground=ENTRY_BD,
             highlightcolor=ACCENT).grid(row=row, column=1, padx=8, pady=4)
    return var


class UniversityApp(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title(APP_NAME)
        self.geometry("1150x700")
        self.configure(bg=BG)
        self.resizable(True, True)

        self.system = UniversitySystem()
        self._seed_data()

        self._build_sidebar()
        self._build_main_area()

        self.show_tab("students")

    def _seed_data(self):
        self.system.initialize_storage()

    def _build_sidebar(self):
        sb = tk.Frame(self, bg=PANEL, width=200,
                      highlightthickness=1, highlightbackground=ENTRY_BD)
        sb.pack(side="left", fill="y")
        sb.pack_propagate(False)

        brand = tk.Frame(sb, bg=ACCENT, height=56)
        brand.pack(fill="x")
        brand.pack_propagate(False)
        tk.Label(brand, text="UniSys ERP", bg=ACCENT, fg=BTN_FG,
                 font=("Segoe UI", 13, "bold")).pack(expand=True)

        nav = [
            ("Students",    "students"),
            ("Instructors", "instructors"),
            ("Courses",     "courses"),
            ("Enrollments", "enrollments"),
            ("Grades",      "grades"),
            ("Charts",      "charts"),
            ("Export",      "export"),
        ]
        self.nav_btns = {}
        for text, key in nav:
            btn = tk.Button(
                sb, text=text, bg=PANEL, fg=FG,
                font=FONT_BTN, relief="flat", anchor="w", padx=20, pady=10,
                cursor="hand2",
                activebackground="#e8f0fe", activeforeground=ACCENT,
                command=lambda k=key: self.show_tab(k)
            )
            btn.pack(fill="x")
            self.nav_btns[key] = btn

    def _build_main_area(self):
        self.main = tk.Frame(self, bg=BG)
        self.main.pack(side="left", fill="both", expand=True)

        self.tabs = {}
        self.tabs["students"]    = self._tab_students()
        self.tabs["instructors"] = self._tab_instructors()
        self.tabs["courses"]     = self._tab_courses()
        self.tabs["enrollments"] = self._tab_enrollments()
        self.tabs["grades"]      = self._tab_grades()
        self.tabs["charts"]      = self._tab_charts()
        self.tabs["export"]      = self._tab_export()

    def show_tab(self, key):
        for frame in self.tabs.values():
            frame.pack_forget()
        self.tabs[key].pack(fill="both", expand=True)
        refresh = getattr(self, f"_refresh_{key}", None)
        if refresh:
            refresh()

    def _refresh_all(self):
        self._refresh_students()
        self._refresh_instructors()
        self._refresh_courses()
        self._refresh_enrollments()
        self._refresh_grades()

    def _make_table(self, parent, columns):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Custom.Treeview",
                         background=PANEL, fieldbackground=PANEL,
                         foreground=FG, rowheight=26,
                         font=FONT_LBL)
        style.configure("Custom.Treeview.Heading",
                         background=HEADER_BG, foreground=BTN_FG,
                         font=("Segoe UI", 10, "bold"))
        style.map("Custom.Treeview", background=[("selected", ACCENT)])

        frame = tk.Frame(parent, bg=BG)
        frame.pack(fill="both", expand=True, padx=10, pady=6)

        tree = ttk.Treeview(frame, columns=columns, show="headings",
                            style="Custom.Treeview")
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=130)

        sb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=sb.set)
        tree.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")
        return tree

    def _section_header(self, parent, title):
        tk.Label(parent, text=title, bg=BG, fg=FG,
                 font=FONT_HEAD, anchor="w").pack(fill="x", padx=16, pady=(16, 4))
        ttk.Separator(parent, orient="horizontal").pack(fill="x", padx=16, pady=2)

    def _tab_students(self):
        frame = tk.Frame(self.main, bg=BG)
        self._section_header(frame, "Students Management")

        form = tk.LabelFrame(frame, text=" Add New Student ", bg=PANEL,
                             fg=ACCENT, font=FONT_LBL)
        form.pack(fill="x", padx=16, pady=6)

        self.s_name  = _lbl_entry(form, "Full Name",  0)
        self.s_age   = _lbl_entry(form, "Age (16-30)", 1)
        self.s_email = _lbl_entry(form, "Email",      2)
        self.s_level = _lbl_entry(form, "Level",      3)

        tk.Button(form, text="Add Student", bg=ACCENT, fg=BTN_FG,
                  font=FONT_BTN, relief="flat", cursor="hand2",
                  command=self._add_student
                  ).grid(row=4, column=0, columnspan=2, pady=8)

        cols = ("ID", "Name", "Age", "Email", "Level", "GPA")
        self.student_tree = self._make_table(frame, cols)
        return frame

    def _add_student(self):
        try:
            age = int(self.s_age.get())
            s = Student(self.s_name.get(), age,
                        self.s_email.get(), self.s_level.get())
            if self.system.add_student(s):
                self.system.save_to_json()
                messagebox.showinfo("Success", f"Student '{s.get_name()}' added with ID: {s.get_id()}!")
                for v in (self.s_name, self.s_age, self.s_email, self.s_level):
                    v.set("")
                self._refresh_students()
            else:
                messagebox.showwarning("Duplicate", "Student already exists.")
        except ValueError as e:
            messagebox.showerror("Validation Error", str(e))

    def _refresh_students(self):
        self.student_tree.delete(*self.student_tree.get_children())
        for s in self.system.students:
            self.system.calculate_student_average(s.get_id())
            self.student_tree.insert("", "end", values=(
                s.get_id(), s.get_name(), s.get_age(),
                s.get_email(), s._level, f"{s.get_gpa():.2f}"
            ))

    def _tab_instructors(self):
        frame = tk.Frame(self.main, bg=BG)
        self._section_header(frame, "Instructors Management")

        form = tk.LabelFrame(frame, text=" Add New Instructor ", bg=PANEL,
                             fg=ACCENT, font=FONT_LBL)
        form.pack(fill="x", padx=16, pady=6)

        self.i_name   = _lbl_entry(form, "Full Name",            0)
        self.i_age    = _lbl_entry(form, "Age (22-80)",          1)
        self.i_email  = _lbl_entry(form, "Email",                2)
        self.i_spec   = _lbl_entry(form, "Specialization",       3)
        self.i_salary = _lbl_entry(form, f"Salary ({CURRENCY_SYMBOL})", 4)

        tk.Button(form, text="Add Instructor", bg=ACCENT, fg=BTN_FG,
                  font=FONT_BTN, relief="flat", cursor="hand2",
                  command=self._add_instructor
                  ).grid(row=5, column=0, columnspan=2, pady=8)

        cols = ("ID", "Name", "Age", "Email", "Specialization", f"Salary ({CURRENCY_SYMBOL})", "Courses")
        self.instructor_tree = self._make_table(frame, cols)
        return frame

    def _add_instructor(self):
        try:
            age    = int(self.i_age.get())
            salary = float(self.i_salary.get())
            inst = Instructor(self.i_name.get(), age, self.i_email.get(),
                              self.i_spec.get(), salary)
            if self.system.add_instructor(inst):
                self.system.save_to_json()
                messagebox.showinfo("Success", f"Instructor '{inst.get_name()}' added with ID: {inst.get_id()}!")
                for v in (self.i_name, self.i_age, self.i_email,
                          self.i_spec, self.i_salary):
                    v.set("")
                self._refresh_instructors()
            else:
                messagebox.showwarning("Duplicate", "Instructor already exists.")
        except ValueError as e:
            messagebox.showerror("Validation Error", str(e))

    def _refresh_instructors(self):
        self.instructor_tree.delete(*self.instructor_tree.get_children())
        for i in self.system.instructors:
            self.instructor_tree.insert("", "end", values=(
                i.get_id(), i.get_name(), i.get_age(),
                i.get_email(), i._specialization,
                format_currency(i.get_salary()), len(i.assigned_courses)
            ))

    def _tab_courses(self):
        frame = tk.Frame(self.main, bg=BG)
        self._section_header(frame, "Courses & Departments")

        form = tk.LabelFrame(frame, text=" Add New Course ", bg=PANEL,
                             fg=ACCENT, font=FONT_LBL)
        form.pack(fill="x", padx=16, pady=6)

        self.c_code    = _lbl_entry(form, "Course Code", 0)
        self.c_title   = _lbl_entry(form, "Title",       1)
        self.c_credits = _lbl_entry(form, "Credits (1-6)", 2)
        self.c_dept    = _lbl_entry(form, "Department",  3)

        tk.Button(form, text="Add Course", bg=ACCENT, fg=BTN_FG,
                  font=FONT_BTN, relief="flat", cursor="hand2",
                  command=self._add_course
                  ).grid(row=4, column=0, columnspan=2, pady=8)

        cols = ("Code", "Title", "Credits", "Department", "Instructor", "Students")
        self.course_tree = self._make_table(frame, cols)
        return frame

    def _add_course(self):
        try:
            credits = int(self.c_credits.get())
            dept_name = self.c_dept.get().strip()
            dept = self.system.search_department(dept_name) if dept_name else None
            c = Course(self.c_code.get(), self.c_title.get(), credits, department=dept)
            if self.system.add_course(c):
                self.system.save_to_json()
                messagebox.showinfo("Success", f"Course '{c.course_code}' added successfully!")
                for v in (self.c_code, self.c_title, self.c_credits, self.c_dept):
                    v.set("")
                self._refresh_courses()
            else:
                messagebox.showwarning("Duplicate", "Course code already exists.")
        except ValueError as e:
            messagebox.showerror("Validation Error", str(e))

    def _refresh_courses(self):
        self.course_tree.delete(*self.course_tree.get_children())
        for c in self.system.courses:
            dept = c.department.name if c.department else "General"
            ins = c.instructor.get_name() if c.instructor else "Unassigned"
            self.course_tree.insert("", "end", values=(
                c.course_code, c.title, c.credit_hours,
                dept, ins, len(c.students)
            ))

    def _tab_enrollments(self):
        frame = tk.Frame(self.main, bg=BG)
        self._section_header(frame, "Student Enrollment")

        form = tk.LabelFrame(frame, text=" Enroll Student in Course ", bg=PANEL,
                             fg=ACCENT, font=FONT_LBL)
        form.pack(fill="x", padx=16, pady=6)

        self.e_sid = _lbl_entry(form, "Student ID or Name", 0)
        self.e_cid = _lbl_entry(form, "Course Code",        1)

        tk.Button(form, text="Enroll Student", bg=ACCENT, fg=BTN_FG,
                  font=FONT_BTN, relief="flat", cursor="hand2",
                  command=self._enroll
                  ).grid(row=2, column=0, columnspan=2, pady=8)

        cols = ("Enrollment ID", "Student Name", "Course Code", "Course Title", "Date")
        self.enroll_tree = self._make_table(frame, cols)
        return frame

    def _enroll(self):
        sid = self.e_sid.get().strip()
        cid = self.e_cid.get().strip()
        s = self.system.search_student(sid)
        c = self.system.search_course(cid)
        if not s:
            messagebox.showerror("Error", f"Student '{sid}' not found.")
            return
        if not c:
            messagebox.showerror("Error", f"Course '{cid}' not found.")
            return
        if self.system.enroll_student_in_course(s.get_id(), c.course_code):
            self.system.save_to_json()
            messagebox.showinfo("Success", f"{s.get_name()} enrolled in {c.course_code}!")
            self.e_sid.set("")
            self.e_cid.set("")
            self._refresh_enrollments()
        else:
            messagebox.showwarning("Failed", "Student may already be enrolled in this course.")

    def _refresh_enrollments(self):
        self.enroll_tree.delete(*self.enroll_tree.get_children())
        for e in self.system.enrollments:
            self.enroll_tree.insert("", "end", values=(
                e.get_id(), e.student.get_name(),
                e.course.course_code, e.course.title,
                str(e.enrollment_date)
            ))

    def _tab_grades(self):
        frame = tk.Frame(self.main, bg=BG)
        self._section_header(frame, "Record Grades")

        form = tk.LabelFrame(frame, text=" Record Grade ", bg=PANEL,
                             fg=ACCENT, font=FONT_LBL)
        form.pack(fill="x", padx=16, pady=6)

        self.g_sid  = _lbl_entry(form, "Student ID or Name", 0)
        self.g_cid  = _lbl_entry(form, "Course Code",        1)
        self.g_mid  = _lbl_entry(form, "Midterm (0-100)",    2)
        self.g_fin  = _lbl_entry(form, "Final (0-100)",      3)
        self.g_asgn = _lbl_entry(form, "Assignments (0-100)", 4)

        tk.Button(form, text="Save Grade", bg=ACCENT2, fg=BTN_FG,
                  font=FONT_BTN, relief="flat", cursor="hand2",
                  command=self._save_grade
                  ).grid(row=5, column=0, columnspan=2, pady=8)

        cols = ("Student ID", "Student Name", "Course", "Midterm", "Final", "Assignments", "Total", "Letter")
        self.grade_tree = self._make_table(frame, cols)
        return frame

    def _save_grade(self):
        sid = self.g_sid.get().strip()
        cid = self.g_cid.get().strip()
        s = self.system.search_student(sid)
        c = self.system.search_course(cid)
        if not s or not c:
            messagebox.showerror("Error", "Student or Course not found.")
            return

        try:
            mid  = float(self.g_mid.get())
            fin  = float(self.g_fin.get())
            asgn = float(self.g_asgn.get())
            if self.system.record_grade(s.get_id(), c.course_code, mid, fin, asgn):
                self.system.calculate_student_average(s.get_id())
                self.system.save_to_json()
                messagebox.showinfo("Success", f"Grade recorded for {s.get_name()} in {c.course_code}!")
                for v in (self.g_sid, self.g_cid, self.g_mid, self.g_fin, self.g_asgn):
                    v.set("")
                self._refresh_grades()
            else:
                messagebox.showwarning("Not Enrolled", f"{s.get_name()} is not enrolled in {c.course_code}.")
        except ValueError as e:
            messagebox.showerror("Validation Error", str(e))

    def _refresh_grades(self):
        self.grade_tree.delete(*self.grade_tree.get_children())
        for e in self.system.enrollments:
            if e.has_grade():
                g = e.get_grade()
                self.grade_tree.insert("", "end", values=(
                    e.student.get_id(), e.student.get_name(),
                    e.course.course_code,
                    f"{g.get_midterm():.1f}", f"{g.get_final():.1f}",
                    f"{g.get_assignments():.1f}",
                    f"{g.get_total_grade():.2f}%", g.get_letter_grade()
                ))

    def _tab_charts(self):
        frame = tk.Frame(self.main, bg=BG)
        self._section_header(frame, "Analytics & Visualizations")

        ctrl = tk.Frame(frame, bg=BG)
        ctrl.pack(fill="x", padx=16, pady=6)

        charts = [
            ("Student GPAs", self._chart_gpas),
            ("Course Grades", self._chart_course_averages),
            ("Letter Grades", self._chart_letter_distribution),
        ]
        for text, cmd in charts:
            tk.Button(ctrl, text=text, bg=ACCENT, fg=BTN_FG,
                      font=FONT_BTN, relief="flat", cursor="hand2",
                      command=cmd).pack(side="left", padx=4)

        self.chart_area = tk.Frame(frame, bg=PANEL,
                                   highlightthickness=1, highlightbackground=ENTRY_BD)
        self.chart_area.pack(fill="both", expand=True, padx=16, pady=10)
        return frame

    def _embed_fig(self, fig):
        for widget in self.chart_area.winfo_children():
            widget.destroy()
        canvas = FigureCanvasTkAgg(fig, master=self.chart_area)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def _chart_gpas(self):
        if not self.system.students:
            messagebox.showinfo("No Data", "No students registered.")
            return
        names = [s.get_name() for s in self.system.students]
        gpas  = [s.get_gpa() for s in self.system.students]

        fig, ax = plt.subplots(figsize=(7, 4))
        ax.bar(names, gpas, color="#1a73e8", width=0.5)
        ax.set_ylabel(f"GPA (out of {GPA_SCALE})")
        ax.set_title("Student Cumulative GPA")
        ax.set_ylim(0, GPA_SCALE + 0.5)
        fig.tight_layout()
        self._embed_fig(fig)

    def _chart_course_averages(self):
        if not self.system.courses:
            messagebox.showinfo("No Data", "No courses registered.")
            return
        titles = []
        averages = []
        for c in self.system.courses:
            grades = [
                e.get_grade().get_total_grade()
                for e in self.system.enrollments
                if e.course.course_code == c.course_code and e.has_grade()
            ]
            if grades:
                titles.append(c.course_code)
                averages.append(sum(grades) / len(grades))

        if not averages:
            messagebox.showinfo("No Data", "No graded courses found.")
            return

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(titles, averages, color="#188038", width=0.4)
        ax.set_ylabel("Average Score (%)")
        ax.set_title("Course Performance Averages")
        ax.set_ylim(0, 105)
        fig.tight_layout()
        self._embed_fig(fig)

    def _chart_letter_distribution(self):
        letters = [
            e.get_grade().get_letter_grade()
            for e in self.system.enrollments
            if e.has_grade()
        ]
        if not letters:
            messagebox.showinfo("No Data", "No graded enrollments found.")
            return

        counts = Counter(letters)
        order = ["A", "B", "C", "D", "F"]
        vals  = [counts.get(l, 0) for l in order]

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(order, vals, color=["#188038", "#1a73e8", "#f59e0b", "#fb8c00", "#e53935"])
        ax.set_ylabel("Number of Students")
        ax.set_title("Letter Grade Distribution")
        ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
        fig.tight_layout()
        self._embed_fig(fig)

    def _tab_export(self):
        frame = tk.Frame(self.main, bg=BG)
        self._section_header(frame, "Export Data")

        tk.Label(frame,
                 text="Export university records and grade reports to CSV format.",
                 bg=BG, fg=FG2, font=FONT_LBL, wraplength=640, justify="left"
                 ).pack(anchor="w", padx=16, pady=(6, 2))

        # CSV Export section
        csv_frame = tk.LabelFrame(frame, text=" CSV Export ", bg=BG, fg=ACCENT2, font=FONT_LBL)
        csv_frame.pack(fill="x", padx=16, pady=6)

        csv_btns = [
            ("Students CSV",    self._csv_students),
            ("Instructors CSV", self._csv_instructors),
            ("Courses CSV",     self._csv_courses),
            ("Grades CSV",      self._csv_grades),
            ("Export All CSVs", self._csv_all),
        ]
        for i, (label, cmd) in enumerate(csv_btns):
            tk.Button(csv_frame, text=label, bg=ACCENT2, fg=BTN_FG,
                      font=FONT_BTN, relief="flat", cursor="hand2",
                      width=18, command=cmd
                      ).grid(row=0, column=i, padx=6, pady=8)

        self.export_log = tk.Text(
            frame, height=12, bg=PANEL, fg=ACCENT2,
            font=("Consolas", 10), relief="flat", state="disabled",
            highlightthickness=1, highlightbackground=ENTRY_BD
        )
        self.export_log.pack(fill="both", expand=True, padx=16, pady=10)
        return frame

    def _log(self, msg):
        self.export_log.configure(state="normal")
        self.export_log.insert("end", msg + "\n")
        self.export_log.see("end")
        self.export_log.configure(state="disabled")

    # CSV Handlers
    def _write_csv(self, path, headers, rows):
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(rows)
        self._log(f"[+] CSV saved -> {path}")
        messagebox.showinfo("Exported", f"Saved to {path}")

    def _csv_students(self):
        rows = []
        for s in self.system.students:
            self.system.calculate_student_average(s.get_id())
            rows.append([s.get_id(), s.get_name(), s.get_age(),
                         s.get_email(), s._level, round(s.get_gpa(), 2)])
        self._write_csv("students_export.csv",
                        ["ID", "Name", "Age", "Email", "Level", "GPA"], rows)

    def _csv_instructors(self):
        rows = [[i.get_id(), i.get_name(), i.get_age(), i.get_email(),
                 i._specialization, f"{CURRENCY_SYMBOL}{i.get_salary():,.0f}", len(i.assigned_courses)]
                for i in self.system.instructors]
        self._write_csv("instructors_export.csv",
                        ["ID", "Name", "Age", "Email", "Specialization",
                         f"Salary ({CURRENCY_SYMBOL})", "Courses Assigned"], rows)

    def _csv_courses(self):
        rows = []
        for c in self.system.courses:
            dept  = c.department.name if c.department else "General"
            instr = c.instructor.get_name() if c.instructor else "Not Assigned"
            rows.append([c.course_code, c.title, c.credit_hours,
                         dept, instr, len(c.students)])
        self._write_csv("courses_export.csv",
                        ["Code", "Title", "Credits", "Department",
                         "Instructor", "Students Enrolled"], rows)

    def _csv_grades(self):
        rows = []
        for e in self.system.enrollments:
            if e.has_grade():
                g = e.get_grade()
                self.system.calculate_student_average(e.student.get_id())
                rows.append([e.student.get_id(), e.student.get_name(),
                            e.course.course_code, e.course.title,
                            g.get_midterm(), g.get_final(), g.get_assignments(),
                            g.get_total_grade(), g.get_letter_grade(),
                            round(e.student.get_gpa(), 2)])
        self._write_csv("grades_export.csv",
                        ["Student ID", "Student Name", "Course Code", "Course Title",
                         "Midterm", "Final", "Assignments", "Total",
                         "Letter Grade", "GPA"], rows)

    def _csv_all(self):
        self._csv_students()
        self._csv_instructors()
        self._csv_courses()
        self._csv_grades()
        self._log("[+] All CSV files exported successfully.")


if __name__ == "__main__":
    app = UniversityApp()
    app.mainloop()
