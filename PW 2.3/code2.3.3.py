class Calculation:
    def __init__(self):
        self.calculationLine = ""

    def SetCalculationLine(self, value: str):
        self.calculationLine = value

    def SetLastSymbolCalculationLine(self, chair: str):
        self.calculationLine = self.calculationLine + chair

    def GetCalculationLine(self):
        print(self.calculationLine)

    def GetLastSymbol(self):
        return self.calculationLine[-1]

    def DeleteLastSymbol(self):
        self.calculationLine = self.calculationLine[0:-1]


calc1 = Calculation()
calc1.GetCalculationLine()
calc1.SetCalculationLine("Автомобиль")
calc1.GetCalculationLine()

print(calc1.GetLastSymbol())
calc1.DeleteLastSymbol()
calc1.SetLastSymbolCalculationLine("и")
calc1.GetCalculationLine()
