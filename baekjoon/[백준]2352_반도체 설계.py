###백준 #2352
###반도체 설계

from sys import stdin

#x를 삽입할 위치 return
def lowerbound(line,x):
    s,e=0,len(line)-1

    while s<=e:
        mid=(s+e)//2

        if line[mid]<x:
            s=mid+1
        else:
            e=mid-1

    return s

#1. 반도체 포트의 개수 입력 : n
n=int(stdin.readline())

#2. 연결 정보
connect=list(map(int,stdin.readline().split()))

#3. 최대 가능 연결 개수
line=[]

for x in connect:
    #3-1. 빈 line이거나 line의 마지막 원소가 x보다 작으면 x를 뒤에 추가해준다.
    if not line or line[-1]<x:
        line.append(x)

    #3-2. x가 line[-1]보다 작을 경우 x가 들어갈 수 있는 lower bound자리의 값을 x로 바꿔준다.
    else:
        line[lowerbound(line,x)]=x

print(len(line))
        

