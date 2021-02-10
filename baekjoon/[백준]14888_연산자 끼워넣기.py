### 백준 #14888
### 연산자 끼워넣기

from itertools import permutations

def calc(a,b,op):
    if op==0:
        return a+b
    elif op==1:
        return a-b
    elif op==2:
        return a*b
    elif op==3:
        if a<0:
            a=abs(a)
            return -(a//b)
        return a//b


#1. 수의 개수 n 입력
n=int(input())

#2. 숫자 리스트
number=list(map(int,input().split()))

#3. operation 개수
data=list(map(int,input().split()))
operation=[]

for i in range(4):
    for j in range(data[i]):
        operation.append(i)

#4. operation 경우의 수
case=list(permutations(operation,len(operation)))
case=set(case) #중복제


#5. 연산 값 구하기
result=[]
for op in case:
    x=number[0]
    for i in range(1,n):
        y=number[i]
        x=calc(x,y,op[i-1])
        
    result.append(x)

print(max(result))
print(min(result))
        

