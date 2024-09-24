from person import Person

class Student(Person):
    def __init__(self, first_name, last_name, age, lecture_attendance):
        super().__init__(first_name, last_name, age)
        self.lecture_attendance = lecture_attendance

    def get_student_name(self):
        print(f"Student's full name: {self.first_name} {self.last_name}")

    def get_lecture_list(self):
        print(self.lecture_attendance)

    def add_lecture(self, new_lecture):
        self.lecture_attendance.append(new_lecture)

    def remove_lecture(self, undesired_lecture):
        self.lecture_attendance.remove(undesired_lecture)

