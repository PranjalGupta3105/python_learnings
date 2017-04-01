class Student:
    def __init__(self, name):
        self.name=name
        self.marks=[]

    def cal_avg(self):
        if(self.marks==[]):
           print("There are no marks available for the Student")
        else:
            total=total+self.marks
            avrg=total/(len(self.marks))
        return avrg
    
    def add_marks(self,mark):
        self.marks.append(mark)

    def print_me(self):
        return self.name

    def menu_choice(choice):
        if choice=="a":
            stu_name=input("Enter the student Number")
            Student(stu_name)
        else:
            if choice=="am":
                mark=int(input("Enter the Marks to be added"))
                add_marks(mark)
            else:
                if choice=="calav":
                    cal_avg(Student(self))
                
            
           
        
ch=input("Enter your choice:"
         "a to add a student,"
         "am to add a mark to the student,"
         "calav to calculate the average of the student,"
         "p to print the student details"
         )

Student.menu_choice(ch)
data=Student.print_me(self)
print(data)
