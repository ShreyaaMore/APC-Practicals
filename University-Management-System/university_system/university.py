import sys
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

import os
import json

try:
    from .enrollment import Enrollment, Grade
    from .models import Person, Student, Instructor
    from .courses import Department, Course
    from .config import GPA_SCALE, CURRENCY_SYMBOL, DEFAULT_DATA_FILE
except ImportError:
    from enrollment import Enrollment, Grade
    from models import Person, Student, Instructor
    from courses import Department, Course
    from config import GPA_SCALE, CURRENCY_SYMBOL, DEFAULT_DATA_FILE

try:
    from utils.helpers import percentage_to_gpa
except ImportError:
    try:
        from ..utils.helpers import percentage_to_gpa
    except ImportError:
        def percentage_to_gpa(percentage):
            return round((percentage / 100.0) * GPA_SCALE, 2)


class UniversitySystem:

    def __init__(self, name="National University Management System", auto_save=True, data_file=DEFAULT_DATA_FILE):
        self.name = name
        self.students = []
        self.instructors = []
        self.courses = []
        self.departments = []
        self.enrollments = []
        self.auto_save = auto_save
        self.data_file = data_file

    def _trigger_save(self):
        if self.auto_save:
            self.save_to_json(self.data_file)

    def initialize_storage(self):
        if not self.load_from_json(self.data_file):
            self.load_sample_data()
            self._trigger_save()

    def add_student(self, student):
        if student is None or self.search_student(student.get_id()):
            return False
        self.students.append(student)
        self._trigger_save()
        return True

    def add_instructor(self, instructor):
        if instructor is None or self.search_instructor(instructor.get_id()):
            return False
        self.instructors.append(instructor)
        self._trigger_save()
        return True

    def add_course(self, course):
        if course is None or self.search_course(course.course_code):
            return False
        self.courses.append(course)
        self._trigger_save()
        return True

    def add_department(self, department):
        if department is None:
            return False
        for dept in self.departments:
            if dept.department_id == department.department_id or dept.name.lower() == department.name.lower():
                return False
        self.departments.append(department)
        self._trigger_save()
        return True

    def search_student(self, identifier):
        if identifier is None:
            return None
        target = str(identifier).strip().lower()
        for student in self.students:
            if student.get_id().lower() == target or student.get_name().lower() == target:
                return student
        return None

    def search_instructor(self, identifier):
        if identifier is None:
            return None
        target = str(identifier).strip().lower()
        for instructor in self.instructors:
            if instructor.get_id().lower() == target or instructor.get_name().lower() == target:
                return instructor
        return None

    def search_person(self, identifier):
        return self.search_student(identifier) or self.search_instructor(identifier)

    def search_course(self, identifier):
        if identifier is None:
            return None
        target = str(identifier).strip().lower()
        for course in self.courses:
            if course.course_code.lower() == target or course.title.lower() == target:
                return course
        return None

    def search_department(self, identifier):
        if identifier is None:
            return None
        target = str(identifier).strip().lower()
        for dept in self.departments:
            if str(dept.department_id) == target or dept.name.lower() == target:
                return dept
        return None

    def update_student(self, student_id, new_name=None, new_email=None, new_level=None):
        student = self.search_student(student_id)
        if student is None:
            return False
        if new_name:
            student.set_name(new_name)
        if new_email:
            student.set_email(new_email)
        if new_level:
            student._level = new_level
        self._trigger_save()
        return True

    def enroll_student_in_course(self, student_id, course_code):
        student = self.search_student(student_id)
        course = self.search_course(course_code)
        if student is None or course is None:
            return False
        for enrollment in self.enrollments:
            if (enrollment.student.get_id() == student.get_id()
                    and enrollment.course.course_code == course.course_code):
                return False
        self.enrollments.append(Enrollment(student, course))
        self._trigger_save()
        return True

    def remove_student_from_course(self, student_id, course_code):
        student = self.search_student(student_id)
        course = self.search_course(course_code)
        if student is None or course is None:
            return False
        for enrollment in self.enrollments:
            if (enrollment.student.get_id() == student.get_id()
                    and enrollment.course.course_code == course.course_code):
                self.enrollments.remove(enrollment)
                course.remove_student(student.get_id())
                self._trigger_save()
                return True
        return False

    def remove_course(self, course_code):
        course = self.search_course(course_code)
        if course is None:
            return False
        self.courses.remove(course)
        if course.department and course in course.department.courses:
            course.department.courses.remove(course)
        if course.instructor and course in course.instructor.assigned_courses:
            course.instructor.assigned_courses.remove(course)
        self.enrollments = [e for e in self.enrollments if e.course.course_code != course.course_code]
        self._trigger_save()
        return True

    def assign_instructor_to_course(self, instructor_id, course_code):
        instructor = self.search_instructor(instructor_id)
        course = self.search_course(course_code)
        if instructor is None or course is None:
            return False
        res = course.assign_instructor(instructor)
        if res:
            self._trigger_save()
        return res

    def record_grade(self, student_id, course_code, midterm, final, assignments):
        student = self.search_student(student_id)
        course = self.search_course(course_code)
        if student is None or course is None:
            return False
        for enrollment in self.enrollments:
            if (enrollment.student.get_id() == student.get_id()
                    and enrollment.course.course_code == course.course_code):
                enrollment.assign_grade(Grade(midterm, final, assignments))
                self.calculate_student_average(student.get_id())
                self._trigger_save()
                return True
        return False

    def calculate_student_average(self, student_id):
        student = self.search_student(student_id)
        if student is None:
            return 0.0
        total_points = 0.0
        total_hours = 0
        for enrollment in self.enrollments:
            if enrollment.student.get_id() == student.get_id() and enrollment.has_grade():
                total_points += enrollment.get_grade().get_total_grade() * enrollment.course.credit_hours
                total_hours += enrollment.course.credit_hours
        if total_hours == 0:
            return 0.0
        percentage_avg = total_points / total_hours
        student.set_gpa(percentage_to_gpa(percentage_avg))
        return percentage_avg

    def display_student_courses(self, student_id):
        student = self.search_student(student_id)
        if student is None:
            print("Student not found.")
            return
        print(f"\nCourses for {student.get_name()}:")
        found = False
        for enrollment in self.enrollments:
            if enrollment.student.get_id() == student.get_id():
                found = True
                if enrollment.has_grade():
                    g = enrollment.get_grade()
                    print(f"  - {enrollment.course.course_code} - {enrollment.course.title}: {g.get_total_grade()}% ({g.get_letter_grade()})")
                else:
                    print(f"  - {enrollment.course.course_code} - {enrollment.course.title}: No grade yet")
        if not found:
            print("  (No enrolled courses)")

    def display_course_students(self, course_code):
        course = self.search_course(course_code)
        if course is None:
            print("Course not found.")
            return
        print(f"\nStudents in {course.course_code} - {course.title}:")
        if not course.students:
            print("  (No students currently enrolled)")
        for student in course.students:
            print(f"  - {student.get_name()} ({student.get_id()})")

    def display_department_info(self, department_name):
        dept = self.search_department(department_name)
        if dept:
            print(dept.display_info())
            return
        print("Department not found.")

    def display_all_students(self):
        if not self.students:
            print("\n[!] No students registered in the system.")
            return
        print("\n" + "=" * 76)
        print("                          ALL REGISTERED STUDENTS")
        print("=" * 76)
        print(f"{'ID':<10} | {'Name':<22} | {'Age':<5} | {'Level':<12} | {'GPA':<6}")
        print("-" * 76)
        for s in self.students:
            print(f"{s.get_id():<10} | {s.get_name():<22} | {s.get_age():<5} | {s._level:<12} | {s.get_gpa():<6.2f}")
        print("=" * 76)

    def display_all_instructors(self):
        if not self.instructors:
            print("\n[!] No instructors registered in the system.")
            return
        print("\n" + "=" * 82)
        print("                         ALL REGISTERED INSTRUCTORS")
        print("=" * 82)
        print(f"{'ID':<10} | {'Name':<22} | {'Specialization':<22} | {'Salary':<12} | {'Courses':<8}")
        print("-" * 82)
        for ins in self.instructors:
            salary_str = f"{CURRENCY_SYMBOL}{ins.get_salary():,.0f}"
            print(f"{ins.get_id():<10} | {ins.get_name():<22} | {ins._specialization:<22} | {salary_str:<12} | {len(ins.assigned_courses):<8}")
        print("=" * 82)

    def display_all_courses(self):
        if not self.courses:
            print("\n[!] No courses registered in the system.")
            return
        print("\n" + "=" * 90)
        print("                           ALL REGISTERED COURSES")
        print("=" * 90)
        print(f"{'Code':<10} | {'Title':<30} | {'Credits':<8} | {'Department':<20} | {'Instructor':<15}")
        print("-" * 90)
        for c in self.courses:
            dept_name = c.department.name if c.department else "General"
            ins_name = c.instructor.get_name() if c.instructor else "Unassigned"
            print(f"{c.course_code:<10} | {c.title:<30} | {c.credit_hours:<8} | {dept_name[:18]:<20} | {ins_name:<15}")
        print("=" * 90)

    def display_all_departments(self):
        if not self.departments:
            print("\n[!] No departments registered in the system.")
            return
        print("\n" + "=" * 65)
        print("                     ALL REGISTERED DEPARTMENTS")
        print("=" * 65)
        print(f"{'Dept ID':<10} | {'Name':<28} | {'Courses':<10} | {'Instructors':<12}")
        print("-" * 65)
        for d in self.departments:
            print(f"{d.department_id:<10} | {d.name:<28} | {len(d.courses):<10} | {len(d.instructors):<12}")
        print("=" * 65)

    def display_all_enrollments(self):
        if not self.enrollments:
            print("\n[!] No enrollments registered in the system.")
            return
        print("\n" + "=" * 88)
        print("                         ALL ENROLLMENTS & GRADES")
        print("=" * 88)
        print(f"{'Enroll ID':<10} | {'Student':<20} | {'Course':<24} | {'Grade (Total)':<15} | {'Letter':<8}")
        print("-" * 88)
        for e in self.enrollments:
            grade_info = f"{e.get_grade().get_total_grade()}%" if e.has_grade() else "Not Graded"
            letter_info = e.get_grade().get_letter_grade() if e.has_grade() else "N/A"
            course_title = e.course.title if len(e.course.title) <= 22 else e.course.title[:20] + ".."
            print(f"{e.get_id():<10} | {e.student.get_name():<20} | {course_title:<24} | {grade_info:<15} | {letter_info:<8}")
        print("=" * 88)


    def to_dict(self):
        return {
            "university_name": self.name,
            "departments": [
                {
                    "department_id": d.department_id,
                    "name": d.name
                }
                for d in self.departments
            ],
            "instructors": [
                {
                    "id": ins.get_id(),
                    "name": ins.get_name(),
                    "age": ins.get_age(),
                    "email": ins.get_email(),
                    "specialization": ins._specialization,
                    "salary": ins.get_salary(),
                    "assigned_courses": [c.course_code for c in ins.assigned_courses]
                }
                for ins in self.instructors
            ],
            "courses": [
                {
                    "course_code": c.course_code,
                    "title": c.title,
                    "credit_hours": c.credit_hours,
                    "department_id": c.department.department_id if c.department else None,
                    "instructor_id": c.instructor.get_id() if c.instructor else None
                }
                for c in self.courses
            ],
            "students": [
                {
                    "id": s.get_id(),
                    "name": s.get_name(),
                    "age": s.get_age(),
                    "email": s.get_email(),
                    "level": s._level,
                    "gpa": s.get_gpa()
                }
                for s in self.students
            ],
            "enrollments": [
                {
                    "enrollment_id": e.get_id(),
                    "student_id": e.student.get_id(),
                    "course_code": e.course.course_code,
                    "enrollment_date": str(e.enrollment_date),
                    "grade": {
                        "midterm": e.get_grade().get_midterm(),
                        "final": e.get_grade().get_final(),
                        "assignments": e.get_grade().get_assignments(),
                        "total": e.get_grade().get_total_grade(),
                        "letter": e.get_grade().get_letter_grade()
                    } if e.has_grade() else None
                }
                for e in self.enrollments
            ]
        }

    def save_to_json(self, filepath=None):
        if filepath is None:
            filepath = DEFAULT_DATA_FILE

        folder = os.path.dirname(os.path.abspath(filepath))
        if folder and not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)

        data = self.to_dict()
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return True

    def load_from_json(self, filepath=None):
        if filepath is None:
            filepath = DEFAULT_DATA_FILE

        if not os.path.exists(filepath):
            return False

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        return self.from_dict(data)

    def from_dict(self, data):
        prev_auto = self.auto_save
        self.auto_save = False
        try:
            return self._from_dict_internal(data)
        finally:
            self.auto_save = prev_auto

    def _from_dict_internal(self, data):
        self.departments.clear()
        self.instructors.clear()
        self.courses.clear()
        self.students.clear()
        self.enrollments.clear()

        self.name = data.get("university_name", self.name)

        max_person_num = 0
        max_enroll_num = 0

        for d_data in data.get("departments", []):
            dept = Department(d_data["department_id"], d_data["name"])
            self.add_department(dept)

        for i_data in data.get("instructors", []):
            ins = Instructor(
                i_data["name"],
                i_data["age"],
                i_data["email"],
                i_data["specialization"],
                i_data["salary"]
            )
            custom_id = i_data.get("id")
            if custom_id:
                ins._id = custom_id
            if ins._id.startswith("P-"):
                try:
                    num = int(ins._id.split("-")[1])
                    if num > max_person_num:
                        max_person_num = num
                except ValueError:
                    pass
            self.instructors.append(ins)

        for c_data in data.get("courses", []):
            dept = self.search_department(c_data.get("department_id"))
            course = Course(
                c_data["course_code"],
                c_data["title"],
                c_data["credit_hours"],
                department=dept
            )
            ins_id = c_data.get("instructor_id")
            if ins_id:
                ins = self.search_instructor(ins_id)
                if ins:
                    course.assign_instructor(ins)
            self.add_course(course)

        for s_data in data.get("students", []):
            s = Student(
                s_data["name"],
                s_data["age"],
                s_data["email"],
                s_data["level"],
                s_data.get("gpa", 0.0)
            )
            custom_id = s_data.get("id")
            if custom_id:
                s._id = custom_id
            if s._id.startswith("P-"):
                try:
                    num = int(s._id.split("-")[1])
                    if num > max_person_num:
                        max_person_num = num
                except ValueError:
                    pass
            self.students.append(s)

        for e_data in data.get("enrollments", []):
            s = self.search_student(e_data["student_id"])
            c = self.search_course(e_data["course_code"])
            if s and c:
                enr = Enrollment(s, c)
                custom_eid = e_data.get("enrollment_id")
                if custom_eid:
                    enr._enrollment_id = custom_eid
                if enr._enrollment_id.startswith("E-"):
                    try:
                        num = int(enr._enrollment_id.split("-")[1])
                        if num > max_enroll_num:
                            max_enroll_num = num
                    except ValueError:
                        pass
                g_data = e_data.get("grade")
                if g_data:
                    g = Grade(g_data["midterm"], g_data["final"], g_data["assignments"])
                    enr.assign_grade(g)
                self.enrollments.append(enr)

        Person._id_counter = max_person_num + 1
        Enrollment._id_counter = max_enroll_num + 1

        for s in self.students:
            self.calculate_student_average(s.get_id())

        return True

    def load_sample_data(self):
        prev_auto = self.auto_save
        self.auto_save = False
        try:
            self.departments.clear()
            self.instructors.clear()
            self.courses.clear()
            self.students.clear()
            self.enrollments.clear()
            Person._id_counter = 1
            Enrollment._id_counter = 1

            # Departments
            cs_dept = Department(1, "Computer Science & Engineering")
            ece_dept = Department(2, "Electronics & Communication")
            self.add_department(cs_dept)
            self.add_department(ece_dept)

            # Courses
            c1 = Course("CS101", "Python & OOP Fundamentals", 4, department=cs_dept)
            c2 = Course("CS102", "Data Structures & Algorithms", 4, department=cs_dept)
            c3 = Course("EC201", "Digital Signal Processing", 3, department=ece_dept)
            self.add_course(c1)
            self.add_course(c2)
            self.add_course(c3)

            # Instructors
            ins1 = Instructor("Dr. Rajesh Sharma", 45, "rajesh.sharma@uni.edu.in", "Software Engineering", 125000)
            ins2 = Instructor("Dr. Sunita Rao", 40, "sunita.rao@uni.edu.in", "Data Science & AI", 115000)
            ins3 = Instructor("Prof. Amit Verma", 36, "amit.verma@uni.edu.in", "Embedded Systems", 95000)
            self.add_instructor(ins1)
            self.add_instructor(ins2)
            self.add_instructor(ins3)

            self.assign_instructor_to_course(ins1.get_id(), "CS101")
            self.assign_instructor_to_course(ins2.get_id(), "CS102")
            self.assign_instructor_to_course(ins3.get_id(), "EC201")

            # Students
            students_info = [
                ("Aarav Patel", 20, "aarav.patel@uni.edu.in", "Junior", [("CS101", 92, 95, 98), ("CS102", 86, 90, 92)]),
                ("Priya Nair", 21, "priya.nair@uni.edu.in", "Senior", [("CS101", 78, 82, 85), ("CS102", 90, 94, 96)]),
                ("Rohan Gupta", 19, "rohan.gupta@uni.edu.in", "Freshman", [("CS101", 85, 88, 90), ("EC201", 80, 84, 88)]),
                ("Ananya Iyer", 20, "ananya.iyer@uni.edu.in", "Sophomore", [("CS102", 92, 96, 94), ("EC201", 88, 90, 92)]),
                ("Aditya Sharma", 21, "aditya.sharma@uni.edu.in", "Senior", [("CS101", 88, 91, 94), ("CS102", 84, 89, 90)]),
                ("Sneha Kulkarni", 20, "sneha.kulkarni@uni.edu.in", "Junior", [("CS102", 91, 93, 95), ("EC201", 87, 89, 91)]),
                ("Vikram Malhotra", 19, "vikram.malhotra@uni.edu.in", "Freshman", [("CS101", 75, 80, 82), ("EC201", 78, 83, 85)]),
                ("Diya Sen", 20, "diya.sen@uni.edu.in", "Sophomore", [("CS101", 89, 92, 95), ("CS102", 85, 88, 91)]),
                ("Rahul Verma", 22, "rahul.verma@uni.edu.in", "Senior", [("CS102", 82, 86, 88), ("EC201", 85, 88, 90)]),
                ("Pooja Reddy", 21, "pooja.reddy@uni.edu.in", "Junior", [("CS101", 94, 96, 98), ("CS102", 90, 93, 95)]),
                ("Siddharth Rao", 19, "siddharth.rao@uni.edu.in", "Freshman", [("CS101", 80, 85, 87), ("EC201", 76, 82, 84)]),
                ("Neha Joshi", 20, "neha.joshi@uni.edu.in", "Sophomore", [("CS101", 86, 89, 92), ("CS102", 88, 91, 94)]),
                ("Arjun Menon", 21, "arjun.menon@uni.edu.in", "Junior", [("CS102", 83, 87, 89), ("EC201", 89, 92, 94)]),
                ("Kavita Deshmukh", 22, "kavita.deshmukh@uni.edu.in", "Senior", [("CS101", 91, 94, 96), ("EC201", 84, 88, 90)]),
                ("Varun Kapoor", 19, "varun.kapoor@uni.edu.in", "Freshman", [("CS101", 77, 81, 84), ("CS102", 79, 83, 86)]),
                ("Meera Pillai", 20, "meera.pillai@uni.edu.in", "Sophomore", [("CS102", 93, 95, 97), ("EC201", 91, 93, 95)]),
                ("Tanmay Chatterjee", 21, "tanmay.chatterjee@uni.edu.in", "Junior", [("CS101", 82, 86, 88), ("CS102", 84, 87, 90)]),
                ("Riya Bansal", 20, "riya.bansal@uni.edu.in", "Sophomore", [("CS101", 88, 90, 93), ("EC201", 86, 89, 91)]),
                ("Harshvardhan Jain", 21, "harsh.jain@uni.edu.in", "Senior", [("CS102", 87, 91, 93), ("EC201", 83, 87, 89)]),
                ("Shreya Ghosh", 19, "shreya.ghosh@uni.edu.in", "Freshman", [("CS101", 90, 93, 95), ("EC201", 88, 91, 94)]),
            ]

            created_students = []
            for name, age, email, level, enrollments in students_info:
                st = Student(name, age, email, level)
                self.add_student(st)
                created_students.append(st)
                for c_code, m, f_score, a in enrollments:
                    self.enroll_student_in_course(st.get_id(), c_code)
                    self.record_grade(st.get_id(), c_code, midterm=m, final=f_score, assignments=a)

            for s in created_students:
                self.calculate_student_average(s.get_id())
        finally:
            self.auto_save = prev_auto
            self._trigger_save()

        return True
