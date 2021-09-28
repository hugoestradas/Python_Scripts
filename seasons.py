import numpy as np

def solution(T):
    four_split = np.array_split(T, 4)
    r=[]
    c=0
    for array in four_split:
        c=c+1
        m=(max(list(array)))
        mi=(min(list(array)))
        a=m-mi
        r.append(a)
    sol=max(r)
    c=1
    y="a"
    for x in r:
        if(sol==x & c==1):
            y="winter"
        if (sol == x & c == 2):
            y="spring"
        if (sol == x & c == 3):
            y="summer"
        if (sol == x & c == 4):
            y="autumn"
    return y

print(solution([2, -3, 3, 1, 10, 8, 2, 5, 13, -5, 3, -18]))
