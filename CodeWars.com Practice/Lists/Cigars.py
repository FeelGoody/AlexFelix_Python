""" https://www.codewars.com/kata/5b64d2cd83d64828ce000039/train/python

DNA sequencing data can be stored in many different formats. In this Kata, we will be looking at SAM formatting. It is a plain text file where every line (excluding the first header lines) contains data about a "read" from whatever sample the file comes from. Rather than focusing on the whole read, we will take two pieces of information: the cigar string and the nucleotide sequence.

The cigar string is composed of numbers and flags. It represents how the read aligns to what is known as a reference genome. A reference genome is an accepted standard for mapping the DNA.

The nucleotide sequence shows us what bases actually make up that section of DNA. They can be represented with the letters A, T, C, or G.

Example Read: ('36M', 'ACTCTTCTTGCGAAAGTTCGGTTAGTAAAGGGGATG')

The M in the above cigar string stands for "match", and the 36 stands for the length of the nucleotide sequence. Since all 36 bases are given the 'M' distinction, we know they all matched the reference.

Example Read: ('20M10S', 'ACTCTTCTTGCGAAAGTTCGGTTAGTAAAG')

In the above cigar string, only 20 have the "M" distinction, but the length of the actual string of nucleotides is 30. Therefore we know that read did not match the reference. (Don't worry about what the other letters mean. That will be covered in a later kata.)

Your job for this kata is to create a function that determines whether a cigar string fully matches the reference and accounts for all bases. If it does fully match, return True. If the numbers in the string do not match the full length of the string, return 'Invalid cigar'. If it does not fully match, return False.
"""
import re
def is_matched(read):
    listInt = sum([int(s) for s in re.findall(r'-?\d+\.?\d*', read[0])])
    if sum(listInt) != len(read[1]):
        return 'Invalid cigar'  # 10M10S ACTCTTCTTG CGAAAGTTCG
    myVar = 0
    indexDNA = 0
    for index, i in enumerate(read[0]):
        if i.isalpha():
            value = int(read[0][myVar:index])
            myVar = index+1
            for ch in read[1][indexDNA:indexDNA+value]:
                if (i == 'M' and not ch in ('A', 'C', 'G', 'T')) \
                        or (i != 'M' and ch in ('A', 'C', 'G', 'T')):
                    return False
            indexDNA = value
    return True

print(is_matched(('5M3H', 'ATCGGGCT')))