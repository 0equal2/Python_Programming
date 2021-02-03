###프로그래머스
###2019 KAKAO BLIND RECRUITMENT
###길 찾기 게임


###참고 코드 출처 : https://kyome.tistory.com/111


import sys
sys.setrecursionlimit(10**6)

class Tree:
    def __init__(self, datalist):
        self.data=max(datalist, key=lambda t: t[1])
        
        leftlist=list(filter(lambda t: t[0]<self.data[0], datalist))
        rightlist=list(filter(lambda t: t[0]>self.data[0], datalist))
        
        if leftlist != []:
            self.left=Tree(leftlist)
        else:
            self.left=None
            
        
        if rightlist != []:
            self.right=Tree(rightlist)
        else:
            self.right=None
            

def search(node,postlist,prelist):

    postlist.append(node.data)
    
    if node.left is not None:
        search(node.left, postlist, prelist)
        
    if node.right is not None:
        search(node.right, postlist, prelist)
        
    prelist.append(node.data)

def solution(nodeinfo):
    answer = []
    
    root=Tree(nodeinfo)
    postlist=[]
    prelist=[]
    search(root,postlist,prelist)
    
    answer.append(list(map(lambda x : nodeinfo.index(x)+1,postlist)))
    answer.append(list(map(lambda x: nodeinfo.index(x)+1,prelist)))

    
    return answer
