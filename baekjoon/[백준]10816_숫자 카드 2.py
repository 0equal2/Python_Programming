### 백준 #10816
### 숫자 카드 2

from sys import stdin
from collections import Counter

#1. n입력
n=int(stdin.readline())

#2. n개의 정수
arr=list(map(int,stdin.readline().split()))

#3. m입력
m=int(stdin.readline())

#4. m개의 정수
find=list(map(int,stdin.readline().split()))


#5. counter 함수 활용
count=Counter(arr)
#print(count)


print(' '.join(str(count[x]) if x in count else '0' for x in find))
        
        
    
