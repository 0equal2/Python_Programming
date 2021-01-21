###[백준]1032

n=int(input())

result=list(input())


for i in range(1,n):
    command=list(input())
    for j in range(len(result)):
        if result[j]!=command[j]:
            result[j]='?'

print(''.join(result))


    
