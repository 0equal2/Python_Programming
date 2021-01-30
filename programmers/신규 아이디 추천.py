### [프로그래머스]
### 2020 KAKAO BLIND RECRUITMENT
### 신규 아이디 추천 


def solution(new_id):
    answer = ''
    
    #1. 대문자를 모두 소문자로 치환
    new_id=new_id.lower()
    
    #2. -,_,. 빼고 다 제거
    temp=''
    for i in new_id:
        if i=='-' or i=='_' or i=='.' or i.isalpha() or i.isdigit():
            temp+=i
            
    new_id=temp
    
    #3. .가 2번 인상 연속되면 하나로 치환
    temp=''
    check=0 #.이 나오면 1로 바꿈
    for i in new_id:
        if i=='.':
            if check==0:
                temp+='.'
                check=1
        else:
            check=0
            temp+=i
    new_id=temp
    
    #4. .이 처음이나 끝이면 제거
    if len(new_id)>0:
        if new_id[0]=='.':
            new_id=new_id[1:]
    if len(new_id)>0:        
        if new_id[-1]=='.':
            new_id=new_id[:-1]
    
    #5. new_id가 빈 문자열이면 'a'를 대입
    if new_id=='':
        new_id='a'
        
    #6. new_id가 16자 이상이면 15개의 문자만 남기고 맨뒤 .이면 제거 
    if len(new_id)>=16:
        new_id=new_id[:15]
        if new_id[-1]=='.':
            new_id=new_id[:-1]
        
    #7. new_id가 2자리 이하면, 길이가 3일 될 때까지 마지막 문자를 붙여준다
    while len(new_id)<3:
        new_id=new_id+new_id[-1]
    
    
    
    answer=new_id
            
        
    return answer
