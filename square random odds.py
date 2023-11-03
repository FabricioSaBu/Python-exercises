import random

my_Number = random.randint(1, 100)
my_First_List = []
my_Second_list = []
for i in range(my_Number):
    my_First_List.append(random.randint(1, 100))
for n in my_First_List:
    if n % 2 != 0:
        my_Second_list.append(n * n)
print(my_Second_list)
