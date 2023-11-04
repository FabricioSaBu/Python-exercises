my_Number = int(input("please write down your number: "))
my_List = []
for i in range(1, my_Number + 1):
    if my_Number % i == 0:
        my_List.append(i)
if sum(my_List) == my_Number + 1:
    print("your number is a prime number c:")
else:
    print("your number is not a prime number :c")
