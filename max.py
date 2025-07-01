a=[1,2,6,7,3,4,5]
max1=max2=a[0]
for i in a:
    if i > max1:
        max2 = max1
        max1 = i
    elif i > max2:
        max2 = i
print("The maximum value in the list is:", max2)  
