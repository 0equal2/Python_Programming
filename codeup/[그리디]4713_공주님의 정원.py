### 그리디 공주님의 정원
### CodeUp 4713



#1. 꽃들의 개수 : n
n=int(input())

#2. 날짜
flower=[]

#2-1. 월, 일 처리를 월에 100을 곱하여 편하게 처리하자.
for i in range(n):
    arr=list(map(int, input().split()))
    start=arr[0]*100+arr[1]
    end=arr[2]*100+arr[3]
    flower.append([start,end])

#3. 먼저 피고 지는  순서로 정렬
flower.sort()

"""
for i in range(n):
    print(flower[i])

#print(flower)
print('====================')
"""



count=0

memo=0
start=301

maxdate=0

for i in range(n):

    #print(start, maxdate,count,'/', flower[i][0],flower[i][1])

    # 목표 달성시 종료
    if start>1130:
        break


    # 꽃을 피울 수 있다
    if flower[i][0]<=start and flower[i][1]>start:

        # 카운트가 안되어있다면
        if memo!=start:
            memo=start
            count+=1

        if maxdate<flower[i][1]:
            maxdate=flower[i][1]

    # 꽃을 피울 수 없다
    else:
        if memo==start:
            if flower[i][0]<=maxdate and flower[i][1]>maxdate:
                start=maxdate
                memo=start
                maxdate=flower[i][1]
                count+=1

        else:
            if start<flower[i][0]:
                count=0
                break


# 모든 날짜를 탐색하였지만 11월 30일까지 꽃을 못피울때    
if maxdate<=1130:
    count=0
    


print(count)






## 참고 : https://swblossom.tistory.com/81


        
    

