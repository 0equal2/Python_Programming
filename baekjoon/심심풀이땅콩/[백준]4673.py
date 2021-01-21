###[백준]4673


memo=[0]*10001

for i in range(1,10001):
    newnum=i+sum(list(map(int,list(str(i)))))

    if newnum<=10000:
        memo[newnum]=1

    if memo[i]==0:
        print(i)
    


