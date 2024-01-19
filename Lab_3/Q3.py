def binarySearch(a,x,si,ei):
    if(si>ei):
        print("Element not found")
    else:
        mid = si+(ei-1)//2
        if(a[mid]>x):
           binarySearch(a, x, mid+1, ei)
        elif(a[mid]<x):
           binarySearch(a,x,si,mid-1)
        elif(a[mid]==x):
           print("Element found at "+str(mid))
 
li = [int(i) for i in input("Enter the list").split()]
x = int(input("Enter the element to be searched"))
binarySearch(li,x,0,len(li)-1)
