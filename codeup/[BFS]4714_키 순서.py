### 코드업 #4714
### 키 순서

### *** 두번째 테스트 케이스에서 입력 형식이 바뀌어서 오류
### 때문에 나머지 테스트들이 맞는지 확인을 못함 ..


from collections import deque

def search(x,check):

    queue=deque()
    queue.append(x)
    
    check[x]=1

    up=0 #나보다 큰 사람 카운트

    while queue:
        x=queue.popleft()
        if x in info.keys():
            for i in info[x]:
                
                if check[i]==0:
                    
                    check[i]=1
                    visit[i]+=1 
                    up+=1

                    queue.append(i)

    return up
    



#1. 학생 수 n
n= int(input())

#2. 비교 횟수 m
m= int(input())


#3. 비교 정보
global info
info=dict()


for i in range(m):
    k,v=map(int,input().split())

    info[k]=info.setdefault(k,[])+[v]
    
    

#print(info)


#4. vist[i]= i보다 작은사람 + i보다 큰사
global visit
visit=[0 for _ in range(n+1)]



for i in range(1,n+1):
    
    check=[0 for _ in range(n+1)] #방문 체크 리스트
    visit[i]+=search(i,check)  #나보다 큰 사람 수를 더해준다.

    
    
#5. visit[i]가 i를 제외한 n-1명이라는 것은 i의 키 순위를 알 수 있다.
result=0
for i in range(1,n+1):
    if visit[i]==n-1:
        result+=1

print(result)
    
    
