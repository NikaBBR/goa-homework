def num():
    sum = 0
    different_number = [77,777,33,44,31,26,79,80]
    for i in range (len(different_number)):
        sum = sum + different_number[i]
    print("sum of numbers:" + str(sum))

num()