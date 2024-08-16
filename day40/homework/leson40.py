numbers = [1, 15, 342432, 123, 72, 235, 3, 132, 354, 13, 12, 1]
numbers_2 = []
counnter = 0

for i in range (len(numbers)):
    if 9 < numbers[i] < 100:
        counnter += 1

print(counnter)