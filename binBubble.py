##FUNCTIONS


def bubbleSort(lissy):
    for index in range(len(lissy)-1,0,-1):
        for index in range(index):
            if ( lissy[index]>lissy[index+1]):
                num = lissy[index]
                lissy[index] = lissy[index+1]
                lissy[index+1] = num

def binSearch(lissy, num):
    first = 0
    last = len(lissy)-1
    found = False

    while(first<=last)and not found:
        mid = (first+last)//2
        if (lissy[mid] == num):
            found = True
        else:
            if(num<lissy[mid]):
                last = mid-1
            else:
                first = mid+1

    return found
            
        
        
                


##RUNNING CODE
myList = [78,42,69,99,23,74,2,100]

bubbleSort(myList)

#print(myList)
print(binSearch(myList,14))
print(binSearch(myList,78))
