"""
1. This function merges multiple PDF files into 1 file.
2. The first argument is a list of file-names.
"""
def merger(files, name= 'new'):

    from sys import exit
    from PyPDF2 import PdfMerger
    
    #Error check
    num = len(files)
    if num == 0:
        print("No PDF files in the current directory")
        exit(0)

    
    merger= PdfMerger()
    
    for i in range(num):
        merger.append(files[i])
    
    merger.write( name + '.pdf')
    merger.close()

    del PdfMerger, sys

    print("---Files merged---")


#Main
import glob

"""
1. Identifies PDF files in the current directory
2. Saves the filesnames in a list 
3. Sorts the filenames alphabetically
- To specify the order (of documents) in the merged PDF, append numerical prefixes to the file names. Rg. "1.pdf", "2.pdf", "3.pdf", etc.
"""
file_names = sorted(glob.glob(".\*.pdf"))

merger(file_names, name = "Merged_Files")
