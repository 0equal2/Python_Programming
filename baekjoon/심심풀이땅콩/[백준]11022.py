### [백준]11022


n=int(input())

for i in range(1,n+1):
    a,b=map(int,input().split())

    print("Case #", end="")
    print(i, end="")
    print(":",a,"+",b,"=",a+b)

    
