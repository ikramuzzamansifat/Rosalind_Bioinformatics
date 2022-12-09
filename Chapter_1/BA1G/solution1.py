from collections import Counter
def Hamming_Distance(s1,s2):
    ans = 0
    for i,j in zip(s1,s2):
        if(i != j):
            ans += 1
    return ans
# Test dataset
s1 = 'GGGCCGTTGGT'
s2 = 'GGACCGTTGAC'

#debug dataset
# s1 = 'AATCAGCACGCTCAGCGAAGATGAGCGGGGTTTGTTAAATGCCTTCAGACCAAGTCACAGGGATTCATCCGCTCCCATGGTTAAATGCCACGGGGTACCCGGAGAACACTTCATTGTGATATGTCGCATGGGACTTGCGCAACTCATATTGCTTAAGCTTGCCCTACTGTCTTCCGAGAAATTAGACTTAGGAATGAGTTTCCCGCCAATGTACCAAATATGGTGCACTAGGGATGTAAGTCCGATGTTGCTTGCAGAAACATTTATAAACATATCCTATCTCCTGGGATGGAGTCTTGAGCCTCGGATAGCCCACCAACTGTGTAATAGTAGCTTAAGACACATTTTGCTAAATACTGCCGGAAGGTTGTTTTCCCATACCCCGATCTGATTTAACACTCGAGTAAGTCCCAACTCGCAGACAATTTACCCACATGGGCGGAAAAGCAGTCGTCTAGGCGAACGAAACAGGCTCACCTTGGGCCACTATGGAAAATGGCGTGGATAAGATGTGTTATATATCCTTGCTACACCGTACATATGCAATTTATGTCAGCCACAGTGTCATGACAGAATTTGTGTTAGGGCATTCGCTCCACTGGGGCTGTCGATTTGATACACTAAGAGGGGAGTAGGATTTGGCCGGAACTTTATGTCGGTTGGACATTGGCTACTCACCAACAGTTGAACGAATAGGATATTCTTTCTTCCGCCCCTGAGTAACCTACGGTCAACGGAACGTTGGATTACCTACGAATATCGTGGCGAGTGGGCTCATGGAGTGTTACAATATACCTATTTTGACCCCAAGCGCACCCTCAATATTATTCGACGTCGAGCGTGTATCTTAATCAAACAACCCCCTATCTAATAGTTCCGGTCGTCCTACTATTCCCCACAGTGTGCCGTTATCTAGGGTGATGCCCAATTTAAACACCCTAGTTGGGGTAAGACATTTGGTCCAGCCAAACAATCAAGCATTCTCCCCATACCGGGATCCTCTCA'
# s2 = 'CGGGAGTAAAGGTTCTTGGTAGTGATCGTTCAGGTGACTTAAGTATACATTCCCCCTGCGTTGTACGTTATCATGCTTTGCCTTAAGCGCTCTACATGGATAGTGCCTTACATGGATTCGCATGTCCGCTCGACAGCTCCGTAACACCTTTGGAGTGTTCATCGATGACTCCGAGTAAAATATCTGGGGATATTTTGTCGCGGTAGTTTCTGTACAGTATGAGTCTGCTATTAGTTGTCTGACGCAGGTCCCGAGCAACCAACTCATATGCCGTGGCCTCAAGCAAGTTAAGTAGTTAATCACTCTCCGCTGCCGAGAGCACGCCCCCTGTGTACCGCCGTGTTCTTTTACTGCCTTAACTCTTGCCCAGCCAGATGTCTCAGGGGCGGCAAAAGGTGAGCTTCACAGTCTCCTCCGGAAGCTTAGGCTTATTAGCTATCGTCTAGTCGGTCTAGCAGATCGGCCACGTAAGATTCAATTAATAGGTGCGACATCCTGGGGTTCAGGATTCATAAAACTAAGTACGCGTGCTACGCTACACCTCATTCTGATTTGCACCAGGTGAGCACATGAAGTACGAATGAACGTGCAACGCGCTACTCGCAGATTACAATCCGTAAGTTGCAGCTGTTTAGTGGTAAGAGTTAAGAGAGAAAAATCATACCGGAATAGCAAACTTTTTCTGCTACTCGGCCTCGAGGTGATGTATCACCCGCCCCGTATAACATCATACGACCCAATTCGCTGTGAGAGTCGATGCTATTAAAGAGCACCATAGCAGCTGTCTTGGGTGCGGTAGTGAACTAGCGATAATGCCTGGTTGTTTGAACCGGGGTGATTACGTTCATATAGAATTGCCTGAAGGAATGTGTACGTAGCTGATTCGGGTCAGCCAGGATCTGTGTCGTTACAGAGAATAGCGCAAGGTTCATTTAAACATTTAGCTCGCCATTTTAAGAAGTCCCGTAGTGGAGGAACCCCATCTTCCCCTTCCTTCGTTTCTGC'
print(Hamming_Distance(s1,s2))