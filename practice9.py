def splt(u_number):
    temp_sum=0
    no_len=len(str(u_number))
    
    for i in range(no_len):
        n=u_number%10
        temp_sum=temp_sum+fact(n)
        u_number=int(u_number/10)
        

    return temp_sum

def fact(n):
    if n==0:
        return 1
    else:
       return n*fact(n-1)
 
    
    
u_num=int(input(""))
splt(u_num)
result=splt(u_num)
print(result)



    
            
  




