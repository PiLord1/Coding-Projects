name1 = input("Enter 1st word: ")
name2 = input("Enter 2nd word: ")
def isanagram(name1, name2):
    x = name1.replace(" ", "")
    y = name2.replace(" ", "")
    if sorted(x.upper()) == sorted(y.upper()):
        print("This is an anagram")
    else:
        print("This is not an anagram")
    return ""
x = isanagram(name1, name2)
print(x)
    
    