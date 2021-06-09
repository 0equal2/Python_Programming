###백준 #4673
### 셀프 넘버


#1. 셀프 넘버인지 check
def search(x,check):

    #1-1. x의 각 자리의 숫자 리스트
    y=list(map(int,str(x)))

    #1-2. 새로운 x
    n_x=x+sum(y)

    if n_x<=10000 and check[n_x]==0:
        check[n_x]=1
        search(n_x,check)

    else:
        return 0



#2. 출력
check=[0 for i in range(10001)]

for i in range(1, 10001):
    if check[i]==0:
        print(i)
        search(i,check)



