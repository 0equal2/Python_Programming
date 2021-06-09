###백준 #1475
###방 번호

import math

#1. room
room=list(map(int,input()))

#2.
check=[0 for i in range(9)]


#3. 9sms 6으로 변환하여 체크
for x in room:
    if x==9:
        x=6

    check[x]+=1


#4.
check[6]=math.ceil(check[6]/2)

#5.
print(max(check))
