#Generate 10 random No's and keep a track of the minimum no in them and print it
#in the last
import random
no=10
minimum=10
for i in range(no):
    randno=random.randint(1,9)
    print("{}".format(randno))
    if randno <= minimum:
        minimum=randno


print("The least Random No found in the list of {} was {}".format(10,minimum))
