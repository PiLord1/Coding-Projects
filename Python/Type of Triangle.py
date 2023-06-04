num_1 = int(input("Enter 1st number: "))
num_2 = int(input("Enter 2nd number: "))
num_3 = int(input("Enter 3rd number: "))
print("")
if (num_1 == num_2 and num_2 == num_3 and num_1 == num_3) and (num_1 + num_2 > num_3 and num_2 + num_3 > num_1 and num_1 + num_3 > num_2):
    print("Equilateral Triangle")
elif ((num_1 == num_2 and num_1 != num_3) or (num_2 == num_3 and num_2 != num_1) or (num_1 == num_3 and num_1 != num_2)) and (num_1 + num_2 > num_3 and num_2 + num_3 > num_1 and num_1 + num_3 > num_2):
    print("Isosceles Triangle")
elif (num_1 != num_2 and num_2 != num_3 and num_1 != num_3) and (num_1 + num_2 > num_3 and num_2 + num_3 > num_1 and num_1 + num_3 > num_2):
    print("Scalene Triangle")
else:
    print("Can't form triangle")