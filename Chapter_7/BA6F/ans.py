# Solved
import numpy as np

def Chromosome_to_Cycle(Ch):
    ans = []
    for i in Ch:
        if i>0:
            ans.append(i*2-1)
            ans.append(i*2)
        else:
            i = -i
            ans.append(i*2)
            ans.append(i*2-1)
    a =    ' '.join([str(a) for a in ans]) 
    print(a)
    return a

# input_str = '''(+1 -2 -3 +4)'''
f = open('rosalind_ba6f.txt')
# input_str = '''(+1 +2 -3 -4 +5 -6 +7 +8 -9 +10 -11 -12 +13 -14 +15 -16 +17 +18 +19 -20 +21 -22 -23 -24 +25 +26 +27 -28 +29 -30 -31 +32 +33 +34 -35 +36 +37 +38 -39 +40 -41 -42 +43 -44 -45 -46 -47 +48 +49 -50 +51 -52 -53 -54 +55 +56 +57 -58 -59 -60 +61 +62 +63 -64 +65 +66 +67 -68 -69)'''
input_str = f.readline().strip()
s = np.array(input_str[1:-1].split(), int)

Chromosome_to_Cycle(s)
# print(s)
