#1) მომხმარებელს შემოატანინეთ ტესტში მიღებული ქულა, თუ ქულა მეტია 90 - ზე და ნაკლებია 100 - ზე მაგ შემთხვევაში დაპრინტეთ, თქვენ დაგიფინანსდებათ სწავლა სრულიად. თუ მიღებული ქულა მეტია 70 - ზე და  ნაკლებია 80 - ზე მაგ შემთხვევაში დაპრინტეთ, თქვენ დაგიფინანსდებათ სწავლა 1500 ლარით, თუ მიღებული ქულა მეტია 40 -  ზე და ნაკლებია 70 - ზე მაგ შემთხვევაში დაპრინტეთ, თქვენ დაგიფინანსდებათ სწავლა 500 ლარტით, ხოლო თუ მიღებული ქულა ნაკლებია 40 ზე, მაგ შემტხვევაში დაპრინტეთ, ტქვენ არ დაგიფინანსდებათ სწავლის პროცესი
score = int(input(" შეიყვანეთ ქულა :  "))
if score > 90 or score < 100:
    print(" თქვენ დაგიფინანსდებათ სწავლა სრულიად ")
elif score > 70 or score < 80:
    print(" თქვენ დაგიფინანსდებათ სწავლა 1500 ლარით ")
elif score > 40 or score < 70:
    print(" თქვენ დაგიფინანსდებათ სწავლა 500 ლარით ")
elif score < 40:
    print(" თქვენ არ დაგიფინანსდებათ სწავლის პროცესი ")