# Combo package of Python learnings..........
student_list=[]
def create_student():
    name = input("Enter the Name of New Student you Wanna add:")
    student_data={"Name":name,          #A New Dictionary for Each Student
                  "Marks":[]
                  }
    print("Student {} added with Marks = {}".format(student_data['Name'],student_data['Marks']))
    return student_data

def add_mark(student):
    new_mark = int(input("Enter the New Marks you want to Add to:"))
    #if not student:
    #    print("The Marks Could Not be Entered since the Student does not exists.... Please Input the Student First")
    student["Marks"].append(new_mark)

def cal_avg_stu(student):
    total=sum(student["Marks"])
    input_marks=len(student["Marks"])
    calavg=total/input_marks
    return calavg

def print_list(student):
    ipid= int(input("Enter the Id of Student whose Data you wanna See:-"))

    for i, students in enumerate(student):
          if i == ipid:
            print("The Details for this Id {} student is{}".format(i, students))
            break
          elif i!=ipid :
              print("The Student Does not exists!!!")

def menu_select():
    print("Please make the appropriate Selection for the following Operations,"
          "Select c for Creating a New Student Data",
          "Select m for add marks to the Existing Student",
          "Select Cavg_np for Calculating The Average and Printing it ",
          "Select pl for Printing Student List"
          "Select e for exiting the App"
                                        )
    user_choice=input("Enter Your Selection Here:")

    while user_choice=="e":
       if user_choice == "c":
           student_list.append(create_student())
       elif user_choice == "m":
           id=int(input("Enter the Id of Student whose marks you wanna Add"))
           add_mark(student_list[id])
       elif user_choice == "Cavg_np":
           id = int(input("Enter the Id of Student whose Average you wanna See"))
           stu_avg = cal_avg_stu(student_list[id])
           print("The average of {} is {}".format(student_list[id],stu_avg))
       elif user_choice=="pl":
            print_list(student_list)
    menu_select()


menu_select()




