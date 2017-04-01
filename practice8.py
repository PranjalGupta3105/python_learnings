n=int(input())
a=[]
same=[]
for no in range(n):
    a.append(input(""))


for no in range(n):
    for j in range(n):
        if a[no]==a[j+1]:
           same=j+1

for no in range(n):
    if no==same:
        print("Don't give")

    else:
        print("Give")
#stuset=set(a)
#stulist=list(stuset)
#type(a)
#type(stuset)
#type(stulist)
#for no in range(n):
#    if a[no]!=stulist[no]:
#        print("Don't Give")
#print("Give")   
