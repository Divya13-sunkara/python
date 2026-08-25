class Printer:
    def print(self):
        print("Printing document")

class PDFPrinter:
    def print(self):
        print("Printing PDF")

def print_document(obj):
    obj.print()

print_document(Printer())
print_document(PDFPrinter())