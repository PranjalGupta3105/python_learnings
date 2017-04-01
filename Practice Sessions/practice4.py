import random
magic=[random.randint(0,9),random.randint(0,9)]
print("Enter the chances You want to play the Game")
chances=int(input(""))



def no_of_chances():
    for attempt in range(chances):
        check_user()

def check_user():
    print("Please Enter your no")
    user_ip=int(input(""))
    if user_ip in magic:
        print("You got it Right")
    if user_ip not in magic:
        print("You didn't quite Get it")

no_of_chances()
