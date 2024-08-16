print("გამარჯობათ რაც გინდათ აირჩიეთ და კონსულტანტი დაგეხმარებათ")

price = int(input("რა ფასის ნივთი გჭირდებათ:  "))
discount = input("რა ფასდაკლება გინდათ:  ")

final = ((int(price) * int(discount)) / 100 )

print (price - final)