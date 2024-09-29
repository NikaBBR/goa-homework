#ფუნქციას გადაეცემა სია და რიცხვი x, დააბრუნეთ ამ სიის მე-x ე უდიდესი ელემენტი. f([3,5,8,7,2], 4) = 3. ახსნა: სიაში [3,5,8,7,2] უდიდესი ელემენტია 8, მეორე უდიდესი 7,...,მეოთხე - 3

def find_xth_largest(lst, x):
    sorted_lst = sorted(lst, reverse=True)  
    return sorted_lst[x - 1]  

result = find_xth_largest([3, 5, 8, 7, 2], 4)
print(result) 