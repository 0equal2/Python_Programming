### 그리디 택배
### codeup 4787

from collections import deque


#1. 마을의 수와 트럭 용량
n, c = map(int, input().split())

#2. 박스 정보의 개수
m=int(input())


#3. 박스 정보
info=[]

for i in range(m):
    info.append(list(map(int, input().split())))
    

#4. 도착지, 받는지 순서로 정렬한다 
info=sorted(info, key=lambda x: (x[1],x[0]))

#for i in info:
    #print(i)


#5. 해당 마을에서 실을 수 있는 용량 메모
memo=[c]*(n+1)  # 헷갈리지않게 n+1개로 배열을 만든다.

#print(memo)


#6.
result=0

for i in range(m):
    end=info[i][1]
    start=info[i][0]

    # 출발지부터 목적지 전까지의 최소값과 실어야하는 택배의 용량의 최소값을 구함
    move=min(memo[start:end])
    move=min(move,info[i][2])

    for j in range(start, end):
        memo[j]-=move

    result+=move
    #print(memo)


print(result)

    

                
                    

                
            
    

        
        
        

    
