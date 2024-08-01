class Phone:
    def __init__(self, serial, model, imei):
        self.serial = serial
        self.model = model
        self.imei = imei

    def info(self):
        return (f"Serial: {self.serial} \nModel: {self.model} "
                f"\nIMEI: {self.imei}")


phone = Phone('AB123456789', 'S23', '123456789')

print(f'access instance variable ==> {phone.serial}')
print(f'calling methods \n{"-" * 10}\n{phone.info()}')
