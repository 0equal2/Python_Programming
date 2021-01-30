###프로그래머스
###2020 카카오 인턴십
###키패드 누르기


def solution(numbers, hand):
    answer = ''
    
    #1. *, 0, #은 10, 11, 12로 생각
    #2. 현재 왼손, 오른손 위치
    left=[3,0]
    right=[3,2]
    
    #3. 번호 누르기 
    for i in numbers:
        #4. 0번을 누르는것은 11을 누른다고 생각 
        if i==0:
            i=11
        button=[(i-1)//3,(i+2)%3] #버튼의 위치
        
        #5. 1,4,7을 눌러야 하는 경우 'L'
        #6. 3,6,9를 눌러야 하는 경우 'R'
        if i==1 or i==4 or i==7:
            left=button
            answer+='L'
        elif i==3 or i==6 or i==9:
            right=button
            answer+='R'
        else:
            
            #7. 2,5,8,0(10)인 경우 가까운 손이 누름
            #ld: 왼엄지와 거리, rd:오른엄지와 거리
            ld=abs(left[0]-button[0])+abs(left[1]-button[1])
            rd=abs(right[0]-button[0])+abs(right[1]-button[1])
            
            
            if ld<rd:
                left=button
                answer+='L'
            elif ld>rd:
                right=button
                answer+='R'
            else:
                #8. 거리가 같으면 오른손잡이는 오른손, 왼손잡이는 왼손
                if hand=="left":
                    left=button
                    answer+='L'
                else:
                    right=button
                    answer+='R'
    
    
    return answer
