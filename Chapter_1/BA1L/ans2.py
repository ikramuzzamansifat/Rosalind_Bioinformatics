S_to_N = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

def Pattern_to_number(pattern):
    l = len(pattern)
    if l==0: return 0
    
    return 4*Pattern_to_number(pattern[:l-1]) + S_to_N[pattern[l-1]]

pattern = 'AGT'
# pattern = 'GTAACCGGTGTCTTAAGTAG'
Pattern_to_number(pattern)
    
