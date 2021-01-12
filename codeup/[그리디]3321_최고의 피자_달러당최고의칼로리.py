### 그리디 최고의피자
### codeup 3321


#1. 토핑수
n= int(input())

#2. 도우 가격, 토핑 가격
a,b=map(int,input().split())

#3. 도우 칼로리
c=int(input())

#4. 토핑 칼로리
d=[]

for i in range(n):
    d.append(int(input()))

#5. 토핑 칼로리 정렬
d.sort(reverse=True)
#print(d)


#6.
result=0 

kcal=0  #토핑 칼로리
cost=0  #토핑 가격

for i in d:
    kcal+=i
    cost+=b

    cal=(c+kcal)/float(a+cost)
    if result>cal:
        break
    else:
        result=cal


print(int(result))
        
