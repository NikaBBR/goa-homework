user_name = input("please enter your name: ")
user_surname = input("plesae enter your surname: ")
user_age = input("please enter your age: ")


def user_info(name,surname,age):
    return "hello " + name + " " + surname + " you are " + age
print(user_info(user_name,user_surname,user_age))