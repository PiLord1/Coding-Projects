file = open((input("File name: ")), "r")
info = []
total = 0
read = file.readlines()
file.close()
grade1 = read[2]
grade2 = read[3]
grade3 = read[4]
avg = (float(grade1) + float(grade2) + float(grade3))/3
info = [read[0], read[1], str(avg) + "\n"]
info_update = []
for i in info:
    info_update.append(str(i)[:-1] + "\n")
print("Exam average is", str(avg))
file1 = open("students.txt", "a")
file1.writelines(info_update)
file1.close()