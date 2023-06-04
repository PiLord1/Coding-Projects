arr = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    # adding the element
    arr.append(ele) 
arr_new=set(arr)
print(arr_new)
