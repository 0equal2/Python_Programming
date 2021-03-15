###백준 #13335
#트럭

#1. n w, l : 트럭의 개수, 다리의 길이, 다리의 최대하중
n,w,l=map(int,input().split())

#2. 각 트럭의 무게
truck=list(map(int,input().split()))

#3.
memo=[0 for i in range(n)] #트럭의 위치 
bridge=l #현재 올라 올 수 있는 트럭의 무게
time=0

start=0 #다리에 올라와 있는 트럭들 중 제일 앞에 있는 트럭 번호
end=0 #다리를 건너야 하는 트럭 번호

while True:
    #3-1.
    time+=1
    
    #3-2. 올라와 있는  트럭들 한 칸씩 앞으로
    for i in range(start,end):
        memo[i]+=1

        if memo[i]>w:
            bridge+=truck[i]
            start+=1

    #3-3. 모든 트럭이 다리를 통과하면 끝
    if start==n:
        break
            
    #3-4. 트럭이 올라올 수 있으면 올라옴
    if end<n:
        if truck[end]<=bridge:
            bridge-=truck[end]
            memo[end]+=1
            end+=1
            

    
print(time)
        
        
