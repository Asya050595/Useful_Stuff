from Bio import SeqIO
import os
os.chdir('THIS_IS_PATH_TO_YOUR_DIR')

records = SeqIO.parse("THIS_IS_YOUR_INPUT_FILE.fasta", "fasta")
count = SeqIO.write(records, "THIS_IS_YOUR_OUTPUT_FILE.phylip", "phylip")
print("Converted %i records" % count)