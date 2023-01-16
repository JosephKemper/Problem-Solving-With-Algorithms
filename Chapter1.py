# Class to use fractions in Python
class Fraction:
    def __init__(self,top, bottom) -> None:
        self.numerator = top # int
        self.denominator = bottom # int

    def show (self):
        print(self.numerator,"/",self.denominator)

myFraction = Fraction(3,5)
myFraction.show()

