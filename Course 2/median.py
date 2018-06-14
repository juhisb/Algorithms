import heapq
lowheap=[]
highheap=[]
ans=0
f=open('median.txt','r')
x=f.readlines()
a=[int(l) for l in x ]
for i in range(0,len(a)):
    if i==0:
        
        highheap.append(a[i])
        heapq.heapify(highheap)
        ans+=a[i]
        #print("high",highheap)
        continue
    if i==1:
        if heapq.nsmallest(1,highheap)[0] < a[i]:
            lowheap.append(heapq.heappop(highheap))
            highheap.append(a[i])
            heapq.heapify(highheap)
            heapq.heapify(lowheap)
            #print("high",highheap)
            
        else:
            lowheap.append(a[i])
            heapq.heapify(lowheap)
            #print("low",lowheap)
            
            
        ans+=heapq.nlargest(1,lowheap)[0]
        print(ans)
        continue
    max = heapq.nlargest(1,lowheap)
    #print(max)
    if(a[i] < max[0]):
        highheap.append(max[0])
        heapq.heapify(highheap)
        lowheap=[i*-1 for i in lowheap]
        heapq.heapify(lowheap)
        #print("low",lowheap)
        heapq.heappop(lowheap)
        lowheap=[i*-1 for i in lowheap]
        
        lowheap.append(a[i])
        heapq.heapify(lowheap)
    else:
        highheap.append(a[i])
        heapq.heapify(highheap)
    if len(highheap)-len(lowheap) > 0:
        lowheap.append(heapq.heappop(highheap))
        heapq.heapify(lowheap)
    
    

    ans+=heapq.nlargest(1,lowheap)[0]
    print(ans)

print(ans%10000)
    




        
    
        
