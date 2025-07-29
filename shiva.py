list=[2,4,6,8,10]
print("Unsorted list: ",list)
for j in range(len(list)-1):
    for i in range (len(list)-1-j):
        if list[i]>list[i+1]:
            list[i],list[i+1]=list[i+1],list[i]
            print(list)
        else:
            print(list)
    print()
print("Sorted list: ",list) 

###Selection sort
##print("selection sort: ")
##
##arr=[34,5,6,81,0,5]
##print("unsorted arr: ",arr)
##for i in range(len(arr)):
##    min_index=i
##    for j in range(i+j,len(arr)):
##        if arr[j]<arr[min_index]:
##            min_index=j
##    arr[j]<arr[min_index],arr[i]
##print("Sorted array: ", arr)

## LINEAR SEARCH

##print("linear search")
##
##list=[10,20,30,40,50]
##key=40
##found=False
##for i in range(len(list)):
##    if list[i] == key:
##        found=True
##        index=i
##        break
##if found:
##    print("Element ", key,"found at index",index)
##else:
##    print("Element",key,"not found in the list")

