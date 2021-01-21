###[구현]행렬이동문제 왕실의 나이트
###이것이 취업을 위한 코딩 테스트다  with  파이썬


#체스판은 8 x 8

#나이트가 이동할 수 있는 벡터 (L자 모양)
dx = [1,-1,1,-1,-2,-2,2,2]
dy = [2,2,-2,-2,1,-1,1,-1]


#현재 말의 위치 ex) a1 -> [0,0]
#ord(a)=97

now=input()
x=int(now[1])-1
y=ord(now[0])-97

#print(x,y)


#이동 가능한지 탐색 (총 8가지 방향  탐색)

count=0

for i in range(8):
    nx=x+dx[i]
    ny=y+dy[i]

    if(nx>=0 and nx<8 and ny>=0 and ny<8):
        count+=1


print(count)


