f=open('int.txt','r')
x=f.readlines()
int_x=[int(i) for i in x]
n=100000
count=0
def merge(arr, l, m, r):
    n1 = int(m - l + 1)
    n2 = int(r- m)
    L = [0] * (n1)
    R = [0] * (n2)
 
    
    for i in range(0 , n1):
        L[i] = arr[l + i]
 
    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]
 
    
    i = 0     
    j = 0     
    k = l     
 
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            global count
            count+=(n1-i)
            arr[k] = R[j]
            j += 1
        k += 1
        print(count)
   
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 

def mergesort(arr,l,r):
    if l < r:
 
        
        m = int((l+(r-1))/2)
 
      
        mergesort(arr, l, m)
        mergesort(arr, m+1, r)
        merge(arr, l, m, r)

mergesort(int_x,0,n-1)