#ფუნქციას გადაეცემა სია. დააბრუნეთ სია, სადაც არის ამ სიის მხოლოდ ლუწი რიცხვები. f([5,4,56,7,8,3,563]) = [4,56,8]. ახსნა:
#  ამ სიის ლუწი ელემენტები.

def even_only(arr):
    even_arr = []
    for i in arr:
        if i % 2 == 0:
            even_arr.append(i)
    return even_arr

print(even_only([5,4,56,7,8,3,563]))