num = int(input("Enter a number: "))

def FibSeq(num):
    if num < 1:
        return("Invalid answer")
    elif num == 1 or num == 2:
        return 1
    else:
        return FibSeq(num-1) + FibSeq(num-2)
print(FibSeq(num))
    
