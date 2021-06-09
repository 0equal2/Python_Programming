###백준 #2748
###피보나치 수 2


def fibo(x1,x2,count,n):
    if count==n:
        return x1+x2

    return fibo(x2,x1+x2,count+1,n)



#1. n 입력
n=int(input())


#2. n==0, n==1이면, print(0),print(1)
if n==0:
    print(0)
elif n==1:
    print(1)

#3. n>1일 경우
else:
    print(fibo(0,1,2,n))
