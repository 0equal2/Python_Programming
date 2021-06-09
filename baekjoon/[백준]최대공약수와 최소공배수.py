###백준 #2609
###최대공약수와 최소공배수

#1. 숫자 두개
a,b=map(int,input().split())


#2. 최대 공약수
def gcd(a,b):
    if a<b:
        (a,b)=(b,a)

    while b!=0:
        (a,b)=(b,a%b)

    return a


#3. 최소공배수
def lcm(a,b,g):
    return (a*b)//g


#4.
g=gcd(a,b)
l=lcm(a,b,g)

print(g)
print(l)
