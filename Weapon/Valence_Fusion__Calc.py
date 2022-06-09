
Fusion_Multiplier = 1.1
Minimum_Bonus = 25
Maximum_Bonus = 60
Starting_Bonus = 25
Bonus_Decimals = 2

print(f"Starting Progenitor Bonus: {Starting_Bonus}\nMultiplier per Valence Fusion: {Fusion_Multiplier}\nNote that the progenitor bonus is rounded to {Bonus_Decimals} decimals")

class Valence:

    def __init__(self) -> None:
        pass
    
    def setMulti(self, Multi):
        self.Multi = Multi
    def getMulti(self):
        return self.Multi
    def setCurrBonus(self, CurrBonus):
        self.CurrBonus = CurrBonus
    def getCurrBonus(self):
        return self.CurrBonus
    def setMinBonus(self, MinBonus):
        self.MinBonus = MinBonus
    def getMinBonus(self):
        return self.MinBonus
    def setMaxBonus(self, MaxBonus):
        self.MaxBonus = MaxBonus
    def getMaxBonus(self):
        return self.MaxBonus
    def setIteration(self, Iteration):
        self.Iteration = Iteration
    def getIteration(self):
        return self.Iteration


v = Valence()

# Resets values to defaults provided at beginning of the file. Useful if running multiple operations in one script?

def ResetValence():

    v.setMulti(Fusion_Multiplier)
    v.setMinBonus(Minimum_Bonus)
    v.setMaxBonus(Maximum_Bonus)
    v.setCurrBonus(Starting_Bonus)
    v.setIteration(0)


ResetValence()

# While loop calculates every valence fusion iteration until the weapon would be max

while v.CurrBonus < v.MaxBonus:
    
    v.CurrBonus = v.CurrBonus * v.Multi
    v.Iteration = v.Iteration + 1

    if v.CurrBonus > v.MaxBonus:
        v.CurrBonus = v.MaxBonus

    print(f"{v.Iteration} - {round(v.CurrBonus, Bonus_Decimals)}")
