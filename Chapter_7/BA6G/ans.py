# Solved
import numpy as np

def Cycle_to_Chromosome(Cy):
    ans = []
    for i in range(0,len(Cy),2):
#         print(Cy[i]//2, Cy[i]/2, Cy[i]//2 == Cy[i]/2)
        if Cy[i]//2 == Cy[i]/2:
            ans.append('-'+str(Cy[i]//2))
        else:
            ans.append('+'+str(Cy[i]//2 + 1))
    print('(' + ' '.join(ans) + ')')
    
# input_str = '''(1 2 4 3 6 5 7 8)'''
f = open('rosalind_ba6g.txt')
input_str = f.readline().strip()
s = np.array(input_str[1:-1].split(), int)
# print(s)
Cycle_to_Chromosome(s)
