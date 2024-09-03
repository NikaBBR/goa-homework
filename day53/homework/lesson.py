number = int(input(" enter a number:  "))

def num(number):

    if number == 0 :
        print(number, " is nether odd nether even")

    elif number % 2 == 0 :
        print(number, " is an odd number")

    else:
        print(number," is an even number")

num(number)