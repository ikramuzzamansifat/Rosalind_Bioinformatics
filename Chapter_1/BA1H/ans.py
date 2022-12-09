# Problem link: https://rosalind.info/problems/ba1h/

from collections import Counter

def Hamming_Distance(s1,s2):
    ans = Counter(i!=j for i,j in zip(s1,s2))
    return ans[1]

def Approx_occurance(pattern, text, d):   # d = no. of allowed mismatches
    t,p = len(text), len(pattern)
    occur = []
    i = 0
    while i < t-p+1:
        if(Hamming_Distance(text[i:i+p], pattern) <= d):
            occur.append(str(i))
        i += 1
    return ' '.join(occur)

pattern = 'ATTCTGGA'
text = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC'
d = 3

# Debug dataset 
# pattern = 'AGTATCGCCG'
# text = 'TACAACCTTTGACCGCGCGGAGTTTTTTAGCTCCTTGAACTGCACATCCTCAAATCACTATAGTGTTGGCTAACCACTAGGCTCAAGAGATACATGTATGAGCCCCAGTATATGCGATAATCAGCCTTCGCAATGAGCCGCGCCCCTTGAATTTGTTTCACTGTTAGTTAATTATTAACTTCCAGTCTCCCGAGTGGAGGCCAAACTGCCCGCTCACGCTAGGGTGCGTAACCAAACATGGTTAAACAATGCCGATACAGAGCAATGCTGGAGCCCCTGAGTAGCCGCTTTCGCCAGTCTGCCGGGGGTCTCGGTCGAGTCAACCACCACACCTATGGCCTCACCAGACTGGGGCTATACCCTACCAATCCACCGTTTGTGCACAAAGCCTCTTACGAAAATGCCATTTAACGCTTTGACCAGTTTCAAGATGCACGATCTCGCTTGAGAGGTGTCATCCATACTATGTAACGCCGGGATGATTTGCTACTATCAACTTCAATTCCTAGAGAAGTTCTAAAGGCTGAGCAAATTTACCGCGACTAGCTTAGTTGCGACCCACGACTGTCGTGACGAACAACTGCGACTACCATCGCGCCACGTCAGTAGGCGTCGGGGGGAGGGATCGTTAGATGCACGTTGCTACGAGCTTTCTGCGAAAAGACCCTATAAGTTCCTAGTATCGGCGTTAGCTTTGTGTCCGACCAGGGCGCCTGGCCATCACGTAACGCCTACATTAAAACGAGCGTGGGGAGAGGGATACTTGGCTAAATTCAGTACCGTACTTCGGTTGCATATTGTGGGCGTCATATACTAGACCACAAGCCAGTGATACCCACCGCCCGACAAGGATTACCAGACATCAGTGCCTACTAAATCCAGCAGTGATCCATTTGCTCCCCGGGACAACCAGACGACGTCGCGTCTGCGAATATTGAATTGTACGGGCTTAGTAGTCGATAAACTGTGTGGGAACGCAGCACCTAACGTATTAATAGCCCCGCTATCGCTCTCGACTTCGTCAAAAACATTACGGGATTCCGAGTTAAAGTAGGCTCGTTGGGGACAGGATCGACGCAAAAAGGGGTATTGACGTATGCGTAGCTTGCTGGCATCGATATGAGAACTTGCTACGAATACCTCCAGTCAGTACCCAGCAGCAATTAATGCACTTCCTTCAGAAGCGCTCGGTGTGCAGATGGAAGTCTTACATCGTGGCACGGATCGACTGTCGTCAATGCCAAGCGGGGCAACCATCTAAAAGACATGCTGATCGCTATTGGCAAATCCGGTTCTACTGTACGTCCTGGACCACCATGCGCCGTAAAGACGCGCTCATATGCAATAAGGCTTTGTGGGATGGTACATGTTAGCCGGCTCGCCGAAAGGGGCGAATGAATTCCGGTTCCACCGCCTTTTGTGCGAAACATCAGTTGGGGCCCGCGGGCTTACCCCCCGTGCGATCTAAAGTATACCATCGCAAAAGCTTCGAACTCCTATGTAGGTTATAAGGCCTCATGCTCCTTGAGACTCGTCGGCCTGCTCACGTTTGGTCAACATGCCTAGTTGGGTTTATGTTACCTAAACCAGGCGCCTGTTGAGGAGCTCGATGGATGAGAAACTTTTCAATGGAACAGATGTATAAATCCCAACTAATAACAACACCTTTCTCTCTTTGGACAACCCCTTGCTACGGGTCTCTACTGACCAAGGATTGACCTAAGTGCAACACATCGTTAGAACTGAGAGAGTGTTGTGCCGTCAACTAAGATTACTTAGAAACTTCTAGGACGTTCTATACAACCGATGGTGGGCTGAGTTGCCTTATCACACTCATGCTTGCGTACGGGTCACCCCATCCTATGCGCGACGGGTTGTTTCGCAAAAGCTGCGCCTGGAGCGCTATTAACTATTCGTGGGGATCCGGTATTTAGTGCGAAGGGCAGCCACGCCATCGTACAAGAAACATACGTTCGGAGCTATTCCAAGTCCGTCACACCGGAAAGTGGAATCGCTGTATCTGTGTAAAAATATGGCGGTGTTCTATGCAGACGGTGATTCGGAGAGGCTTCATTTTATTTCGGCCAGATAAACAACGAATTTCGGGGTAAGCGGCGTATTATTTATAGGAGTTGGATTGGGTGTCTTGGCCCAGGTTGTCGTGATTGCATTAATACATATGAATAAAGGCAAAGAATTTTATGTCCCCCTCGCTGCGGAAGCCGAACCACGGCCTTAACACCAACAGAGAATCGCGAGTGGTGCCACGGCTTATAGAGCACCCTAACTTTGACTAGTGTAATAACTGCCAGCTGTATCGAGATGGACGAGGGTTAAGGCTATGAACAATGTAAGACTCTCCATTATAAGCTCTTAATTCTTCATATCACCCCTGGGCCGTATCAAGAGTTACTGGCTCCATGTTCACTTCCGATGTTGAGCTGCTGACGAAGTGGCCTGTTCTTTCCAAGACGTCAGTTTAGGTTGGCACCTCCTGTTACCAGAGGCATTCAACGTATTGGTGAAGCGGCACGACGCTTGGTTGGACCTAAACTGACTTCTGTCGTCTAAGCTGTCATGCCTTGTTCCCTTACCCGTGTTACTTCGCATGACTCTAATGACTTATAGGACTAGGTGTGTAGCTCCCCTCCGCGCGAATTTGCTACCTTGCAAAATAAGGTAGTAGGATCCTTCGAAAAGAGCTTTGTATGATAGAGGCCTGGGGTAATCTAAGATACTTTGAAAACAGGGCGATTTTGGCAGACACTAACAAAAAGTAGATGCCTAAATGCGGTCGGACGTCTAACACAAATTTAGTCTCACCCACTGTGCACCGTGATTAGTATGCCGCCCACCGGCACGGATGTGATTGCCCGACAGCCTGAAACTTATGCCTATCTACTAGGACGACCACATCCCTCATACAGCAGTCCTCAAACTGAGAACTAGGTGTTCGAAGAGAATGTGTTGAAAATCTAGGCCTCCAGTTATTGGTTGGTAGGCATTTTGCAGCCAGTGCACGAAGAAAGCCTCTGATGTTTATGAGGTATTGGACAGTACAAGACACCCTCTTGGCTATCTCGTCAGCGCCAGTAAAAGTCACGTTTAGGTGCACTCATATCAATCAGCAAGAGCGAACGGACGGATCTGGGCCTTGAAATCGACCGATAAGCACTACGGACCCTTCAACAAATCTTGAGGTGACTCACCGTTGCGGTAGGAAAATGCTTGGAGGGGGGTTATGGCACAGTCGCTCAGTCTGTTAGCTTCTTACCGCCTGGTTGCAGCCTTTGTCAGTAAAGTCAGACCTGTCCTTAAACTGAACATTCGGTCGTCTGTCGACGCCATGTATCAGTTTAATTTGTTTAGAGAAGCAGCTGTCGACAACACGCAGGTAATGTTAGCCTGTGCGCATAGTCGTTAACATTTCCGATATTTCCGTGTGGATACAACTCTTTGACATCCACTGACCACTATCGGGAACCGATCTAGGGCTATAGTCTGCCGCTTAAGGCATTCAGCCGTCATCTTGATAGCCACTTGGTTACGATACCCTGGCTAATTACTTGTTAAGTTATATCGAGGGATCAGTTGCTAGGCTTCGTCGGTTGCGCTGAGCCATAGGCGTGATATTCACTGATGCTGGCGCTAGGCGAAGCAATCAACAAATGTGATGCCTCTTTTGCTAACTGGGACTAGTTTTCGACATGCCGTAACAGCGTACCCTCTTTCGTTTTCACTAATGCCTCTACGCGACACCCTTCGGACTCTTCTAGCTCCAACAGTGGGCTCGCCTACGAAACTGTCTTGACTAATATTACTGCGATGTGCAGCTGCCAGTATAACTACTCCATAACGTATCCCGAATCAGAGTTACATGGCCACTCAGCCCCTTTGCCGACAGATCCAACAGGTACCCTTTATGAGGGCCTGTCATAAGTCGTAAACTCTGCTGACCCCAACGCTTCAACATCCAAATATGAAACAAACCTTGGGGCAAACTCTCCGTCTCTACGTTTTCAATCAGCCTTAAAGAACTACACGGCTTGTTACATAAGAGAAACTCATCCCCCGCTCCCAGAGACGGTGCTCACTGGGGGCCTGAGGCACCCAGTCCTGTATGCGCTGCCAGAGCCCAACTTGGTCTATGACCCTCTCAATATTTACCCATATGCTCGTCCCCAAGCGGCGAGCCGTAAGCATAGGCCACAGGGCACTCGGTAATTCACGGAAGCAACCTATTTGCAAATCTCGCCGACCTTCGCCCTAGTACAGAAGACGACTAACTGGTTTCTCTGCGTCGTCCGAATCGCCAGCCGAATACAGAAGATTAACCAGTTTACTCATGCCAAACGACAATCCCCCTAAGCGTATTGCGGAATTCTTACTAGTGCAACGTCGGTGTGGCAACGAAGGACTCTGGGCCATTTTACGACATAAGCTCCCATTATGACCTGAGATAAACTAGGTAACACTACGAAGGATCGAATGGTTTTGGCGAAGTTACCTGAAGTGGCATCAGCAAACGTCCGCCACAAAAGCATGTCCGTTCAGATAGCCTCGTATCAGATACGCGCTTCGTGGCACCAGCCGGAGCTCTAATGCATGACGACGGTAAGTTCACTACTCTGGGTCGCGCCGCAAACGAGATCGATGAATAAGTCAATGCCTCTGGACCCTACCCAATCCCAGTCACTTGGACGCTGATCCCTCTACGTAACTATAGAAGATGCGGAGGAGCCGAGTACCGTTTCAGTGGCCATTATGCTTCGGGATACAGATTAAAGTATAGGGTTGCAAGTGAGACGATCTAGGTCTTCTACCTGCCTGTCATCAGTCACTAACTCGGGTTGCTGATGGCCGAAAGAGCCCGCCCGCAAGTGGTCTTAACGACAATGTAGTCCGAACAGAATGTTGGAGTACTGGATGCTCGCACCGCGGTAGACTGCCTTTGCCGGGACCCTGCCCTACGGAGATAAGAGATGCGCCGCTGAGCTTAAATGCGTTTAGAACGCTCGACGGGAGTCACACCCATCGGTATGACCCGGCTCCCACATGATTAGTCTGGTGTAACATTTTGGCTCACTAAATTCCTGGTATATCGGGATCCGCTTGTATAGTAGCAGCCTGGACAAGTACCCCCAATAGAGAGGTGCCTCTTACTTTAGACGTAGGCGGAGCTTGTGCATACGGTACTTTGCGATGTAAATGTCTGTGTGGAATGGTAGCCGTTGCAGCATCTCGGGAAGCCAGAAAAGAGTCACACATGCATGTTCGTTTTTTTCAGAAAGATCGACGTGATGTAAGTACAGATAAGAATCCTCATACCTTACATATGCCTCTAAAGGTAAGCATGGTATCAGAGCGTAACAGTAAACACACGGTTCACTCTCTTCATCTGATTTTCACGTTGAGAGGCCTGGCCCTAGTAAGTTGCTGCAATTACCGTTTGCCTGCCGGATTCAGGCGTGTCCGGATTCAACTTCGCGCCCGGTATTTTAACGGGCCGTAGGGTCAAATGGGTCCATTTCGATCTTCCGCAACTCTGGAACCTTAACCAGGTTCTAGTATGTTTACGGCCCTACTGTCGTTCAGGATGACAGTTATCTCAAACCACCATGCGGACGCATGTCGACCCTGGGCTAATCTCAGTGCTTGAGGGCCCTGACGAACTTTACAAAGAAGTTTCGCTGAGGTACGAATCCAAAGCAGGACGACTTATTCGTACGGATTAAGCCGACGGACATAACATTGCCCTGGGGGAAGAAGATCCAACTTTCCAACGTCATTAAAGGCGTTGGGGGGCCACAGCCTCAAGGGCGGTTGTCATGGGATATATTCTATTGAAACTTGAGCAGTCTAAATGTACGTCAGCGGTGCCTTGTATCTTTGTAATTATTACACCATCTTGTTTGATTACCTATGATAGATTGAGAAACTCAATCATGACGGCGATCGCCGGAGGGGGACAGTGCTGTGGCGCCCTATAGTGCAGGGACTCTAAGCACAGTAATGGCACTAGACCCTAGCTCCTACGGGGGTTTATTGGCAAGCATAAATTCGCTTCTATTGTGCAGGCTACGAGTTTGCTTGCACGACTCTACATGTAACGAGCTCGGGAATTAACGGTACACCGGGCTACTGATTGGCAATTCAGTATTTTAGCTTCCAAAGGATCCTTATTCCATGGATGGCCACGTAATGATCCAAATGGCAACGCTCATCCGACAGATTTCTTTAATGTCCGGCGGCTGCTTACGATAAAAGTGTGACCACGCGTCGGCTCCCGGGACGAACTCCGGACCACGTCCGACTTTTTAGCGTACAGAAGGGCTGGGTCTATTAGGCATAAATAGAAGGGGTCGAGCTACCGCAGCCAATTCAACAACATCACATAACTGCTCACCGCTAGTACATTGCAATGACTCTGAATGTGACAAATTTGTCTAGACGGCTAAAAAGGTCCGACCGGCAGTCCGGAATCGCCGGAGGTAGTGTTAATAGGCCTCGAGCGCCAGCTAGAATTTAGATACTGGAGTGCTCCAGGGCAAACGAGCGCAGGTCATGACAACATAATTCTGTATCAACCTCAAATGGTGTACCCTGCCACTTAGATGAAGGACGGCTCGTTTTTGACGGGATCTGACCATTCAGGGAACCAGCATAAGCCGGTCGCCTTGAGAAGGCGCCTGGTTGGAGTAGGTCGGTTACGGTGCCGTCGACAAAATTTGTCGAGATTTTGTCTTGTTTTAGTAAAGTGAGCGGATGCAACCGGTATTAGACGTATATCGTACCCACGGCCCTGACACCCACAAACCAGGGAGCGCTTTGAGACTTCCCCGCGTCCAGGACAACTATATCCGAAACCTCTCTACGAAGCTGTAATTTCATTGGCACCAATGATGAACTACGGTTAGCTCGAAACCGAGTTGAGGCGTATTGCCTTTACGCGTTGATGATAGTGGTTCGCCCCTTCACCAAAGAGTATTCAGTATCAAGGTCGCAGTCCCCGTCCTATGCGGACAAATATGTCTTTGGGTCGCGCTCATGAACTCTCCGATTGCTACAACATGTCCCCTGGACCGGCTAGCCTGGCATATCAAGCCAACCAGTTTCCCCCGACAGGGCCGCCCAGATGAGAAGTTACATTTCTAGTGCTCCCATCGAGTAGAGGAGAGTCACCTGAACTCGGGCTGACTGAGCACGGGCTCGGTCATGTGTAGTCGGAAATTCCGGAATGGCGGATATGGTCAGTTTGGCTAAATCTCGACTCTTTGTGTAGGAAGAGTGCTCGCATCCGGTAGGCTTCTATGACGGTCTGAGAGGTCACCCTAGTGCTGCTTATGCGTTAAAGCTCAGTAACCAGATAACCTCAGGGGGGTGAAGATTTACAGACCAAGAAGTGGCCAACACACCTCAGCGTGATTATTGTGCTAGCACTAAGATAGCCGAAGTAAGCAAAAACGCAACTTCCATGCCTTATAAAGGGCAGTATTGATGTACAAATAACACTATAGGTTTGATCTAGATTTTACAAGTTGAGCCCGATTCCCTAACTCGCCACATGAGTGTAGATTGGCCGAGTTTTGGGTGCCGTACGGAGTGCATTTGTTGACCGCCCTCTACTGTAACTGTGAGGGAAGGGCGATATCCGGCCACCGGCTCCGAGCAGGCCGGTATCCCCCCCTTAAGATAAGATCACATCATGCAAAATTGCCGCGGGGGGATGTGGCAGGGGTGTCATATCCTGCTTTCGTGTGCTACAGTTCCACTAGCGTCGCCGCGCTCAGTTGGAACTAAGGTAACATGCGAACACAACTTAATCTCGTACTCCCCTGAAGAATGCTTGGTCTTAGACGAATTAGCATTAGAAACCTTGTCGTAACCAGAGTCGTTGGTTCCGGGCGCTTTCATACTAAAGTGGCGCACTTATTTCTATGCCCCCACGAAGAGATACAGCAAGCCTATTGGCCGCACTAATCTATGGTGGCATGATTACTGTTATGAAATCACCGCGTATACTGATGTCTTCTCGAGCATGACCGACCCAATCATTAGGCTAGGTCCGTCTGGTAGGGCATCGACGGCTGAGCCTTTACCATCTTGACTCTGTAGCTCGATTATCTTCCGCACAGAGGTAGTTCTTAATAATCGAAGTCCCTGCTTCCCGGAGTGGGGTTACTACTAATTCTCGTACATGAAAAAAATTAGCCGGTATATCCGTGCCCGGACTCTCTAGTTACTGCCTTGACCATGGGCAGTCGCACAAAAGTCTGCTGTTCTCCCGGCCCCTGTATCTTTCTAAGCGCAGCGAAGCTCTGCGCTGGTTCTGTATAGTAAACTACTCCCAATGCTCGTTAGGTGTCACTACCCGCGAATCGCTAACATGAGTATCTCTACCCAGTAGTCCTGGATAAGTTTGTGAACCTATAGAAATAATTCAATAGAGGGGTTGAGCACAACACGTTGCCTTTCCATAGTGCATCCGACGATCCGTAGGAAAAGCCGTGGATATAGGGAGCGTAAATAAATCAAAGCCAAAAGTCCTTAAATTCAGGAGCGTCGTTGGACCCAACTAGATAGGGCTCACAAAAAGCGCTTGGAATTGACTTACCTCGGATTCCATCAGCTCCCTTTAGAACCCCTTGTGGCCGGGGTGCTCTGCAAGGAGGGTAACAAGCATAGAAGCTCAGGCAGGGTACCTTCGTAGGACGACCCCGTGCATTACCTAAGAATTAAGCTCTTTATAGGGTTCGTATGACATCACAACAGTCGCTCATCAATCCTAGAGACCCCTGCGTCGCTTGTCCGTCGTGGAGGGATTTCTACAGTATGACCGTAATAGGACAGAACAACCAAGTGATTGTACGTTCTGGCCGTCCCCTCGTCGCTCCGCGTGAAACACCTACCAACTAGGAGCGTAAGATAATGCCCCCTCCGTTCTCAGTAACTTGACGGATGACCACGATCTAATCCGGTGTTACGTCTCGCGCAGAGCTAACCTCAACAACGAGAACACGACCCGAGGTGGTCTTGCCCCTAACTTGGGCCTACCGACGCACTGTTACCATATCTGCCAAAACCCATAAAAAGCGCCTAGCAGCGCGAATAGTCTCGCAGTACGCTGACGACGAAGATCGGTTGTTCGACCAAGGCAGATCTGTTGTTCGTCGCGTGACAAGTCACACATTCAAGGGCATGCGCCTATAACGGCTATGGTACAATTCAGCAGAGGCCGACGGATCTATGCCCCCAACGCAATTCCATTGGATTAGGGGTCCAAAAGACCCTATGGACGAAAAATCGGGTGGGTGTTCTGGACCTACAAAAATCACGGGAGGTACCTGCCTAAAAGCCTGACCCAGCTCCACCAGCGGAACGGGTACTATTGACGGCGTGATTCCCACACTTCCGGTTAATAATGTCCGCTTCTAAATCTGGGACATCGACGGTCAGCTATAACGAATTTGGCGCTGATGACATTGTTTACATTGGTATGCGGATGGGGCCTGGCTTTACAAGCATGTTGTGCTAACTTGGGTTGAAGGTCATCAGGCCGTTAGTCGAAATCGAGTGGTCTCATGTCTACTTTCCCTGTGTAGTGCGTCGTTATGTCGTCCTAGTAACACAATGCCGAGATACATGATCTTTGCCCCCAGCCCTCACGACAGCCCTGATAGAGACACGTGCTCGTGAAACCTAGTTTTTCATGACCGGAAATCCTTCAGCCGGCGGCATCTAGTAATCATAGAAAGTAGATTATATGATTTTACTGTCAGCCCCAGCGCTAGTCTCCAATGCTTATTACCAAGGTATAGTACATATCTCCAGGCGTTCAGTTCAAGTGGTAGGAACTTAAGGCGATGTCCATACAGTGAACCCTTAGGGGGAGTGAGAGTCAATAGTGCCCCCACTTGAGCGATCGCCTCAGGAACCTTGCTTGTCCTCATAAGACTTCGACCTCCGTCAGACGCGACTTCGCACATAATGGGACCCTGAGACCTGCATCTGGCTAACTTGGATGACCTGGTAGTGTAAAGGGAAAACCGTCCCGGGCGGCGGTTGCCTTGGAGGATACGTAGAGTACGTCACATGGAGCCTACTGTGTGTTTTTCTCTGGGTCTTAAAATGATCCTATCCCAGGAGACATATCATAGCATCCTGCCAACAGTGGTTAGTTCGCTACCCAAAGTATATGTCAAATATGCGGGTAGGGGAAAGTCGAGACATCGCATCTTCAATACCTGATTATTTTCGCTATACCCCTATAACTAGCGCCAGAGAATGGACGCTAGAGTCAACCCGACCATAAGGTAGATGTTTGCTTTGGATACGTCACTTTGCGAGACACTCCGACTCGAGAGTTGCGTACTCGCAAACCACCAAGCACGTCCTTATAAAGCAATTCTGACATAAGATCTTGTCACGTCCTGTTATTATATAGACAATGGATTATTCCGTTTCCCTAAACCTGTACGCCAGGCGGCTCGCTCTTTCATTATGTGGAGTCGTCCACGCGCGCACGACCGCGGCAAGCCGAAACACGTACGCGTTTTTGAGTATAGTCACGACTAACGCCTAGCGGTCTTTATAGCCCCCTCAGCTAAGGTTGAGGAGAGTGCGGCCCGAGGGAAACCGGTCAAACGGTGTACTCTTGCTACTACTAGGTATGTAACTCGAAAATCGCCCAAAAGCACCTGTTAGCAGCTGCCAGAACGGAAGGTCCGGCCACGACGGAATATAGCGTAAGTGCTTAGCTCTAAGCAGTGTAAGGCTCCGCCCGAACGTCTACGCAAGAGTAAAATTCGTAACCACCATGTGTTAACGATTACCTCCGACTAATTACATGCCGGTTATCTTCTTTCTAAACTACACGCTCCGTGCGGCAAACAGTGAACCCTTGCGTCTCAGAGCGCCGAAGATAGCTGTTTTCGTCCAGCTCTAGTCAAAGCTTAGGCATCCAATAAAATAGCCTGTCCGGGATTACAGAAATGGGACAGGAAGTTGCGCTGATAGATAATTCAGCCAAGAACTGAGTAACGCATTTGGCGTAGTTGGTCGCTGCACAACTCGGGTCACAATAATGCATCAGTTACCTCTACTCTTATCACGATAATGCGGGCGGGGTTGCCCATGCTGGCGGTTAAACCAAGGACCTTCTACTCTATTTCGTCCCAATCCTTCGCCTAGCGCTCATCCTAGGGTTGTGGACATAAAGGTGCCCAGGCGACGAGAGAATGTGACAGTATTGTTGACGGATCGTGTAAATTAATAGTTATCGTTAGGAAATGGATATAAGTGCGATCGTTAGTAAGTGCTGGAAACGCTCGCTCTACACGCTCTCCCTCTACGACACTGTTCATAAATCGGTCCGAACCAGTAAGACTCGAGTCTCTTATCAGGCGGGTTAACCCCTCGTCTCCCTACGTAGTCTTGACTCCTTGTCGGAAGGATTACTGAAGCCGCACAAAGTAGAGAGCTCCCTTCGCTCCTGGAACTCCAGCACGATTAGGAAACCTAGCTCAAATAGGCAATTTCTCTTGACACTTTTGTCCTGTTTGTCCTTTACAACCCTGAATATGCATACCTCGGAAGGGCTGATTGTCTTCCAGGCGATTGGAGACTATGAATACGATACCACAAACCGGTTCGGTGATTGGTCCGAAACAATCTGGAGGGTCGACGAATTAGCATTCTTCGAAGATCGTAGGATGAAGTGACATGGGAAGTGCGAAACAGAGACCTAATAGACTATCACTTCCTCTGAAGGCAATAGGTTCTGACTCCAGGCCGTTACCGAGGACGATAAGAAGAGAAGCCGGCCTCCCTCATTGATCAGTCGTAAGGCCATTAACACATTTTGCTGGTTAGCTTCAGTAAGAAGGTAACCTTATTCTTACGTAAATATAGTACTAATGATTGTTGGCGGTAGCCAATTGCCTTTTCACATTTACCATTTTGAGTGTTAGCCAAGAGAGGTGTTAGCGCTGAACGCTGGAAGATCCGGTTAGTTCGAATTATTGTGATGAGTGGTCCCCTATCCATCAGTCTACTTCCGTTTTTTGTACCTTCCACTCGCCGAGCGGCAAGGACTGATCTAGAATTGCAAGACATCGTTAAGCCCGAATGACCAGATTAGTTTTATGGACACTAATAACGAAGCATATGTACAGGGTTTCATGGTGAGGATAACGGAGGAAGTCCCCAGTAAAGTACAGTACAATCAACTTACGACCAGCAGACCTCCACCCCTCAAGTGAACGTATTGCAATGAAGGTTAGACAATTGTGTGACGAGCGAGATCAGTGTCCTACGTGTTAGCGGGCAGGATCTTAAACCTGGCCTCTACGCTGTTTTACGAACAGGCCACGACTTTTCGCAATGCCGTATTTCGCTAGACACGGCATTTAAGCACTCCTGGCTCCCTAATGGCATTCGTGCCCCGCCGACCAGGTGATTGGAATGTTCGTCGGTAAATATGGTCTGTAACATTAAATTCCTATAAGACACACCCGACGATGACGCTCAGCCCCTAACCTACCCATCGTGATCTGCGTGATGTAGTGATACTCAAGATGCCAGAGCAACTCGCCAGGAGGACCCATAAGAGTGACCAGAAAAAGCTTTACAATCTCCAGCAATACGAATTACCTAAATGTGCGAAATGGGCTGGGATCTCGTCCCGAAGCTTGCATTAGTGTGTAGTTACAATCTTCACCAATATGCCTCGGCCCGTTTATTCTTCCCTGAGAACCGCTCTTATCTCCCTCCAGTTAGTGCGCCGTCTCGGCCCACGTTGGATGAGGTGGTGATTTATGTGTTCGCGTCGAGATTATACTGAAGGATTCTAGTATAGCCGATTACGAGTTCCAACGTGTCGTAACGCATCAACTGATGTCTTGGGCATAGAAGACACGAACTAATCAACTCTACGAGTGTAAAGGAGGTTATGGCACCACCTTCGGTCCGTAGGAATGCAGTTAGGTGTGGTCATCACGTAAATTAGCGTCATTCTTGCTTATCTCGGAACTCCTGGCTAACCTACTACTAAAAGCAGAGGGTCGTGTGTCATTGCCCACCTAGTCATAACGACTGATCATAACAGTGTTGGTCGGCCCTCTTTAGGGAATCACTACATACACGCGTACATCTAACTTTACGATGACATGTGGAAATAATTACAATCTATTCGGGCTATACCCGCCACATAAAGGCACGTATACGAGACTTTAGAGGTTGGTCCCCCCAGTGAATCGTTGGTGCTACTCTACGTCTTATTGTCGCTCGCACCTACTAGGCCCCTGAAAATTTCATATTCCTGTAGCACCTGTTCTTAGTTCGAGAGGCAATTCATACATCCACTGGTCTGCGATTGTAGCGAGACGTAAGCATATCATATTAGGAACACGTAGGGCCTGTCCTGTCGTAGAGACAGTCAAGCCCAATCGTGTATGAGGTACAGAGGCACTTCACGCTACTTTCATCGTAACGCCGGATGTGCGAGTCACTCCGTAGATACCTTAGTATAGCTTCGCATCATGCTGTGTCTGACTAAGATACAACGTGTGGCCTTTCAATACGAAAAAATCTATGCAGGTCGCGTCACATCATGTGCCTCCCGTTGGGGGGGCTGGTCATAGATAGCGTTCCTGTGCGTCGCTCCAGAACCCCCCGCATTATGATAGTGTGGACGTACGTCGTACAGTAGTTCGTACAGCGCATGACCCAGGCTTCAATTGCAGTTACTCCGCGCCCATACAGCAATGCGTCGAGTATTCGACTCTTCTTCACAGGTTGCATGGTTTCCCTTCCCACTCGCCAGCGACGAAACCGGTTGCCAGCGTCTCATAGGCTCTGTGGACTTGGTGTTCCTAGGTACCCCTCTCATGACGCCGGTAAGGAAGACGAACAAATGGTGATGCAGGTCCCTAAAGGGCTCACTCCGCGGGCCAGCCTGCCAAAAGTTATGTGGATGTCCCCTGTGAGTGTTCAGTTTATGTCGGCACTTTAAAAAGGTTCTATCAACAGCCGCCTGAAGCGACGGTAGGTGTTTCACGAAGACTACGAGGAAGTGGGTTTCGTACGACAGCATGGGGGCTCTGAGACAAGCTTGCCCCCTCTTACGGGATTTAGGTTAGATGTAAGATTGACAGGCGTCGTACGAGCAACGTTAGCGCCTCAAATGACCTGGGCCTCCAGATCAGGTCAAACTGAGATCCACGCTGTGGGCGTAAGCGGGTTATAACGGGGATGAGTTACGTGTGAGTACCTACATGTGCGAGGCGCCTCTCGGTAGTGTCATACGTGCTAATGCGCGTCGAGCTTGGATGTGACTGAGAGGACGGGTGAAGGCTCCAATTCGTAGAAGCTGACGCATTAGTGCTTGGTATAGTAACTCAATCATCTCATCACGAAGTCTTCACGGACAAGTGACGTGTCGGCATGCCCTTTGTTTCGTGGTGGATAATATCGAAATTAATACCGGTGTCCTCCCGCATTCCCGCAGACTTACAGCTACTTCATATTACGTACAGGGCAGTAACCACTGTACGGCCTCATGATGTACTGCGAGGCTCTGCTCTAGCACGATCGGGTTGTGTTCCGAACACAGGCACCGTGTTGGCGGCTCATCATATCCACAAGAATCCCTTATGTCGCCTTGTTATTGAAGCGACAACCAATTAGTGTCACCTTCGCTTGGCTATCGGAAACTGTTGAACTGCGGATACATTACAACTATGATAAAGCTCTAAAACCAACTGTAATGTATAAAATAATTGGGCCCATTTTATTTCCCACAAGCTTACTGAACACTGACTTCGAGACATACAATTAACAGATGGACAGAACACCCCAGGATCCGGGTTTTTAATAAATGAGTTATCATTTCACGTTCTTTGCCTCCAGGGGCTGCCTCGTTCTGACTCCGATACTACTTGAGCGGATCCTATATTCCGGACGTAGGCAACACTAAAGGTGAAAATGCCAACGACCTTGGCTTATTCCCCTGAGCCCTTGTGGCCTTTCTCAAAATAAGAGGGTGGTGGGAGTGCCCAAGGCCGTTAGGAGTCTGTGCCAGGGGGTACCGCCATAGGGTACTCCATCCAATCTTCAGTGCGTGGCTAATCTCACAGGCGGTGATGGGCGATGGCGCTGAACTGACTTAAATCATTCCAATGAGATAGAAGAAGTACCCATGCTACTTCATCGCGGTTAAGAGGAGCCGTCTTAGGCTACCGGGATAGTTTCTGTTGCATTTTGGATCGGACACGAAAAGTATACCCAGGTGCTTTATTCATATCGTCGTCAGCCAAGTGCGCCGTTTGGAACAGAGAGCTCTAATTGTACTCCACGTCTCGCGCAACTACCCATACCCCAAATGGCCGCCTTCTTTACACGCGGATACTTTAGAAAACCTGTCTGAATCAATATTGGTCTGCGAGCTGGCGGCCAGCCTGTTCGCGACGTCAATGGCCGGATTTCAGCGCCGGTGTCTCTTAAAGGATCACTTCGCTTGTACCACGTGATACTAGATCTCCGATATTTGCACTTAGAACAGGACAAACCAGGACCGCTGAAACTCAAACTCGCAGTCTTTGAAAAGATAACGGAGGTTTAACGTAGTAGCGAATAGCGATTCCGTTTCTAATGTTGGCTACGCCCCAGTGAGCATGGTATCATGAGATTCCGGCAAGCAGCCGGTGTATAACGTTCAATATCCACGATATTATGCTCGTAAAGTTTGGGTGACCTTCATGCGATTGAACTGGCTTCCCTACTCACAACCAGCGACACCTGGCCGTATGGTCCGTGTTTGACCTTATGGCCGTTGGTACCTTAGCTGCTTCGTGAGTCGAAGGTCAAATAAAAGGTCAGCCAGACCAGAGACGTATCGACCGTTCGCGATTGCTGAGAGCTGATAACCCCGACCATACGCCTACAATATCAACCGGTCCCAGTCAAGCGTATACTGCGACCAGACGGTTCACAGCTAGGGTCGCACAAGTTATTGTTGACGTCTTTACCTCCGAATCTTACGGAGATGCCTACATAAGTCACTGAGGACACGTCGAGTAGGCTTATCTTATAGTGCATGAACTTTGATTTGCCACACATTAGAAGCCATTCGAATAAGAGGGTTATACTGGCAAACAGCATAGGCCAGTGACGCTAGAAGCTTGCCGATCCAATTGGCTCTATGGAAAAATGTAAACTATCTATGTGTTTAGGAGCCGCACTCCATCGCACGGTATAGATCTCTACGCTGGCGGCCTGATTAAG'
# d = 4
print(Approx_occurance(pattern,text,d))