class PDFReport:
    def generate(self):
        print("Generating PDF report")

class ExcelReport:
    def generate(self):
        print("Generating Excel report")

class WordReport:
    def generate(self):
        print("Generating Word report")

def generate_report(report):
    report.generate()

generate_report(PDFReport())
generate_report(ExcelReport())
generate_report(WordReport())