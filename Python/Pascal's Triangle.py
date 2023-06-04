num = int(input("Enter a number: "))
def recursion(num):
    if num < 1:
        return []
    elif num == 1:
        return [1]
    elif num == 2:
        return [1,1]
    else:
        call = recursion(num-1)
        base = []
        base.append(1)
        for i in range(num-2):
            base.append(call[i] + call[i+1])
        last_list = [1]
        base.extend(last_list)
        return base
print("Pascal", num, recursion(num))