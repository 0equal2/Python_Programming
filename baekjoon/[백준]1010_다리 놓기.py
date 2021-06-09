###백준 #1010
###다리 놓기


#1. test case
tc=int(input())

#2.n,m입력받기
for testcase in range(tc):
    n,m=map(int,input().split())
    result=1
    
    for i in range(n):
        result*=m-i
        result//=i+1

    print(result)
