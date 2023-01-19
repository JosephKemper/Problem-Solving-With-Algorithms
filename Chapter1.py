# Class to use fractions in Python
class Fraction:
    def __init__(self,top, bottom):
        self.numerator = top # int
        self.denominator = bottom # int

    def __str__(self) -> str:
        
        return str(self.numerator)+"/"+str(self.denominator)

    def show (self):
        print(self.numerator,"/",self.denominator)

    def __add__ (self,otherFraction):
        newNumerator = self.numerator*otherFraction.denominator +\
            self.denominator*otherFraction.numerator
        newDenominator = self.denominator* otherFraction.denominator
        common = gcd(newNumerator,newDenominator)

        return Fraction(newNumerator//common,newDenominator//common)
    
    def __eq__(self, other) -> bool:
         firstNumerator = self.numerator * other.denominator
         secondNumerator = other.numerator * self.denominator

         return firstNumerator == secondNumerator


def gcd (m,n):
        while m%n != 0:
            oldM = m
            oldN = n

            m = oldN
            n = oldM%oldN
        return n


class LogicGate:
    def __init__(self,n):
         self.label = n
         self.output = None
    
    def getLabel (self):
        return self.label
    
    def getOutput (self):
        self.output = self.performGateLogic ()# type: ignore
        return self.output

class BinaryGate(LogicGate):
    def __init__(self, n):
        super().__init__(n)

        self.pinA = None
        self.pinB = None
    
    def getPinA (self):
        return int (input("Enter Pin A input for gate " +\
            self.getLabel()+ "-->"))
    
    def getPinB (self):
        return int (input("Enter Pin B input for gate " +\
            self.getLabel()+ "-->"))

class UnaryGate (LogicGate):

    def __init__(self, n):
        super().__init__(n)

        self.pin = None
    
    def getPin (self):
        return int (input("Enter Pin input for gate " +\
            self.getLabel()+ "-->"))

class AndGate (BinaryGate):

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic (self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

myFraction = Fraction(3,5)

myFraction.show()
print (f"I ate {myFraction} of the pizza")

f1 = Fraction (1,4)
f2 = Fraction (1,2)
f3 = f1 + f2
print (f3)