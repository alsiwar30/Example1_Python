

class Student:


    def __init__(self, student_id, average):
        self.student_courses = list()
        self.student_id = student_id
        self.average = average
        self.students = list()


    def get_average(self):
        return self.average

    def add_new_student(self, student):
        self.students.append(student)

    def register_course(self, course_id):
        self.student_courses.append(course_id)

    def add_course(self,course):
        self.student_courses.append(course)

    def delete_course(self, course_id):
        self.student_courses.remove(course_id)

    def set_mark(self,course_id , mark):

        self.student_courses[course_id] = mark

    def set_average(self):
        pass

    def get_students(self):
        return self.students

    def get_student_id(self):
        return self.student_id

    def get_student_course(self):
        return self.student_courses

    def delete_student(self, student_id):

        for i in self.students:
            if i.student_id == student_id:
                self.students.remove(student_id)


    def show_average(self, student_id):
        for i in self.students:
            if i.student_id == student_id:
                return i.average


    def show_ranks(self):
        self.students.sort(key= lambda x : x.average)
        for i in self.students:
            print(i)

    def show_ranks(self,course_id):

        self.students.sort(key=lambda x: x.average)

        for i in self.students:
            print(i)
