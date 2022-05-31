import json
from xml.etree.ElementTree import tostring


class VoidRelic:

    itemType = 'Void Relic'

    def __init__(self) -> None:
        return        
        
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

    print(f"[{tier} {id} Relic] \nRefinement: {quality}")
    # print(f"{tier} {id} - \({quality}\)")
