###[백준]5622

word=input()

dial={}
alpha=65

for i in range(2,10):
    if i==9 or i==7:
        count=4
    else:
        count=3

    for j in range(count,0,-1):
        dial[chr(alpha)]=i+1
        alpha+=1

#print(dial)

result=0

for i in word:
    result+=dial[i]

print(result)
