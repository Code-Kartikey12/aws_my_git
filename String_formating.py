import random
age = random.randrange(25,85)
name = 'Kartikey'
#for python 3.6 and above
print(f"Age of {name} is {age}"); # print("\nAge of "+name+" is "+age) <- this will give error unlike C
#for python 3.6 and below
print("Age of {} is {}".format(name,age))

x = 0
for i in name:
    print(f"{name} and {x} "+i)
    x = x+1


# print(inte)
# type(inte)
print("array printing "+name[2])

