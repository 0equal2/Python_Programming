###백준 #1026
###보물

#1. n 입력
n=int(input())

#2. a 입력
a=list(map(int,input().split()))

#3. b 입력
b=list(map(int, input().split()))


#4. a,b정렬
a=sorted(a, reverse=True)
b=sorted(b)

#5.
result=0

for i in range(n):
    result+= a[i]*b[i]

print(result)
