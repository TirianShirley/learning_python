#!/usr/bin/env python3

import gzip
import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

def read_fasta(filename):
	name = None
	seqs = []

	fp = None
	if filename == '-':
		fp = sys.stdin
	elif filename.endswith('.gz'):
		fp = gzip.open(filename, 'rt')
	else:
		fp = open(filename)

	for line in fp.readlines():
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				seq = ''.join(seqs)
				yield(name, seq)
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)
	yield(name, ''.join(seqs))
	fp.close()
def kd(protein):
    sum = 0
    for aa in protein:
        if aa == 'I': sum += 4.5
        elif aa == 'V': sum += 4.2
        elif aa == 'L': sum += 3.8
        elif aa == 'F': sum += 2.8
        elif aa == 'C': sum += 2.5
        elif aa == 'M': sum += 1.9
        elif aa == 'A': sum += 1.8
        elif aa == 'G': sum += -0.4
        elif aa == 'T': sum += -0.7
        elif aa == 'S': sum += -0.8
        elif aa == 'W': sum += -0.9
        elif aa == 'Y': sum += -1.3
        elif aa == 'P': sum += -1.6
        elif aa == 'H': sum += -3.2
        elif aa == 'E': sum += -3.5
        elif aa == 'Q': sum += -3.5
        elif aa == 'D': sum += -3.5
        elif aa == 'N': sum += -3.5
        elif aa == 'K': sum += -3.9
        elif aa == 'R': sum += -4.5
    return sum/len(protein)

def hah(sequence, w, thres):
    for i in range(len(sequence)-w+1):
        sseq = sequence[i:i+w]
        if kd(sseq) > thres and 'P' not in sseq: return True
    return False


for name, sequence in read_fasta(sys.argv[1]):
    nterm = sequence[0:30]
    rest = sequence[30:len(sequence)]
    if hah(nterm, 8, 2.5) and hah(rest, 11, 2.0):
        print(name)
    

"""
18w
Dtg
Krn
Lac
Mcr
PRY
Pxt
Pzl
QC
Ror
S1P
S2P
Spt
apn
bai
bdl
bou
bug
cue
drd
ft
grk
knk
ksh
m
nac
ort
rk
smo
thw
tsg
waw
zye
"""
