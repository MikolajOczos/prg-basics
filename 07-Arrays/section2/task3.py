###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]
XD = " "
print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print("The last value", arr[len(arr)-1])
print("The last but one", arr[len(arr)-2])
print(int(arr[0])+int(arr[len(arr)-1]))
print("The middle value is", arr[(len(arr)-1)//2] )\
    
for i in arr:
    XD = XD + str(i) + " "


print(XD)
...
...