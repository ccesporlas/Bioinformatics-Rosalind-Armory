'''
Convert sequence data from FASTQ to FASTA format
http://rosalind.info/problems/tfsq/

Bio.SeqIO.convert()

from Bio import SeqIO
records = SeqIO.parse(in_handle, in_format)
count = SeqIO.write(records, out_handle, out_format)

from Bio import SeqIO
count = SeqIO.convert(in_handle, in_format, out_handle, out_format)

Sample Dataset:
@SEQ_ID
GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT
+
!*((((***+))%%%++)(%%%%).1***-+*****))**55CCF>>>>>>CCCCCCC65

Sample Output:
>SEQ_ID
GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT
'''

from Bio import SeqIO
fastq = open('rosalind_tfsq.txt')
#fastq = open('testFASTQ.txt')
fasta = open('testFASTA.txt','w+')
count = SeqIO.convert(fastq,'fastq',fasta,'fasta')
fastq.close()
fasta.close()

fastaRead = open('testFASTA.txt').read()
print fastaRead

