import json


class VoidRelic:

    itemType = 'Void Relic'

    def __init__(self, id) -> None:

        self.id = id        
        
    def setTier(self, tier):
        self.tier = tier
    def getTier(self):
        return self.tier
    def setQuality(self, quality):
        self.quality = quality
    def getQuality(self):
        return self.quality
        

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
    i = VoidRelic(i["id"])
    i.setTier(i["tier"])
    i.setQuality(i["quality"])
    print(i["id"])
