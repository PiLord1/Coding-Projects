try:
    name_input = input("Enter the name of input file: ")
    input_file = open(name_input, "r")
except IOError:
    print("\n" + name_input + " doesn't exist in same folder!")
else:
    read = input_file.readlines()
    new_read = sorted(read, key=str.casefold)
    updated = []
    for line in new_read:
        if line[-1] != "\n":
            line = line + "\n"
        updated.append(line)
    input_file.close()
    if len(read) == 0:
        print("\n" + name_input + " is empty. Nothing to sort.\n")
    else:
        try:
            name_output = input("Enter the name of output file: ")
            output_file = open(name_output, "r")
        except IOError:
            print("\n" + name_output + " doesn't exist in same folder!")
        else:
            output_file1 = open(name_output, "w")
            output_file1.writelines(updated)
            print("\nSorted file written to " + name_output)
            output_file1.close()
            output_file.close()  
finally:
    print("\n*****Program finished*****\n")
        
    
    
     