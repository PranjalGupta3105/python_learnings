userno="1,2,3,4,5"
usernumbers=userno.split(",")
print("The Numbers in the List of String are Splitted into")
print(usernumbers)
user_numbers=[]
for number in usernumbers:
    user_numbers.append(int(number))
    
print("The Numbers in the List Mutipled by two are :-")
[print((int(number))*2) for number in usernumbers]



#print(user_numbers)
#1)It converts the Number into the temporary Variable number at run time whose value is  of the String type
#2)String Repeated two times

