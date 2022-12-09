Symbol_to_number = {'A':0, 'C':1, 'G':2, 'T':3}

def Pattern_to_number(pattern):
    l = len(pattern)
    if(l == 0):
        return 0
    
    symbol = pattern[l-1]
    prefix = pattern[:l-1]
    return 4*Pattern_to_number(prefix) + Symbol_to_number[symbol]

pattern = 'AGT'
# pattern = 'GTAACCGGTGTCTTAAGTAG'
Pattern_to_number(pattern)
    
 
