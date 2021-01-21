###[백준]1475

room=input()
memo=[0]*10

count=0

for i in room:
    i=int(i)
    
    if i==6 or i==9:
        if memo[6]<=memo[9]:
            memo[6]+=1
            count=max(count,memo[6])

        else:
            memo[9]+=1
            couint=max(count,memo[6])

    else:
        memo[i]+=1
        count=max(count,memo[i])

print(count)
        

        
