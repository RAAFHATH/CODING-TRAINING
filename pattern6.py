n=5
k=n
for i in range(1,n+1):
    for j in range(1,i+1):
        a=k-n+1
        print(a,end=" ")
        a-=1
    print()
    k+=1
