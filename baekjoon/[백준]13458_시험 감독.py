### 백준 #13458
### 시험 감독

#1. 시험장의 개수 : n
n=int(input())

#2. 각 시험장에 있는 응시자수 : a
a=list(map(int,input().split()))

#3. 총감독관, 부감독관 감시 응시자 수 : b,c
b,c=map(int,input().split())


#4. 필요한 감독관 수의 최솟값
count=0


#5.
for person in a:
    #5-1. 총감독관 감시
    count+=1
    person-=b

    #5-2. 부감독관 감시
    if person>0:
        count+=person//c

        if person%c>0:
            count+=1

print(count)
