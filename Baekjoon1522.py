x = input()

a_cnt = x.count("a")
ans = len(x)
# for i in x:
#     if i == "a":
#         a_cnt += 1
for i in range(a_cnt-1,len(x)):
    ans = min(ans, x[i-a_cnt+1:i+1].count("b"))

for i in range(0,a_cnt-1):
    ans = min(ans,(x[i-a_cnt+1:]+x[:i+1]).count("b"))

print(ans)



