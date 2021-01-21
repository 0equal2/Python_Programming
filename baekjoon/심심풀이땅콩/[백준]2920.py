###[백준]2920


info=list(map(str,input().split()))

info="".join(info)

if info=="12345678":
    print("ascending")
elif info=="87654321":
    print("descending")

else:
    print("mixed")
