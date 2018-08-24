def binary_search(list,item):
    low=0
    high=len(list)-1
    i=0
    while low<=high:
        mid=(high+low)//2
        guess=list[mid]
        if guess==item:
            return mid,i
        if guess>item:
            high=mid-1
            i+=1
        else:
            low=mid+1
            i+=1
    return None

mylist=[1,3,5,7,9]
print(binary_search(mylist,9))
