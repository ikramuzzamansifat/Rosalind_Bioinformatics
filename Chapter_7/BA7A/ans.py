import networkx as nx

def dist_matrix(weighted_edge_list):
    tree = nx.Graph()
    tree.add_weighted_edges_from(weighted_edge_list)
    dist = dict(nx.all_pairs_dijkstra_path_length(tree))
    leaves = [n for n in tree.nodes() if tree.degree(n) == 1]
    return [[dist[n1][n2] for n1 in leaves] for n2 in leaves]

# n = 4
# input_txt = '''0->4:11
# 1->4:2
# 2->5:6
# 3->5:7
# 4->0:11
# 4->1:2
# 4->5:4
# 5->4:4
# 5->3:7
# 5->2:6'''.replace('->', ' ').replace(':', ' ').split()
# print(input_txt)

# weighted_edge_list = [(u,v,int(w)) for u,v,w in zip(input_txt[::3], input_txt[1::3], input_txt[2::3])]
# print(weighted_edge_list)

# dist = dist_matrix(weighted_edge_list)
# for i in dist:
#     for j in i:
#         print(j, end = ' ')
#     print()

with open('rosalind_ba7a_.txt') as f:
    n = int(f.readline().strip())
#     print(n)
    input_txt = [line for line in f]
    input_txt = ''.join(input_txt)
    input_txt = input_txt.replace('->', ' ').replace(':', ' ').split()
#     print(input_txt)
    weighted_edge_list = [(u,v,int(w)) for u,v,w in zip(input_txt[::3], input_txt[1::3], input_txt[2::3])]
#     print(weighted_edge_list)
    dist = dist_matrix(weighted_edge_list)
    for i in dist:
        for j in i:
            print(j, end = ' ')
        print()
        
    
