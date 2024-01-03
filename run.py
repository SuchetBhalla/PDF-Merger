#If there are no PDFs, then the program exits
def check(A, M):
    import sys

    if ( not(A) ):
        print(M)
        sys.exit()

#This function merges the files
def merger(files, name= 'new'):

    #Error check
    num= len(files)
    check(num > 0, "Zero files in list" )


    from PyPDF2 import PdfMerger

    merger= PdfMerger()

    for i in range(num):
        merger.append(files[i])

    merger.write( name + '.pdf')
    merger.close()

    del PdfMerger

    print("---Files merged---")


#Main
import glob

file_names = sorted(glob.glob(".\*.pdf"))

merger(file_names, name = "Merged_Files")
