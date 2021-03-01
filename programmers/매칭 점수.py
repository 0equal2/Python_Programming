###프로그래머스
###2019 KAKAO BLIND RECRUITMENT
###매칭 점수 


def solution(word, pages):
    answer = 0
    
    word=word.lower() # 찾는 단어는 대소문자 구분이 없기때문에 소문자로 변환
    
    connection=dict() # key,value: key를 링크하는 사이트를 value 
    outlink=dict() # key,value: key가 링크하고 있는 사이트 개수 (외부 링크수)
    score=dict() # key,value: key가 포함하고있는 word의 수 (기본 점수)
    
    #=========================================================================
    
    for html in pages:
        #1. html '\n'으로 parsing
        html=html.split('\n') 
        
        #2. head 분리 
        head=html[html.index('<head>')+1:html.index('</head>  ')]
        #print(head)
        
        #3. 자신 url 구하기
        myurl=''
        for url in head:
            if '<meta property="og:url" content="' in url:
                myurl=url[url.index('<meta property="og:url" content="'):]
                myurl=myurl[myurl.index('https'):]
                myurl=myurl[:myurl.index('"')]
                break
        
        #connection, outlink 초기화
        connection[myurl]=connection.setdefault(myurl,[])
        outlink[myurl]=outlink.setdefault(myurl,0)
        
        
        #4. body 분리
        body=html[html.index('<body>')+1:html.index('</body>')]
        
        
        #5. 기본 점수와 외부 링크 수 구하기
        count=0 #기본 점수(포함하고있는 word의 개수)
        
        for text in body:
            text=text.lower()
            
            w=''
            
            while '<a href="' in text:
                before=text[:text.index('<a href="')]
                
                # text 부분은 word 탐색
                for x in before:
                    if x.isalpha():
                        w+=x
                    else:
                        if w==word:
                            count+=1
                        w=''
                if w==word:  
                    count+=1
                w=''
                
                # 외부링크 <a href= ~ > 구하기
                text=text[text.index('<a href="')+9:]
                link=text[:text.index('"')]
                text=text[text.index('"'):]
                
                connection[link]=connection.setdefault(link,[])+[myurl] 
                outlink[myurl]+=1 # 외부 링크 개수 +1
            
            # 남은 text 부분은 word 탐색
            for x in text:
                if x.isalpha():
                    w+=x
                else:
                    if w==word:
                        count+=1
                    w=''
            if w==word:
                count+=1
            w=''
        
        #6. myurl의 기본 점수 기록
        score[myurl]=count
    
          
    #7. 링크 점수, 매칭 점수 구하기
    maxscore=0
    i=0 #인덱스 번호
    
    for key,value in score.items():
        linkscore=0 #링크 점수
        
        for link in connection[key]:
            if outlink[link]!=0:
                linkscore+=score[link]/outlink[link]
                
        matchscore=value+linkscore
        
        if maxscore<matchscore:
            maxscore=matchscore
            answer=i
        i+=1
        
    return answer
