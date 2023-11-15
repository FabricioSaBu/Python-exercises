user_Number = int(input("Please enter the number of Fibonacci terms you want: "))
fibonacci_List = [0, 1]

if user_Number == 0:
    print("There are no elements in this list.")
elif user_Number == 1:
    print(fibonacci_List[:1])
elif user_Number < 0:
    print("Please don't write negative numbers.")
else:
    while len(fibonacci_List) < user_Number:
        fibonacci_List.append(fibonacci_List[-1] + fibonacci_List[-2])
    print(fibonacci_List)
