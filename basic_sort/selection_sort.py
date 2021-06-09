## 선택 정렬
## selection sort


def selection_sort(arr):
    
    for i in range(len(arr)-1):
        
        #1. i위치에 올 제일 작은 수를 고른다.
        index_min=i
        
        for j in range(i+1,len(arr)):

            if arr[j]<arr[i]:
                index_min=j


        #2. 제일 작은 수(arr[j])와 i위치 원소(arr[i])와 바꾼다.
        temp=arr[i]
        arr[i]=arr[index_min]
        arr[index_min]=temp
        
        
        
    
arr=list(map(int,input().split()))
selection_sort(arr)
print(arr)
