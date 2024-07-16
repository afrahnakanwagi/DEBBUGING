if True:
    print("Hello,World")


y = 2
print(y)

x = 5 + 10

print(x)


def calculate_sum(numbers):
    sum = 0

    for num in numbers:
        sum += num  

        return sum  

numbers = [1, 2, 3, 4, '5'] 

result = calculate_sum(numbers)

print(f"The sum of numbers is: {result}")