
from student import Student
from lecturer import Lecturer
from course import Course

students_list = list()
lecturer_list = list()
course_list = list()

while(True):

    command = input()

    if command.startswith("addStudent"):
        id = command.split(" ")[1]
        students_list.append(Student(id,0))

    elif command.startswith("addLecturer"):
        line = command.split(" ")
        le = Lecturer(line[0])
        for i in range(2, len(line)):
            le.courses.append(i)

        lecturer_list.append(le)

    elif command.startswith("W"):
        line = command.split(" ")

        for item in students_list:
            if item.student_id == line[2]:
                item.delete_course(line[1])
                break

    elif command.split(" ")[1] == "register" and\
            len(command.split(" ")) == 3:

        line = command.split(" ")

        for item in students_list:
            if item.student_id == line[0]:
                item.add_course(line[2])
                break

    elif command.split(" ")[1] == "register" \
            and len(command.split(" ")) > 3:

        line = command.split(" ")

        for item in students_list:
            if item.student_id == line[0]:

                for i in range(2, len(line)):
                    item.add_course(line[i])

                break

    elif command.startswith("addCourse"):

        line = command.split(" ")

        course_list.append(Course(line[1], line[2]))

    elif command.startswith("showCourse"):
        line = command.split(" ")

        bool_exist = False

        for item in course_list:
            if item.course_id == line[1]:
                bool_exist = True

                if line[2] == "students":
                    pass

                elif line[2] == "lecturer":
                    pass
                    # for i in lecturer_list:


                elif line[2] == "capacity":

                   print(item.capacity)

                elif line[2] == "average":
                    pass
                    # print(item.)

        if not bool_exist:
            print("shoma daneshjoo nistid")

    elif command.startswith("showRanks"):

        for i in students_list:
            print(i.show_ranks())

    elif command.startswith("showAverage"):

        line = command.split(" ")

        for item in students_list:
            if item.student_id == line[1]:
                print(item.average)
                break


    elif command.split(" ")[1] == "capacitate":

        line = command.split(" ")

        for item in lecturer_list:
            if item.lecturer_id == line[0]:
                item.add_capacity(line[2], int(line[3]))
                break

    elif command.split(" ")[1] == "mark":

        line = command.split(" ")

        for item in lecturer_list:
            if item.lecturer_id == line[0]:
                pass


    elif command.split(" ")[1] == "-all":
        for i in students_list:
            print(i.show_ranks())

