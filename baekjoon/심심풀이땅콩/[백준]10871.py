### [백준]10871

n, x = map(int,input().split())

num=list(map(int,input().split()))

for i in num:
    if i<x:
        print(i,end=" ")


