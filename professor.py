from person import Person

class Professor(Person):
    def __init__(self, first_name, last_name, age, subjects_taught):
        super().__init__(first_name, last_name, age)
        self.subjects_taught = subjects_taught

    def get_professor_name(self):
        print(f"Professor's full name: {self.first_name} {self.last_name}")

    def get_subject_list(self):
        print(self.subjects_taught)

    def add_subject(self, new_subject):
        self.subjects_taught.append(new_subject)

    def remove_subject(self, undesired_subject):
        self.subjects_taught.remove(undesired_subject)