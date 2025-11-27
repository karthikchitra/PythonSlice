lst = [10,20,30,40,50,60,70,80,90]
ans = lst[1:8:1]
print(ans)

ans = lst[1:8:2]
print(ans)

ans = lst[1:8:3]
print(ans)

#negative index
ans = lst[8:3:-2]
print(ans)

ans = lst[8:3:-1]
print(ans)

#reverse
ans = lst[::-1]
print(ans)

# start value big undali and negative ichhinappudu
ans = lst[len(lst)::-1]
print(ans)

# half on the list will be come 
lst1 =[10,20,30,40,50,60,70,80]
half = len(lst1)//2
print(lst1[:half])

