### [그리디] 펜션
### codeup 4040


# 1. n, m 입력받기
n,m = map(int,input().split())


# 2.
info = [['X']*m] # 날짜를 편하게 확인하기 위해서 0번째 줄은 임의로 추가

for i in range(n):
    info.append(list(input()))


# 3. 손님이 머물 날
s, t = map(int, input().split())



# 4.

# 머물 수 있는 방들 중에서 가장 오래 머물 수 있는 날짜 구하기
def check(n):

    maxday=0

    for i in range(m):
        day=0
        for j in range(n,t):
            if info[j][i]=='O':
                day+=1
            else:
                break

        if maxday<day:
            maxday=day
    return maxday





count=-1
today=s

while today<t:
    
    stay=check(today)  # 몇 박을 지낼 수 있는가 

    if stay==0:  #stay가 0 : 더이상 머물 수 있는 방이 없다
        count=-1
        break


    count+=1
    today+=stay 

    


print(count)
            
    

    
        
