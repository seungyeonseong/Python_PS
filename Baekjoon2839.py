# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
t = int(input())

for _ in range(t):
    k = int(input()) #k층 n호
    n = int(input())
    total = []
    
    for i in range(0,k):
            li=[]
            for j in range(1,n+1):
                li.append(j)
            total.append(li)
    #print(total)
    #print("\n\n")
    
    for i in range(1,k):
        for j in range(1,n):
            summ = 1
            for m in range(1,j+1):
                summ += total[i-1][m]
            total[i][j] = summ
   # print(total)
    
    print(sum(total[k-1]))

# +
n = int(input())

five = 0
three=0
if n%5==0:
    five +=(n//5)
    print(five)
elif (n%5)%3==0:
    five +=n//5
    three +=(n%5)//3
    print(five+three)
    
elif n%3 ==0:
    three += n//3
    print(three)
else:
     i in range((n//5),-1,-1):
            j in range((n%i)//3,-1,-1):
                if i*5+3*j == n:
                    print(i+j)
                
            
# -

#11=5*1 +3*2
#18=5*3 +3
#21 =5*3+3*2
print((11%5)%3)

# +
li=[]

for i in range(0,100):
    for j in range(0,100):
        li.append((5*i+3*j,i+j))
print(li)

# +

n =int(input())
cnt = 0
for i in range((n//5),0,-1):
    for j in range((n%(5*i))//3,-1,-1):
            if i*5+3*j == n:
                cnt = i +j
                print(cnt)
if cnt == 0 and n%3==0:
    print(n//3)
else:
    print(-1)

# +
sugar = int(input())
bag=0
while sugar >=0:
    if sugar%5 ==0:
        bag += sugar//5
        print(bag)
        break
        
    sugar -= 3
    bag += 1
    
else:
    print(-1)

# -

# # 
