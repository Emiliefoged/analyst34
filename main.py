import ifcopenshell

from rules import GeometryRule
from rules import GeometryRule3

model = ifcopenshell.open("C:/Users/Emilie Foged Larsen/Dropbox/Pc/Desktop/DTU/Kandidat/BIM/CES_BLD_24_06_ARC.ifc")
print("model loaded")


#volumeResult = GeometryRule.checkRule(model)
#floorResult=GeometryRule1.checkRule(model)
#floorResult=GeometryRule2.checkRule(model)
floorResult=GeometryRule3.checkRule(model)


#print("volume result:",volumeResult)
#print("volume result:",floorResult)
for result in floorResult:
    print(result)
