# --- Base class ---
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

# --- Child class ---
class Undergraduate(Student):
    def __init__(self, name, student_id, gpa):
        """Initialize an undergraduate student with GPA."""
        super().__init__(name, student_id)  # reuse Student initialization
        self.gpa = gpa                      # add GPA attribute

    def show_gpa(self):
        """Show the GPA of this undergraduate student."""
        print(f"{self.name}'s GPA: {self.gpa}")

u1 = Undergraduate("Henry", 3001, 3.8)
u1.add_grades([80, 90, 85])
u1.summary()               
u1.show_gpa()              
