# 8.	Create a base class Report with a method generate(). Derive PDFReport, ExcelReport, and HTMLReport. Override generate() in each class. Write a function that accepts any report object and calls generate().

class Report:
    def __init__(self, title, data):
        self.title = title
        self.data = data

    def generate(self):
        print(f"Generating generic report: {self.title}")


class PDFReport(Report):
    def generate(self):
        print(f"[PDF] Compiling vector graphics, headers, and pagination for '{self.title}.pdf'...")
        print(f"      Rows compiled: {len(self.data)}")


class ExcelReport(Report):
    def generate(self):
        print(f"[Excel] Generating workbook worksheets and formulas for '{self.title}.xlsx'...")
        print(f"      Data written across {len(self.data)} spreadsheet rows.")


class HTMLReport(Report):
    def generate(self):
        print(f"[HTML] Rendering responsive DOM tables and CSS styling for '{self.title}.html'...")
        print(f"      Embedded items: {len(self.data)}")


def process_report(report_obj):
    report_obj.generate()


sales_data = [{"id": 1, "item": "Keyboard"}, {"id": 2, "item": "Monitor"}]
reports = [
    PDFReport("Monthly_Financial_Statement", sales_data),
    ExcelReport("Inventory_Audit_Log", sales_data),
    HTMLReport("Executive_Dashboard", sales_data)
]

print("Generating Polymorphic Reports")
for r in reports:
    process_report(r)
