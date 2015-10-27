from Bio.Seq import Seq
dnaSeq = Seq(open('rosalind_ini.txt','r').read().rstrip())

#we already have a set of expected values. count only these.
nucleotides = ['A','C','G','T']

#store the count per nucleotide in the same sequence
nucleotidesCount = []

#go through the list of nucleotides and count the number of occurences of the nucleotide in the DNA sequence
#DNA sequence must be formatted correctly once received (e.g. expect that data must contain only uppercase letters)
for i in nucleotides:
    nucleotidesCount.append(str(dnaSeq.count(i)))
print ' '.join(nucleotidesCount)
