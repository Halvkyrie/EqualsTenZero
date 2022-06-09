import json
import yaml


# Class for the Void Relic and its values
class VoidRelic:

    itemType = 'Void Relic'

    # init - Requiring no other input
    def __init__(self) -> None:
        return        
    
    # definitions to read/write information
    def setTier(self, tier):
        self.tier = tier
    def getTier(self):
        return self.tier
    def setQuality(self, quality):
        self.quality = quality
    def getQuality(self):
        return self.quality
    def setID(self, ID):
        self.id = ID
    def getID(self):
        return self.id
    
    # Class for Rewards
    class Reward:

        def __init__(self) -> None:
            return
        
        def setT3(self, T3):
            self.T3 = T3
        def getT3(self):
            return self.T3
        def setT2(self, T2):
            self.T2 = T2
        def getT2(self):
            return self.T2
        def setT1(self, T1):
            self.T1 = T1
        def getT1(self):
            return self.T1
        




VoidRelicList = [
    {
        "id": "G5",
        "tier": "Axi",
        "quality": "Intact"
    },
    {
        "id": "K3",
        "tier": "Neo",
        "quality": "Radiant"
    }
]

for i in VoidRelicList:
    relic = VoidRelic()
    relic.setTier(i["tier"])
    relic.setQuality(i["quality"])
    relic.setID(i["id"])
    tier = relic.getTier()
    quality = relic.getQuality()
    id = relic.getID()
    fullName = f"{tier} {id} Relic"

YamlRelicList = ("""
""")
