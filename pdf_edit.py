from PyPDF2 import PdfFileReader, PdfFileWriter
# Merging PDFs 
def merge_pdfs(output_name, location, pdf1, pdf2):
    paths = []
    paths.append(pdf1)
    paths.append(pdf2)
    location = location + '/'+ output_name;
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(location, 'wb') as out:
        pdf_writer.write(out)

    print(location)
    return location
        


    






