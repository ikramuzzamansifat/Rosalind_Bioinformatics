# Solved
import numpy as np

def Chromosome_to_Cycle(Ch):
    Cycle = []
    
    for i in Ch:
        if i<0:
            i *= -1
            Cycle.append(2*i)
            Cycle.append(2*i-1)
        else:
            Cycle.append(2*i-1)
            Cycle.append(2*i)
#     print(Cycle)
    return Cycle

def colored_edge(genome):
    edges = []
    for ch in genome:
        cycle = Chromosome_to_Cycle(ch)
#         print(cycle)
#         edges.extend((a,b) for (a,b) in zip(cycle[1::2], cycle[1::2]))
        cycle.append(cycle[0])
        for (a,b) in zip(cycle[1::2], cycle[2::2]):
#         for a in cycle:
#             print(a,b)
            edges.append((a,b))
#     print(edges)
    return ', '.join(str(e) for e in edges)
    

# input_str = '''(+1 -2 -3)(+4 +5 -6)'''.split(')')
# print(input_str)
f = open('rosalind_ba6h_.txt')
input_str = f.readline().split(')')
genome = []
# print(input_str,len(input_str))
for i in input_str:
    genome.append(list(np.array(i[1:].split(), int)))
    
# genome = [[+1, -2, -3], [+4, +5, -6]]
genome.remove([])
# print(genome)
# print(type(genome[0]))
print(colored_edge(genome))
