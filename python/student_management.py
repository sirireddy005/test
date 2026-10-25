
class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, name, marks):
        self.students.append({
            "id": student_id,
            "name": name,
            "marks": marks
        })

    def get_average(self):
        total = sum(s["marks"] for s in self.students)
        return total / len(self.students)


manager = StudentManager()
print("Average:", manager.get_average())
