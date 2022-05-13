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
#고수의 힌트로 패스한 2트 풀이
# -

import copy
T = int(input())
for test_case in range(1, T + 1):
    num = input()
    mmin,mmax = int(num),int(num)
    num = list(num)
    
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if i==0 and int(num[j])==0:
                continue
            tmp_min = copy.deepcopy(num)
            if tmp_min[i] >tmp_min[j]:
                tmp_min[i],tmp_min[j] = tmp_min[j],tmp_min[i]
                tmpmin = int("".join(tmp_min))
                mmin = min(mmin,tmpmin)
            
            tmp_max = copy.deepcopy(num)
            if tmp_max[i] <tmp_max[j]:
                tmp_max[i],tmp_max[j] = tmp_max[j],tmp_max[i]
                tmpmax = int("".join(tmp_max))
                mmax = max(mmax,tmpmax)

    print("#%d" %test_case, mmin,mmax) 


# +
##1트에 런타임에러난 내 풀이

# +
import copy
t = int(input())
for _ in range(t):
    num = list(input())
    
    for n,i in enumerate(num):
        num[n] = int(i)
    sort_n = copy.deepcopy(num)
    sort_n = sorted(sort_n)

    mmax = copy.deepcopy(num)
    mmin = copy.deepcopy(num)
        
    for i in range(len(num)):
        if num[i] != sort_n[len(num)-i-1]:
            for j in range(-1,-1*len(num),-1):
                if num[j] == sort_n[len(num)-i-1]:
                    idx = j
                    break
            mmax[i],mmax[idx] = mmax[idx],mmax[i]
            break
            
    if 0 in num:
        for j in sort_n:
            if j !=0:
                m = j
                break
        if m != mmin[0]:
            idx = num.index(m)
            mmin[0],mmin[idx] = mmin[idx],mmin[0]
        else:
            sort_n.remove(m)
            print(sort_n)
            print(mmin)
            for i in range(1,len(num)):
                if num[i] != sort_n[i-1]:
                    for j in range(i+1,len(num)):
                        if mmin[j]==sort_n[i-1]:
                            idx = j
                            break
                    mmin[i],mmin[idx] = mmin[idx],mmin[i]
                    break
    else:
        for i in range(0,len(num)):
            if num[i] != sort_n[i]:
                idx = num.index(sort_n[i])
                mmin[i],mmin[idx] = mmin[idx],mmin[i]
                break
    a = int("".join(str(e) for e in mmax))
    b = int("".join(str(e) for e in mmin))
    print(b)
    print(a)

        

# +
##고수풀이

# +
T = int(input())
 
for t in range(1, T + 1):
    N = int(input())
    strN = str(N)
    number_list = [N]
    for i in range(len(strN) - 1):
        for j in range(i + 1, len(strN)):
            arrN = [*strN]
            temp = arrN[i]
            arrN[i] = arrN[j]
            arrN[j] = temp
            if arrN[0] != '0':
                number_list.append(int(''.join(arrN)))
 
    print(f'#{t} {min(number_list)} {max(number_list)}')

# +
T = int(input())
 
for k in range(T):
    N = list(input())
 
    check = 0
    for i in range(len(N)):
 
        min_val = N[i]
        for j in range(i, len(N)):
            if (min_val >= N[j]) and not (i == 0 and N[j] == '0'):
                min_val = N[j]
                idx = j
 
        if N[i] != min_val:
            if (i == 0 and min_val != '0') or (i != 0):
                print("#" + str(k + 1), end=" ")
                for j in range(len(N)):
                    if j == i:
                        print(N[idx], end="")
                    elif j == idx:
                        print(N[i], end="")
                    else:
                        print(N[j], end="")
 
                check = 1
                break
 
    if not check:
        print("#" + str(k + 1), end=" ")
        for j in range(len(N)):
            print(N[j], end="")
 
    print(" ", end="")
    check = 0
    for i in range(len(N)):
 
        max_val = N[i]
        for j in range(i, len(N)):
            if (max_val <= N[j]) and not (i == 0 and N[j] == '0'):
                max_val = N[j]
                idx = j
 
        if N[i] != max_val:
            if (i == 0 and max_val != '0') or (i != 0):
                for j in range(len(N)):
                    if j == i:
                        print(N[idx], end="")
                    elif j == idx:
                        print(N[i], end="")
                    else:
                        print(N[j], end="")
                check = 1
                break
 
    if not check:
        for j in range(len(N)):
            print(N[j], end="")
 
    print()

# +
import copy
 
T = int(input())
 
for test_case in range(1, T + 1):
    N = input()
    Min = int(N)
    Max = int(N)
     
    N = list(N)
 
    for i in range(len(N)):
        for j in range(i+1,len(N)):
             
            if (i==0)&(int(N[j])==0):
                continue
                 
            # 최솟값 찾기
            tmpN_Min = copy.deepcopy(N)
            if tmpN_Min[i] > tmpN_Min[j] :
                temp = tmpN_Min[i]
                tmpN_Min[i] = tmpN_Min[j]
                tmpN_Min[j] = temp
                tmpMin = int("".join(tmpN_Min))
                #print("Min ",Min," tmpMin ",tmpMin)
                 
                if Min > tmpMin:
                    Min = tmpMin
             
            tmpN_Max = copy.deepcopy(N)
            # 최댓값 찾기
            if tmpN_Max[i] < tmpN_Max[j] :
                temp = tmpN_Max[i]
                tmpN_Max[i] = tmpN_Max[j]
                tmpN_Max[j] = temp
                tmpMax = int("".join(tmpN_Max))
                 
                if Max < tmpMax:
                    Max = tmpMax
     
     
    print("#"+str(test_case)+" "+str(Min)+" "+str(Max))
