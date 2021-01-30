###프로그래머스
###2019 카카오 개발자 겨울 인턴십
###크레인 인형뽑기 게임


def solution(board, moves):
    answer = 0 
    basket=[] #바구니 생성
    
    for i in moves:
        doll=0 #뽑히는 인형 번호
        
        for j in range(len(board)):
            if board[j][i-1]!=0:
                doll=board[j][i-1]
                board[j][i-1]=0
                break
                
        if doll!=0: #뽑히는 인형이 있다면
            basket.append(doll) #바구니 마지막에 집어 넣음 
            
            if len(basket)>=2: #바구니에 2개이상 인형이 있다면
                if basket[-2]==basket[-1]: #마지막 두개가 같을 경우 사라짐
                    basket.pop()
                    basket.pop()
                    answer+=2
    
    return answer
