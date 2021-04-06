###백준 #2141
###우체국


#1. 마을의 개수 : n
n=int(input())

#2. 마을의 위치, 인구 수 : info : [x,a]
info=[]
people=0 #전체 인구 수

for i in range(n):
    x=list(map(int,input().split()))
    info.append(x)
    people+=x[1]

#3. 마을 위치 순으로 정렬
info=sorted(info)

#4. 인구의 절반 구하기 
mid=people//2

#4-1. 전체 인구가 홀수 일 경우에는 올림
if (people%2)==1:
    mid+=1

#5. 인구의 절반이 속한 마을에 우체국 설치
count=0
for l,p in info:
    count+=p

    if count>=mid:
        print(l)
        break
