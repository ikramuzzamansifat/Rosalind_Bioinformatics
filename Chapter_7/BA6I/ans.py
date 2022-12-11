# Solved
import numpy as np

def Graph_to_Genome(graph):
    
    i,l = 0,len(graph)
    
    first = graph[0]
    if first == 2:
        last = 1
    else: last = 2
    genome = []
    if first != 1:
        genome.append('(+'+'1')
    else: genome.append('(-'+'1')
#     print(genome)
    for i in range(1,l,2):
        if last == graph[i]:
            
            genome.append(')')
            if i+2 < l:
                first = graph[i+1]
                if first%2 == 0:
                    last = first-1
                    genome.append('(+'+ str(first//2))
                else:
                    last = first+1
                    genome.append('(-'+ str(first//2+1))
        else:
            if graph[i]%2 == 0:
                genome.append('-' + str(graph[i]//2))
            else:
                genome.append('+' + str(graph[i]//2 + 1))
#         print(graph[i], end = ' ')
    
#     print(''.join(genome))
    return genome

# line = '''(2, 4), (3, 6), (5, 1), (7, 9), (10, 12), (11, 8)'''.split(', (')
# print(input_str, type(input_str))

f = open('rosalind_ba6i.txt')
line = f.readline().split(', (')
line[0] = line[0].replace('(', '')
# print(line)
graph = []
for i in range(len(line)):
    line[i] = line[i].replace(')', '')
    node1, node2 = line[i].split(',')
    graph.append(int(node1))
    graph.append(int(node2))
# print(graph)
# print(line)
genome = Graph_to_Genome(graph)
s = ' '.join(genome).replace(' )', ')')
s = s.replace(' (', '(')
print(s)
