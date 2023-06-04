num = int(input("Enter size: "))
for i in range(1, num, 2):
    print((num//2 - i//2) * " " + i * "*")
for b in range(num, -1, -2):
    print((num//2 - b//2) * " " + "*" * b)

    
    
    
    
    