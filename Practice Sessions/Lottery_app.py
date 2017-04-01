#User can pick 6 Numbers
#Lottery calculates 6 Random Numbers (between 1 and 20)
#Then we  match the user numbers to the Lottery Numbers
#Calculate the Winning based on how many Numbers the User Matched
import random
def playagain():
    print("Do You Wanna play it Again")
    usersaid=input("")
    if usersaid=="True":
        print("Please Enter Any 6 Random Numbers between 1 to 20")
        uip1=int(input())
        uip2=int(input())
        uip3=int(input())
        uip4=int(input())
        uip5=int(input())
        uip6=int(input())
        Result=ltapp(uip1,uip2,uip3,uip4,uip5,uip6)
              
        
    
            
                    
def ltapp(uip1,uip2,uip3,uip4,uip5,uip6):

        userip={uip1,uip2,uip3,uip4,uip5,uip6}
        #print("you have Entered the Numbers-{}".format(userip))
        comptestcases={random.randint(1,20),random.randint(1,20),random.randint(1,20),random.randint(1,20),random.randint(1,20),random.randint(1,20)}
        var=userip.intersection(comptestcases)
        if var!=set():
            return "Congrats You Have Won the Lottery"
            
            
        return "Oops Hard Luck This Time"
        

print("Welcome to the Lottery App")
#counter=3
print("Do you Wanna Play say True or False")
myans=input()
if myans=="True":
    print("Please Enter Any 6 Random Numbers between 1 to 20")
    uip1=int(input())
    uip2=int(input())
    uip3=int(input())
    uip4=int(input())
    uip5=int(input())
    uip6=int(input())
    Result=ltapp(uip1,uip2,uip3,uip4,uip5,uip6)
    print(Result)
    playagain()




    
       
    


