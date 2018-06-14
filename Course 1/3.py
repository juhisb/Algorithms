f=open('quicktxt.txt','r')
x=f.readlines()
int_x=[int(i) for i in x]
n=10000
count=0
def swap(array, index1, index2):

    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

def partition(arr, l, r):
    if (r-l-1)%2 == 0:
        m=int((l+(r-l-1)/2))
    else:
        m=int((l+(r-l)/2))
    if (arr[l]<arr[m] and arr[m]<arr[r]) or (arr[r]<arr[m] and arr[m]<arr[l]) :
        pi=m
    elif (arr[m]<arr[l] and arr[l]<arr[r]) or (arr[r]<arr[l] and arr[l]<arr[m]):
        pi=l
    else:
        pi=r
    swap(arr,l,pi)
    p=arr[l]
    i=l+1
    for j in range(l+1,r+1):
        
        if arr[j]<p:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            i=i+1
    temp=arr[l]
    arr[l]=arr[i-1]
    arr[i-1]=temp
   
    
    return (i-1)
    
 

def quicksort(arr,l,r):
    
    if l < r:
        global count
        count+=(r-l)
        print(count)
        p=partition(arr,l,r)   
        quicksort(arr, l, p-1)
        quicksort(arr, p+1, r)
        

quicksort(int_x,0,n-1)
#for i in range(n):
    #print ("%d" %int_x[i])