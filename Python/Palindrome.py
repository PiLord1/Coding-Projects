name = input("Enter something: ")
def invertstring(name):
    if name[:].lower() == name[-1::-1].lower():
        print(name + " is a palindrome.")
    else:
        print(name + " is not a palindrome.")
        return ""
x = invertstring(name)
print(x)