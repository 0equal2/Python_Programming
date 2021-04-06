###백준 #2747
#피보나치 수


def Fibonacci(a,b,count,n):
    
    if count==n:
        return(a+b)

    else:
        return Fibonacci(b,a+b,count+1,n)


#1. n
n=int(input())

#2.
if n==0:
    print(0)

elif n==1:
    print(1)

else:
    print(Fibonacci(0,1,2,n))
