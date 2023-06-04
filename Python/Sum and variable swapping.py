num = int(input("Enter a number: "))
num_1 = 1
num_2 = 0
count = 1
if num == 0:
    print(1)
else:
    while count <= num:
        sum = num_1 + num_2
        count += 1
        num_1 = num_2
        num_2 = sum
        print(sum)
