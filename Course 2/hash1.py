f=open('hash.txt','r')
x=f.readlines()
a=[int(l) for l in x ]
s=dict.fromkeys(range(1000000), False)
for i in range(0,len(a)):
    s[i] = True
n=1000000
count = 0
for j in range(-10000,10000):
   
    flag = False
    
    for i in x:
        
        if (j-i) in s and x != (j-i):
        
            flag = True
            break
    if flag:
        count+=1

print(count)
