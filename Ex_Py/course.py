

class Course:


    def __init__(self,course_id, unit):
        self.course_id = course_id
        self.unit = unit
        self.capacity=0
        self.numberOfRegisteredStudent=0
        self.score=0
        self.courses = list()


    def add_new_course(self,course):
        self.courses.append(course)

    def get_courses(self):
        return self.courses

    def get_number_of_numberOfRegisteredStudent(self):
        return self.numberOfRegisteredStudent

    def increament_numberOfRegisteredStudent(self):
        self.numberOfRegisteredStudent += 1

    def decrement_numberOfRegisteredStudent(self):
        self.numberOfRegisteredStudent -= 1

    def get_course_id(self):
        return self.course_id

    def add_capacity(self,number):
        self.capacity += number

    def get_score(self):
        return self.score

    def get_unit(self):
        return self.unit

    def get_score(self,score):
        self.score = score

    def get_capacity(self):
        return self.capacity

    def show_course(self,course_id,string):
        print(course_id + " " + string)