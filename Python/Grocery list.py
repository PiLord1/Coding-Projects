grocery = ("chicken", "2.0", "3banana", "apple2.5")
print("Tuple contains", grocery)
locate = input("Enter item to search: ")
if locate in grocery:
    print("Index of", locate, "is", grocery.index(locate))
    print("Count is", grocery.count(locate))
else:
    print("Error, item is not part of the tuple")