###백준 #1138
###한 줄로 서기

#1. 사람 수 : n
n=int(input())


#2. 자기보다 키가 큰 사람이 왼쪽에 몇명있는가
left=list(map(int,input().split()))


#3. 메모 : 내앞에 큰 사람이 있는 수 
memo=[i for i in range(n)]

#4.
loc=[0 for i in range(n)]

for i in range(len(left)):

    #4-1. 현재 사람의 키
    num=i+1

    #4-2. 필요 키 큰 사람의 수
    count=left[i]

    #4-3. 예상 위치
    x=left[i]


    while True:
        if (count-memo[x])==0:
            break

        x+=1
        


    loc[x]=num
    
    for j in range(x,len(left)):
        memo[j]-=1

        

print(' '.join(map(str,loc)))

   
