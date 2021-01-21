###[백준]2446

n=int(input())

for i in range(n-1,-1,-1):
    num1=2*i+1
    num2=n-i-1

    for j in range(num2):
        print(" ",end="")
        
    for j in range(num1):
        print("*",end="")
    print()


for i in range(1,n):
    num1=2*i+1
    num2=n-i-1
    for j in range(num2):
        print(" ",end="")
    for j in range(num1):
        print("*",end="")
    print()
