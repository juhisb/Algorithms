f=open('knap2.txt','r')
x=f.readlines()
x1=x[0].split()
w=int(x1[0])
n=int(x1[1])
weight=[]
value=[]
for l in x[1:] :
    l=l.split()
    
    val=[int(i) for i in l]
    value.append(val[0])
    weight.append(val[1])
    
print(value)
print(weight)                
knapsack = [[0 for x in range(w+1)] for x in range(n+1)]
 
    
for i in range(n+1):
    for j in range(w+1):
        if i==0 or j==0:
            knapsack[i][j] = 0
        elif weight[i-1] <= j:
            knapsack[i][j] = max(value[i-1] + knapsack[i-1][j-weight[i-1]],  knapsack[i-1][j])
        else:
            knapsack[i][j] = knapsack[i-1][j]
 
print(knapsack[n][w])