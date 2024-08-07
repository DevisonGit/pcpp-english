class Scanner:
    def scan(self):
        print("scan() method from Scanner class")


class Printer:
    def print(self):
        print("print() method from Printer class")


class Fax:
    def send(self):
        print("send() method from Fax class")

    def print(self):
        print("print() method from Fax class")


# Multifunction device classes with different inheritance orders
class MFD_SPF(Scanner, Printer, Fax):
    pass


class MFD_SFP(Scanner, Fax, Printer):
    pass


# Instantiate the classes
mfd_spf = MFD_SPF()
mfd_sfp = MFD_SFP()

# Call the methods on each object
print("MFD_SPF:")
mfd_spf.scan()
mfd_spf.print()
mfd_spf.send()

print("\nMFD_SFP:")
mfd_sfp.scan()
mfd_sfp.print()
mfd_sfp.send()
