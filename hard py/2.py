#ფუნქციას გადაეცემა სია. დააბრუნეთ True, თუ ამ სიაში მეორდება ელემენტი ორჯერ. სხვა შემთხვევაში დააბრუნეთ False. f([4,6,3,7,4,9,8]) = True. ახსნა: 4 მეორდება 2-ჯერ.
def has_duplicate(lst):
    return len(lst) != len(set(lst))
print(has_duplicate([4, 6, 3, 7, 4, 9, 8]))