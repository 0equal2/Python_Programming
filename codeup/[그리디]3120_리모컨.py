### 그리디 리모컨
### CodeUp 3120


### 조절하면서 온도가 0과 40을 벗어나도 된다. 



#더하기 빼기 함수
def cal10(n,t):

    if n<=t:
        return n+10
    else:
        return n-10

def cal5(n,t):
    if n<=t:
        return n+5
    else:
        return n-5

def cal1(n,t):
    if n<=t:
        return n+1
    else:
        return n-1
    



# 현재 온도, 목표온도
now,target=map(int,input().split())

#
count=0



while True:
    #print(now,target,count)

    # 현재온도와 목표온도가 같으면 break
    if now==target:
        break

    
    # 차이가 10도가 나면 10을 더하거나 빼거나
    if abs(target-now)>=10:
        now=cal10(now,target)
        count+=1
        continue

    # 차이가 5보다 클경우 10계산과 5계산중에 효율적인것을 택
    elif abs(target-now)>=5:
        new1=cal10(now,target)
        new2=cal5(now,target)

        if abs(target-new1)<abs(target-new2):
            now=new1
        else:
            now=new2
        count+=1
        continue

    # 차이가 5보다 작을경우 5계산과 1계산중에 효율적인것을 택
    else:
        new1=cal5(now,target)
        new2=cal1(now,target)

        if abs(target-new1)<abs(target-new2):
            count+=abs(target-new1)+1
        else:
            count+=abs(target-new2)+1

        break


print(count)
        
        

        
