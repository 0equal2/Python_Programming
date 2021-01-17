###[정렬] 성적이 낮은 순서로 학생 출력하기
###이것이 취업을 위한 코딩 테스트다 with 파이썬

#1. n
n=int(input())

#2.
arr=dict()

for i in range(n):
    info=list(map(str, input().split()))
    arr[info[0]]=int(info[1])


print(arr)


#3. 딕셔너리 정렬


#value값 기준으로 아이템 정렬
arr= sorted(arr.items(), key=lambda k:k[1])
print(arr)
