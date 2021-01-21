###[백준]1110


n=int(input())
#1. 만약 n이 10보다 작으면 *10
if n<10:
    n=n*10


x=n
count=0

while True:
    
    #2.
    s=(x//10)+(x%10)

    a=str(x%10)
    b=str(s%10)

    x=int(a+b)
    count+=1

    if x==n:
        break
    

    
        
print(count)
