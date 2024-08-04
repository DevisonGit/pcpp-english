from abc import ABC, abstractmethod


class AbstractScanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass

    @abstractmethod
    def get_scanner_status(self):
        pass


class AbstractPrinter(ABC):
    @abstractmethod
    def print_document(self):
        pass

    @abstractmethod
    def get_printer_status(self):
        pass


class MFD1(AbstractScanner, AbstractPrinter):
    def scan_document(self):
        return "Document scanned with low resolution"

    def get_scanner_status(self):
        return "Scanner status: Max resolution 200dpi, Serial number: MFD1-Scanner-001"

    def print_document(self):
        return "Document printed with low resolution"

    def get_printer_status(self):
        return "Printer status: Max resolution 200dpi, Serial number: MFD1-Printer-001"


class MFD2(AbstractScanner, AbstractPrinter):
    def __init__(self):
        self.print_history = []

    def scan_document(self):
        return "Document scanned with medium resolution"

    def get_scanner_status(self):
        return "Scanner status: Max resolution 600dpi, Serial number: MFD2-Scanner-002"

    def print_document(self):
        message = "Document printed with medium resolution"
        self.print_history.append(message)
        return message

    def get_printer_status(self):
        return "Printer status: Max resolution 600dpi, Serial number: MFD2-Printer-002"

    def get_print_history(self):
        return self.print_history


class MFD3(AbstractScanner, AbstractPrinter):
    def __init__(self):
        self.print_history = []

    def scan_document(self):
        return "Document scanned with high resolution"

    def get_scanner_status(self):
        return "Scanner status: Max resolution 1200dpi, Serial number: MFD3-Scanner-003"

    def print_document(self):
        message = "Document printed with high resolution"
        self.print_history.append(message)
        return message

    def get_printer_status(self):
        return "Printer status: Max resolution 1200dpi, Serial number: MFD3-Printer-003"

    def get_print_history(self):
        return self.print_history

    def fax_document(self, fax_number):
        return f"Document faxed to {fax_number}"


# Create instances of each MFD
mfd1 = MFD1()
mfd2 = MFD2()
mfd3 = MFD3()

# Demonstrate MFD1 capabilities
print("MFD1 Capabilities:")
print(mfd1.scan_document())
print(mfd1.get_scanner_status())
print(mfd1.print_document())
print(mfd1.get_printer_status())
print()

# Demonstrate MFD2 capabilities
print("MFD2 Capabilities:")
print(mfd2.scan_document())
print(mfd2.get_scanner_status())
print(mfd2.print_document())
print(mfd2.get_printer_status())
print("Print history:", mfd2.get_print_history())
print()

# Demonstrate MFD3 capabilities
print("MFD3 Capabilities:")
print(mfd3.scan_document())
print(mfd3.get_scanner_status())
print(mfd3.print_document())
print(mfd3.get_printer_status())
print("Print history:", mfd3.get_print_history())
print(mfd3.fax_document("123-456-7890"))
print()
