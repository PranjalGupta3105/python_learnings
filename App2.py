def create_student(name):
    mark=[]
    for i in range(5):
        mark.append(int(input()))

    stu_dictionary={"name":name,"Marks":mark}
    return stu_dictionary

name=input("Enter Student Name:==")
result=create_student(name)
print(result)
