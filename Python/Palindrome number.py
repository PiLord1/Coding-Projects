x=int(input("Enter an integer: "))
x_string=str(x)
def palindromeChecker(x_string):
    x_list = [*x_string]
    x_list_reversed = []
    for i in range(len(x_list)-1,-1,-1):
        x_list_reversed.append(x_list[i])
    if x_list == x_list_reversed:
        print("True")
    else:
        print("False")
palindromeChecker(x_string)

