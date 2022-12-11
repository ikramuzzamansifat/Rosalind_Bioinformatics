# Solved 
import numpy as np

def breakpoints(p):
    ans = 0
    for i in range(len(p)-1):
        if p[i]-p[i+1] != -1:
            ans += 1 
    print(ans)
    return ans

# input_str = '''(+3 +4 +5 -12 -8 -7 -6 +1 +2 +10 +9 -11 +13 +14)'''
f = open('rosalind_ba6b.txt')
input_str = f.readline().strip()
s = input_str[1:-1]
p = np.array(s.split(), int)
# print(len(p), p[0])
p = list(p)
p = [0] + p + [len(p)+1]
# print(p, len(p))
breakpoints(p)
