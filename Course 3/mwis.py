f=open('mwis1.txt','r')
x=f.readlines()
w=[]
n=int(x[0])
for line in x[1:] :
    w.append(int(line))

maxw = [0]*n
for i in range(0, n):
    if i==0:
        continue
    elif i ==1:
        maxw[i]=w[1]
        continue
    maxw[i]=max(maxw[i-1], maxw[i-2] + w[i-1])

i = n
mwis = []
while i >= 1:
    if maxw[i-1] >= maxw[i-2] + w[i-1]:
        i -= 1
    else:
        mwis.insert(0, w[i-1])
        i -= 2
print(mwis)
arr = [1, 2, 3, 4, 17, 117, 517, 997]
ans = '00000000'
k=0
for j in arr:
    if j < n:
        
        if w[j-1] in mwis:
            ans=ans[:k]+'1'+ans[k+1:]
        k+=1
print(w[3])
print(ans)