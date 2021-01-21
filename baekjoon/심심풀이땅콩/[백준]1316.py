###[백준]1316


n=int(input())

count=0

for i in range(n):
    word=input()
    now=''

    alpha=[]
    check=1

    for j in word:
        if j not in alpha:
            alpha.append(j)
            now=j
        else:
            if now!=j:
                check=0
                break

    if check==1:
        count+=1



        

    
print(count)
