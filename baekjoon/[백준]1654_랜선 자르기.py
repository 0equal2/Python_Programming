### 백준 #1654
### 랜선 자르기


from sys import stdin

#1. k, n 입력
k,n=map(int,stdin.readline().split())


#2. 가지고 있는 랜선들
lanwire=[]

for i in range(k):
    lanwire.append(int(stdin.readline()))

#print(lanwire)

#3. 이분 탐색
left=1 #랜선 최소길이
right=max(lanwire) #랜선 최대길이



while left<=right:
    
    mid=(left+right)//2
    #print(left,right,mid)

    count=0 #mid 길이씩 잘랐을 때 얻을 수 있는 랜선 수
    for wire in lanwire:
        count+=wire//mid


    if count>=n: #랜선 수>필요수 : 자르는 단위 증가
        left=mid+1

    elif count<n : #랜선 수<필요 수 : 자르는 단위 감소
        right=mid-1




print(right)
        
