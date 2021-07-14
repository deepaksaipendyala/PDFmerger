import sys
import os
import PyPDF2

#grabbing args from User input
input_folder=sys.argv[1]

def pdf_combiner(pdf_list):
  merger= PyPDF2.PdfFileMerger()
  for pdf in pdf_list:
    p=open(f'{input_folder}{pdf}', 'rb')
    pdf=PyPDF2.PdfFileReader(p)
    merger.append(pdf)
  merger.write('merged.pdf')
  #saved the combined pdf as merged.pdf

#filtering pdf files from the folder and saving them as list
pdf_list=[a for a in os.listdir(input_folder) if a.endswith(".pdf")]
#calling the function by sending pdf list saved into it
pdf_combiner(pdf_list)
