###[백준]8958

n=int(input())




for i in range(n):
    result=0
    count=0
    score=list(map(str,input()))

    for j in score:
        if j=='O':
            count+=1
            result+=count
        else:
            count=0

    print(result)
    
    
