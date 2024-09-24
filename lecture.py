class Lecture:
    def __init__(self, name, max_students, duration, professors_list):
        self.name = name
        self.max_students = max_students
        self.duration = duration
        self.professors_list = professors_list

    def get_lecture_info(self):
        print(f"The {self.name} lecture will last {self.duration} minutes")

    def add_professor(self, new_professor):
        self.professors_list.append(new_professor)
