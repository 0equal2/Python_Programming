### [백준]2675

n=int(input())


for i in range(n):
    info=list(map(str,input().split()))

    count=int(info[0])
    s=info[1]

    for j in s:
        for k in range(count):
            print(j,end="")
    print()
