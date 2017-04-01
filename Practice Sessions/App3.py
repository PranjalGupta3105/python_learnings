


def stu_data():
    name=input("enter name")
    stu_datadic={"Name":name,"Marks":[]}
    return stu_datadic



def add_marks(student,mark):
    student['Marks'].append(mark)

def cal_avg(student):
    total=sum(student["Marks"])
    if len(student["Marks"])==0:
        return 0

    avrg=total/(len(student["Marks"]))
    return avrg

s=stu_data()
result=cal_avg(s)
print(result)
add_marks(s,20)
result=cal_avg(s)
print(result)
add_marks(s,40)
result=cal_avg(s)
print(result)