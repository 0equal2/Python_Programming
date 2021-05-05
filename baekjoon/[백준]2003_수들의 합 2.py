###백준 #2003
#수들의 합 2

#1. 수의 개수, 수들의 합 : n, m
n,m=map(int,input().split())

#2. 수열 : a
a=list(map(int,input().split()))

#3.
left=0
right=0

now=a[0]
result=0

while True:
    #3-1. 현재 합이 m보다 작으면 right+1
    if now<=m :
        if now==m:
            result+=1

        
        right+=1
        
        #3-2.right가 a크기를 벗어나면 break
        if right>=n:
            break

        now+=a[right]
        
    #3-3. 현재 합이 m보다 크면
    elif now>m:
        now-=a[left]
        left+=1


print(result)


        
