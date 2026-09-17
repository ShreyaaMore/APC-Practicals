# 13.	Create classes Printer and Scanner with suitable methods for printing and scanning documents. Create a MultifunctionDevice class that inherits from both and supports both operations.

class Printer:
    def __init__(self, print_speed_ppm):
        self.print_speed_ppm = print_speed_ppm

    def print_document(self, document_name):
        print(f"[Printer] Printing '{document_name}' at {self.print_speed_ppm} pages per minute...")


class Scanner:
    def __init__(self, scan_resolution_dpi):
        self.scan_resolution_dpi = scan_resolution_dpi

    def scan_document(self, document_name):
        print(f"[Scanner] Scanning '{document_name}' at {self.scan_resolution_dpi} DPI...")


class MultifunctionDevice(Printer, Scanner):
    def __init__(self, model_name, print_speed_ppm, scan_resolution_dpi):
        Printer.__init__(self, print_speed_ppm)
        Scanner.__init__(self, scan_resolution_dpi)
        self.model_name = model_name

    def display_specs(self):
        print(f"Device Model     : {self.model_name}")
        print(f"Print Capability : {self.print_speed_ppm} ppm")
        print(f"Scan Resolution  : {self.scan_resolution_dpi} DPI\n")


mfd = MultifunctionDevice("HP LaserJet Pro MFP", 28, 1200)
print("Multifunction Device Operations")
mfd.display_specs()
mfd.print_document("APC_Project_Report.pdf")
mfd.scan_document("National_ID_Card.png")
