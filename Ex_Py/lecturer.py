

class Lecturer:

    def __init__(self, lecturer_id):
        self.lecturers = list()

        self.courses = list()
        self.lecturer_id = lecturer_id

    def get_lecturer(self):
        return self.lecturers

    def add_new_lecturer(self, lecturer):
        self.lecturers.append(lecturer)

    def add_course(self, course_id):
        self.courses.append(course_id)

    def get_course(self):
        return self.courses

    def get_lecturers(self):
        return self.lecturer_id

    def add_capacity(self, course_id, number):

        dict1 = {
            "number": number,
        }

        self.courses[course_id] = dict1

    def set_mark(self,  course_id, mark, student_id):

        dict1 = {
            "mark": mark,
            "students" :  student_id
        }
        self.courses[course_id] = dict1


