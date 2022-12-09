Number_to_Symbol = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
def Number_to_Pattern(index, k):
    if k==1:
        return Number_to_Symbol[index]
    
    q = int(index/4)
    r = index%4
    return Number_to_Pattern(q,k-1) + Number_to_Symbol[r]

# index,k = 45,4
index,k = 7010,8
print(Number_to_Pattern(index,k))
    
