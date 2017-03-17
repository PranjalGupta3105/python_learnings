import random
#chances=3
magic=[random.randint(0,9),random.randint(0,9)]
def chance_available(chances):
    for attempt in range(chances):
         check_op()

def check_op():
    print("Enter your Number User")
    user_input=int(input(""))
    if user_input in magic:
        print("You got the No Right")
    if user_input not in magic:
        print("You didn't quite get it")

chance_available(5)
    
