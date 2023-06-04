num_1 = float(input("Enter 1st number: "))
num_2 = float(input("Enter 2nd number: "))
print("\n1 - addition\n2 - subtraction\n3 - multiplication\n4 - division (quotient and remainder) \n5 - exponentiation")
operation = input("Choose an operation: ")
if operation == "1":
    sum = num_1 + num_2
    print(sum)
elif operation == "2":
    diff = num_1 - num_2
    print(diff)
elif operation == "3":
    product = num_1 * num_2
    print(product)
elif operation == "4":
    quotient = num_1 // num_2
    remainder = num_1 % num_2
    print(str(quotient) + " and remainder " + str(remainder))
elif operation == "5":
    exp = num_1 ** num_2
    print(exp)
else:
    print("Invalid answer")

