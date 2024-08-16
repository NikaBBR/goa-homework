list = []

for i in range(10):
    number = int(input("please enter any number:  "))
    list.append(number)

even_numbers = []
odd_numbers = []

for number in list:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

result_list = []
result_list += even_numbers
result_list += odd_numbers

print("result:",result_list)