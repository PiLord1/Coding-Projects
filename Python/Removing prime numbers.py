num = input("Input entry (Q to end input): ")
orig = []
orig.append(num)
while (num != "Q"):
    num = input("Input entry: ")
    orig.append(num)
del(orig[-1])
print("Original list:", orig)
def delprime(orig):
    for num in orig[0:-1]:
        if (int(num) > 0):
            if (int(num) > 2):
                i = 2
                inc = 0
                while (int(num)//2 >= i):
                    if (int(num)%i != 0):
                        i += 1
                    else:
                        inc += 1
                        break
                if (inc == 0):
                    orig.remove(num)
            elif (int(num) == 2):
                orig.remove(num)
        else:
            pass
    print("Prime numbers removed:", orig)
    return ""
x = delprime(orig)
print(x)