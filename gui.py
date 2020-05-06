import pdf_edit as edit
import tkinter as tk
from tkinter import filedialog
from tkinter import font as tkfont
import os
class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # Main window is not resizable for now 
        self.resizable(0, 0)
        self.geometry("400x400")
        self.geometry("400x300")
        self.title("PDFEdit")
        self.iconbitmap('C:/Users/chenp/Documents/GitHub/PDFEdit/res/pdf.ico')
        self.create_widgets()

    # Creating widgets for the starting screen 
    def create_widgets(self):
        # Creating the buttons 
        self.merge_btn = tk.Button(self, font =("Arial", "12"), text = "Merge PDF", padx = 30, pady = 30, command = self.merge, fg = '#ffffff', bg = '#ff0000')
        self.edit_btn = tk.Button(self, font =("Arial", "12"), text = "Edit PDF", padx = 36, pady = 30, fg = '#ffffff',  bg = '#ff0000', command = self.edit_pdf)
        # Positioning the buttons 
        self.merge_btn.grid(row = 2, column = 2,  padx = 10, pady = 20)
        self.convert_btn.grid(row = 2, column = 4,  padx = 10, pady = 20)
        self.edit_btn.grid(row = 4, column = 2,  padx = 10, pady = 20)
        self.extract_btn.grid(row = 4, column = 4,  padx = 10, pady = 20)


    def merge(self):
        top = tk.Toplevel()
        top.title("Edit your Pdf")
        top.iconbitmap('C:/Users/chenp/Documents/GitHub/PDFEdit/res/pdf.ico')
        top.geometry("400x400")
        f_label = tk.Label(top, font =("Arial", "12"), text = "Merged file name:", pady = 20)
        file = tk.Entry(top, width = 35, borderwidth = 5)
        button = tk.Button(top, font =("Arial", "12"), text = "Merge PDF", padx = 30, pady = 20, 
                            fg = '#ffffff', bg = '#ff0000', command = lambda: self.merge_wrapper(file.get()))
        f_label.pack()
        file.pack()
        button.pack()


    # This function opens 3 separate file dialogs to find the combined PDF and location 
    # to be saved
    # Merged file is opened afterwards 
    def merge(self):
    def merge_wrapper(self, output):
        pdf1 = tk.filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select first PDF")
        pdf2 = tk.filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select second PDF")
        location = tk.filedialog.askdirectory(initialdir = os.getcwd(), title = "Select a folder to be stored")
        combined = edit.merge_pdfs('merged.pdf', location, pdf1, pdf2)
        combined = edit.merge_pdfs(f'{output}.pdf', location, pdf1, pdf2)
        os.startfile(combined)

    def pdfToDocx(self):
        document = Document()
        document.add_heading('Document Title', 0)
        text=""
        pdf_file = tk.filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select PDF")
        pdf_file
        read_pdf = PdfFileReader(pdf_file)
        c = read_pdf.numPages
        print('gunga')
        for i in range(c):
            page = read_pdf.getPage(i)
            text+=(page.extractText())
        
        document.add_paragraph(text)
        document.add_page_break()
        document.save(read_pdf.documentInfo.title + '.docx')

    def docxtoPDF(self):
        wdFormatPDF = 17
        word = comtypes.client.CreateObject('Word.Application')
        doc = tk.filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select first PDF")
        doc.SaveAs(doc.Title + '.pdf', FileFormat=wdFormatPDF)
        doc.Close()
        word.Quit() 
    # Edit_pdf creates a new window to create a new_pdf from a user specified page range
    def edit_pdf(self):
        top = tk.Toplevel()
        top.title("Edit your Pdf")
        top.iconbitmap('C:/Users/chenp/Documents/GitHub/PDFEdit/res/pdf.ico')
        top.geometry("400x400")
        label = tk.Label(top, font =("Arial", "12"), text = "Enter the starting page",pady = 20)
        label2 = tk.Label(top, font =("Arial", "12"), text = "Enter the ending page", pady = 20)
        label3 = tk.Label(top, font =("Arial", "12"), text = "File name", pady = 20)
        start = tk.Entry(top, width = 35, borderwidth = 5)
        end = tk.Entry(top, width = 35, borderwidth = 5)
        file = tk.Entry(top, width = 35, borderwidth = 5)
        button = tk.Button(top, font =("Arial", "12"), text = "Create PDF", padx = 30, pady = 20, 
                            fg = '#ffffff', bg = '#ff0000', command = lambda: 
                            self.create_split_pdf(file.get()+".pdf", start.get(), end.get()))
        label.pack()
        start.pack()
        label2.pack()
        end.pack()
        label3.pack()
        file.pack()
        button.pack()

    # A wrapper function for create_split in pdf_edit.py
    # Opens newly created pdf and prompts user to select pdf and folder to store
    def create_split_pdf(self, output_name, start, end): 
        file = tk.filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select PDF")
        folder = tk.filedialog.askdirectory(initialdir = os.getcwd(), title = "Select Folder To Store")
        new_file = edit.create_split(file, output_name, folder, start, end)
        os.startfile(new_file)


    def start_file(self, new_file):
        os.startfile(new_file)

    def create_widgets(self):
        # Creating the buttons 
        self.merge_btn = tk.Button(self, text = "Merge PDF", padx = 50, pady = 50, command = self.merge)
        self.edit_btn = tk.Button(self, text = "Edit PDF", padx = 56, pady = 50)
        # Positioning the buttons 
        self.merge_btn.grid(row = 2, column = 2,  padx = 10, pady = 20)
        self.convert_btn.grid(row = 2, column = 4,  padx = 10, pady = 20)
        self.edit_btn.grid(row = 4, column = 2,  padx = 10, pady = 20)
        self.extract_btn.grid(row = 4, column = 4,  padx = 10, pady = 20)

if __name__ == '__main__':
    app = Application()
    app.mainloop()

