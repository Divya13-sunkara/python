class TextFile:
    def read(self):
        print("Reading Text file")

class PDFFile:
    def read(self):
        print("Reading PDF file")

class ExcelFile:
    def read(self):
        print("Reading Excel file")

def read_file(file):
    file.read()

read_file(TextFile())
read_file(PDFFile())
read_file(ExcelFile())