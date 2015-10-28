'''
FASTQ Read Filtration by Quality
http://rosalind.info/problems/filt/

Given:
Quality cut-off value
Percent of bases in sequence that must have quality equal to / higher than cut-off value
'''
from Bio import SeqIO
fastq = open('rosalind_filt.txt')
#fastq = open('testFASTQ.txt')

#t = threshold, p = percentage
t,p = [int(i) for i in fastq.readline().rstrip().split()]
records = list(SeqIO.parse(fastq,'fastq'))

#q = phredQuality list
q = [record.letter_annotations['phred_quality'] for record in records]

print len([k for k in [sum([int(j >= t) for j in i])/float(len(i)) for i in q] if k >= p/100.])

