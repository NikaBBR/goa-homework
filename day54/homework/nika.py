def num():
    question = int(input("please enter the number:  "))
    question1 = int(input("please enter another number:  "))
    if question < question1:
        return(question)
    elif question1 < question:
        return(question1)

print(num())