def num():
    question = int(input("please enter the number:  "))
    if question < 0:
        return("უარყოფიტი")
    elif 0 < question:
        return("დადებითი")

print(num())