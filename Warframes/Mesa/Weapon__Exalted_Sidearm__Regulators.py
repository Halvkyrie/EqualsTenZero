import math

### Base Stats ##
WeaponBaseStats = {
    "dmg": 50,
    "physImpact": 0.5,
    "physPuncture": 0.25,
    "physSlash": 0.25
}
WFBaseStats = {
    "dur": 1,
    "eff": 1,
    "range": 1,
    "str": 1
}

### Stat Bonuses ###

WFStatBonus = {
    "dur": 0,
    "eff": 0,
    "range": 0,
    "str": 0
}
WeaponModBonus = {
    "dmg": 2.2
}

### Modifiers ###

DMGMulti = {
    "constant": 1.5,
    "conditional": 1.5,
    "burst": 4.5,
    "specialBurst": 1.5
}
BurstCount = 1
MaxBurstCount = 20

finalDMG = WeaponBaseStats["dmg"] * (1 + (DMGMulti["conditional"] * (WFBaseStats["str"] + WFStatBonus["str"])) + (DMGMulti["constant"] * WFBaseStats["str"]) + WeaponModBonus["dmg"] + ((DMGMulti["burst"] * (WFBaseStats["str"] + (0.5 * WFStatBonus["str"])) + (DMGMulti["specialBurst"] * (1 + WeaponModBonus["dmg"]))) * (BurstCount / MaxBurstCount)))
finalImpact = finalDMG * WeaponBaseStats["physImpact"]
finalPuncture = finalDMG * WeaponBaseStats["physPuncture"]
finalSlash = finalDMG * WeaponBaseStats["physSlash"]

quantum = finalDMG / 16

quantizedImpact = round(finalImpact / quantum) * quantum
quantizedPuncture = round(finalPuncture / quantum) * quantum
quantizedSlash = round(finalSlash / quantum) * quantum

finalDmgCharger = finalImpact + finalPuncture + (finalSlash * 1.25)

quantizedDmgCharger = round(quantizedImpact + quantizedPuncture + (quantizedSlash * 1.25))

print(f"The Total Damage is: {finalDMG}")
print(f"This is distributed as: \nImpact: {finalImpact} \nPuncture: {finalPuncture} \nSlash: {finalSlash}")
print(f"Before quantization this should deal {finalDmgCharger} Damage against an Infested Charger")
print(f"With quantization in mind, this should deal {quantizedDmgCharger} Damage against an Infested Charger")