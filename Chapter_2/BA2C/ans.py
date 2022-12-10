# Solved 

def compute_probability(profile, kmer):
    prob = 1
    for i in range(len(kmer)):
#         print(profile[0][i])
        if kmer[i] == 'A':
            prob *= profile[0][i]
        elif kmer[i] == 'C':
            prob *= profile[1][i]
        if kmer[i] == 'G':
            prob *= profile[2][i]
        elif kmer[i] == 'T':
            prob *= profile[3][i]
#     print(prob)
    return prob

def profile_most_probable_kmer(dna,k,profile):
    d = {-150.05: 'AAAAA'}
    mx = -150.05
    for i in range(len(dna)-k+1):
        temp = compute_probability(profile,dna[i:i+k])
        if(temp > mx):
            mx = temp
            d[temp] = dna[i:i+k]
#             print(dna[i:i+k])
#     print(mx,d[mx])
    print(d[mx])
    return d[mx]

with open('rosalind_ba2c.txt') as f:
    dna = f.readline().strip()
    k = int(f.readline().strip())
#     k = 5
    profile = [[float(l) for l in line.strip().split()] for line in f]
    profile_most_probable_kmer(dna,k,profile)

#     input
# problem link: https://rosalind.info/problems/ba2c/
'''ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT
5
0.2 0.2 0.3 0.2 0.3
0.4 0.3 0.1 0.5 0.1
0.3 0.3 0.5 0.2 0.4
0.1 0.2 0.1 0.1 0.2'''
    #     print(profile)
#     kmer = 'ACGTT'
#     compute_probability(profile, kmer)
    
