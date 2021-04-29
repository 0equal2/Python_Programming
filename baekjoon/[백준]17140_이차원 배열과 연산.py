###백준 #17140
#이차원 배열과 연산

#R연산
def r_sort(a):
    max_c=0
    
    for i in range(100):
        #temp=[k,v]=[숫자,count]
        temp=dict()

        for j in range(100):
            if a[i][j]!=0:
                temp[a[i][j]]=temp.setdefault(a[i][j],0)+1

        #temp 정렬
        temp=sorted(temp.items(), key=lambda t : (t[1],t[0]))
        temp=list(map(list,temp))


        #a[i]를 업데이트
        count=0
        for k in range(len(temp)):
            
            for v in range(len(temp[k])):
                a[i][count]=temp[k][v]
                count+=1

                if count>=100:
                    break
            if count>=100:
                break

        if max_c<count:
            max_c=count
            
        for k in range(count,100):
            a[i][k]=0

    return max_c



#C연산
def c_sort(a):
    max_r=0
    
    for j in range(100):
        temp=dict()

        for i in range(100):
            if a[i][j]!=0:
                temp[a[i][j]]=temp.setdefault(a[i][j],0)+1

        #temp 정렬
        temp=sorted(temp.items(),key=lambda t:(t[1],t[0]))
        temp=list(map(list,temp))

        #a[j]를 업데이트
        count=0
        for k in range(len(temp)):
            for v in range(len(temp[k])):
                a[count][j]=temp[k][v]
                count+=1

                if count>=100:
                    break
            if count>=100:
                break
        if max_r<count:
            max_r=count
            
        for k in range(count,100):
            a[k][j]=0


    return max_r


#1. r,c,k 입력
r,c,k=map(int,input().split())

#2. A 입력
a=[[0 for i in range(100)] for j in range(100)]

for i in range(3):
    info=list(map(int,input().split()))
    for j in range(3):
        a[i][j]=info[j]

        

#3.
time=0 #시간
rn=3
cn=3

while True:

    #3-1. a[r][c]==k이면 연산을 종료
    if a[r-1][c-1]==k:
        break


    #3-2. 행의 개수>= 열의 개수 : R연산
    if rn>=cn:
        cn=r_sort(a)


    #3-3. 행의 개수 < 열의 개수 : C연산
    else:
        rn=c_sort(a)

    time+=1

    #3-4. 100초가 넘으면 -1을 출력
    if time>100:
        time=-1
        break


print(time)
    
