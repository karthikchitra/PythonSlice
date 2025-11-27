lst = [10,20,30,40,50,60,70,80,90]
# syntax
#lst[start:end:step]
ans = lst[2:6]
print(ans)
ans = lst[0:3]
print(ans)
ans = lst[:3]
print(ans)

ans = lst[5:-1]
print(ans)

ans = lst[5:len(lst)]
print(ans)

ans=lst[:]
print(ans)