#ფუნქციას გადაეცემა ორი არგუმენტი: სიტყვა და შესაცვლელი სიმბოლო. დააბრუნეთ სიტყვა, საიდანაც ამოშლილი იქნება ყველა შესაცვლელი სიმბოლო. f("hello", "l') = "heo" ახსნა: სიტყვაში შეგვხვდა "l", ამიტომ ის ამოიშალა
def remove_symbol(word, symbol):
    return word.replace(symbol, "")
result = remove_symbol("hello", "l")
print(result) 