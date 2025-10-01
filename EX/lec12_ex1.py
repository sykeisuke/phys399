class Student:
    # constructor
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grades(self, grades: list):
        """Add a list of grades at once"""
        self.grades.extend(grades) 

    def average(self):
        """Compute the average grade for this student."""
        if not self.grades:  # If the list is empty
            return 0
        return sum(self.grades) / len(self.grades)

    def summary(self):
        """Print a short summary for this student."""
        print(f"{self.name} (ID: {self.student_id}) "
              f"has {len(self.grades)} grades. "
              f"Average: {self.average():.1f}")

class Course:
    def __init__(self, name, code):
        """Initialize course with a name and code."""
        self.name = name
        self.code = code
        self.students: list[Student] = []

    def add_student(self, student: Student):
        """Add a Student object to the course."""
        self.students.append(student)

    def list_students(self):
        """List all students enrolled in the course."""
        print(f"Course: {self.name} ({self.code})")
        print("Enrolled students:")
        for s in self.students:
            print(f" - {s.name} (ID: {s.student_id})")

class Teacher:
    def __init__(self, name):
        """Initialize teacher with a name and an empty course list."""
        self.name = name
        self.courses: list[Courses] = []

    def add_course(self, course: Course):
        """Add a course (string or Course object) to this teacher."""
        self.courses.append(course)

    def list_courses(self):
        """List all courses taught by this teacher."""
        print(f"Teacher: {self.name}")
        print("Courses taught:")
        for c in self.courses:
            print(f"{c.code}: {c.name}")

course1 = Course("Introduction to Scientific Programming", "PHYS399")
course2 = Course("Modern Electronics for physicists", "PHYS476")

teacher = Teacher("Prof. Yoshihara")
teacher.add_course(course1)
teacher.add_course(course2)

teacher.list_courses()
