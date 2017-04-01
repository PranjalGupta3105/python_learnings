a=[]
b=[]
nos=int(input())
for i in range(nos):
    a.append(input(""))
    
    
for i in range(nos):
    for j in range(i+1,nos):
        if a[i]==a[j]:
            b.append(j)
            
            
for i in range(nos):
    if i in b:
        print("Don't Give")
    else:
        print("Give")
