###[백준]2442

n=int(input())


for i in range(n):
    num1=n-i-1
    num2=2*i+1

    for j in range(num1):
        print(" ",end="")

    
    for j in range(num2):
        print("*",end="")

    print()
        
        
