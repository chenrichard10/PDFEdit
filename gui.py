import tkinter as tk
from tkinter import filedialog
# os.startfile(opens the specified )
class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.resizable(0, 0)
        self.geometry("400x400")
        self.title("PDFEdit")
        self.iconbitmap('C:/Users/chenp/Documents/GitHub/PDFEdit/res/pdf.ico')
        self.create_widgets()

    """def merge(self):
        first_pdf = "temp"
        second_pdf = "temp"
        combined_pdf = "temp"""
        




    def create_widgets(self):
        # Creating the buttons 
        self.merge_btn = tk.Button(self, text = "Merge PDF", padx = 50, pady = 50)
        self.convert_btn = tk.Button(self, text = "Convert to .docx", padx = 45, pady = 50)
        self.edit_btn = tk.Button(self, text = "Edit PDF", padx = 56, pady = 50)
        self.extract_btn = tk.Button(self, text = "Extra Info", padx = 64, pady = 50)
        # Positioning the buttons 
        self.merge_btn.grid(row = 2, column = 2,  padx = 10, pady = 20)
        self.convert_btn.grid(row = 2, column = 4,  padx = 10, pady = 20)
        self.edit_btn.grid(row = 4, column = 2,  padx = 10, pady = 20)
        self.extract_btn.grid(row = 4, column = 4,  padx = 10, pady = 20)

    def greet(self):
        print("Greetings!")


if __name__ == '__main__':
    app = Application()
    app.mainloop()

