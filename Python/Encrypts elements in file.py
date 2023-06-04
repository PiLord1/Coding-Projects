try:
    name_input = input("Enter name of input file: ")
    with open(name_input, "r") as original:
        get_word = original.readlines()
        encrypted_word = ""
        for word in get_word: 
            for i in word:
                if i.isnumeric() or i.isalpha():
                    if i.isnumeric():
                        orig = ord(i) + 1
                        if orig > ord("9"):
                            orig -= 10
                        encrypted_num = chr(orig)
                        encrypted_word += str(encrypted_num)
                    elif i.isalpha():
                        if i.islower():
                            orig = ord(i) - 31
                            if orig == ord("["):
                                orig -= 26
                            encrypted_letter = chr(orig)
                            encrypted_word += encrypted_letter
                        elif i.isupper():
                            orig = ord(i) + 33
                            if orig == ord("{"):
                                orig -= 26
                            encrypted_letter = chr(orig)
                            encrypted_word += encrypted_letter
                else:
                    encrypted_word += str(i)
except IOError:
    print("\n" + name_input + " not found!")
else:
    try:
        name_output = input("Enter name of output file: ")
        with open(name_output, "r") as encrypted:
            get_encrypted = encrypted.readlines()
    except IOError:
        print("\n" + name_output + " not found!")  
    else:
        with open(name_output, "w") as encrypted:
            encrypted.writelines(encrypted_word)
            print("\nOutput has been written to " + name_output)
finally:
    print("\n*****Program finished*****\n")

        
    

