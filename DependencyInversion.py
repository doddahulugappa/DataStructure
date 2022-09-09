from abc import ABC


class Convertor(ABC):
    def convert(self, from_currency, to_currency, amount):
        pass


class AEDConversion(Convertor):
    def convert(self, from_currency, to_currency, amount):
        return amount * 20


class USDConversion(Convertor):
    def convert(self, from_currency, to_currency, amount):
        return amount * 77


class App:
    def __init__(self, converter: Convertor):
        self.convertor = converter

    def start(self, from_currency, to_currency, amount):
        return self.convertor.convert(from_currency, to_currency, amount)


to_currency = "INR"
amount = 100000
aed_convertor = AEDConversion()
app = App(aed_convertor)
from_currency = "AED"
print("From {} to {} = {}".format(from_currency, to_currency, app.start(from_currency, to_currency, amount)))
usd_convertor = USDConversion()
from_currency = "USD"
app = App(usd_convertor)
print("From {} to {} = {}".format(from_currency, to_currency, app.start(from_currency, to_currency, amount)))
