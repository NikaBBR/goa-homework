import random

print("გამარჯობა მოდი ვითამაშოთ ჯეირანი")

choices = ['ქვა','ქაღალდი', 'მაკრატელი']
computer_choice = random.choice(choices)
user_choice = input("შეიყვანე შენი არჩევანი (ქვა , ქაღალდი ან მაკრატელი):  ")

while user_choice not in choices:
    print("არასწორი არჩევანი")
    user_choice = input("შეიყვანე შენი არჩევანი (ქვა , ქაღალდი ან მაკრატელი):  ")


print("your choice: ", user_choice)
print("compiuter choice:  ",computer_choice)

if user_choice == computer_choice:
    print("ფრეა")

elif (user_choice == 'ქვა' and computer_choice == 'მაკრატელი') or \
     (user_choice == 'ქაღალდი' and computer_choice == 'ქვა') or \
     (user_choice == 'მაკრატელი' and computer_choice == 'ქაღალდი'):
    print("შენ მოიგე!:")

else:
    print("შენ წააგე")