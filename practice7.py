def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)

    

print("enter the no")
number=int(input(""))
result=fact(number)
print(result)
print(len(str(result)))
