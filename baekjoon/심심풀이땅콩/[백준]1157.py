###[백준]1157

s=input().lower()

#print(s)


info=dict()

for i in s:
    info[i]=info.setdefault(i,0)+1


#print(info)
#print(max(info.values()))

maxcount=max(info.values())
key=''
count=0

for i in info.keys():
    if count>=2:
        break
    if info[i]==maxcount:
        key=i
        count+=1

if count==1:
    print(key.upper())
else:
    print('?')
        
