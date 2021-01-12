### 그리디 최소대금
### CodeUp 2001



# 파스타 가격
pasta=[]

for i in range(3):
    pasta.append(float(input()))



#print(pasta)



# 생과일쥬스 가격
juice=[]

for i in range(2):
    juice.append(float(input()))



#print(juice)




# 각 최소 대금 구하기

result=(min(pasta)+min(juice))*1.1

print(format(result,".1f"))
