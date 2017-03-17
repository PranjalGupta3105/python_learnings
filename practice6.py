#All Set Operations in the Document below 
set1={1,2,3,4}
set2={5,6,7,8}
print(set1)
print(set2)
print("Union Operation on the Set")
print(set1.union(set2))
print("")
print("Intersection Operation on the above given Set is Resulted to:-")
no=set1.intersection(set2)
if no==set():
    print("No Element Found")

print("")
set3={1,2,3,4}
set4={4,5,6,7}
print(set3)
print(set4)
print("The Difference of Two Sets is")
print(set3.difference(set4))

print("")
print("Given Two Sets:--")
set5={1,2,3}
set6={1,2,3,4,5}
print(set5)
print(set6)
answer=set5.issubset(set6)
if answer==True:
    print("The first set is a subset of the Underlining Set")

print("")
print("Given Two Sets:--")
print(set5)
print(set6)
answer1=set6.issuperset(set5)
if answer1==True:
    print("The Second set is the Super Set of the first set")

print("")
if  5 not in set1:
    print("No 5 is not in the set1")

print("")
print("length of set1 is-{} , of set2 is-{} , of set3 is-{} , of set4 is-{} , of set5 is-{} , and of set6 is-{}".format(len(set1),len(set2),len(set3),len(set4),len(set5),len(set6)))


print("")
set7=set1.symmetric_difference(set4)
#new set with elements in either set1 or set4 but not both
print("New Set with Symmetric Difference is {}".format(set7))

print("")
set8=set7.copy()
set9=set8.union({4,8,9,10})
print("This set {} is formed by copying previous set and adding a few new values in the set".format(set9))
