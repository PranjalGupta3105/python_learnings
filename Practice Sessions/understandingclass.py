student_list = []


class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []


def create_new_stu():
    name = input('Enter the name of the student')
    student_data = Student(name)
    return student_data


def add_marks(student_object,mark):
    student_object.marks.append(mark)


def cal_average(student_object):
    num = len(student_object.marks)
    if num == 0:
        return 0

    total = sum(student_object.marks)
    return total / num


def print_stu_detail(student_object):
    ##print(student_object.name)
    ##print(cal_average(student_object))

    print("{} Average Marks are: {}",format(student_object.name,type(cal_average(student_object))))
    ##print("{}".format(student_object.name))
    ##print("and {} are the average marks ".format(cal_average(student_object)))


def print_stu_list(complete_list_of_student):
    for i, students in enumerate(complete_list_of_student):
        print("ID {}".format(i))
        ##print(students)
        print_stu_detail(students)


def menu_select():
    print("Please make the appropriate Selection for the following Operations",
          "Select c for Creating a New Student Data",
          "Select m for add marks to the Existing Student",
          "Select Cavg_np for Calculating The Average and Printing it ",
          "Select pl for Printing Student List",
          "Select e for exiting the App"
          )
    user_choice = input("Enter Your Selection Here:")

    while user_choice!="e":
        if user_choice == "c":
            student_list.append(create_new_stu())
        if user_choice == "m":
            id = int(input("Enter the Id of Student whose marks you wanna Add"))
            mark = int(input("Enter the Marks now:"))
            add_marks(student_list[id],mark)
        if user_choice == "Cavg_np":
            id = int(input("Enter the Id of Student whose Average you wanna See:"))
            stu_avg = cal_average(student_list[id])
            print("The average of {} is {}".format(student_list[id].name,stu_avg))
        if user_choice == "pl":
            print_stu_list(student_list)
        if user_choice == "e":
            SystemExit

        print("Please make the appropriate Selection for the following Operations",
              "Select c for Creating a New Student Data",
              "Select m for add marks to the Existing Student",
              "Select Cavg_np for Calculating The Average and Printing it ",
              "Select pl for Printing Student List",
              "Select e for exiting the App"
              )
        user_choice = input("Enter Your Selection Here:")


menu_select()
