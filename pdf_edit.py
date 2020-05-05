from PyPDF2 import PdfFileReader, PdfFileWriter

# merge_pdfs appends pdf2 to the end of pdf1
# returns the location of the new pdf file
def merge_pdfs(output_name, location, pdf1, pdf2):
    paths = []
    paths.append(pdf1)
    paths.append(pdf2)
    location = location + '/'+ output_name
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(location, 'wb') as out:
        pdf_writer.write(out)

    return location


# create_split creates a new pdf from a given pdf 
# with page ranging from (start, end)
# returns location of newly created pdf
def create_split(pdf, output_name, location, start, end):
    start = int(start)
    end   = int(end) + 1
    location = location + '/'+ output_name
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(pdf)
    for page in range(start, end):
        pdf_writer.addPage(pdf_reader.getPage(page))
    with open(location, 'wb') as out:
        pdf_writer.write(out)
    print(location)
    return location 

    

    


