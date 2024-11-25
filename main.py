import ifcopenshell

from rules import GeometryRule

model = ifcopenshell.open("C:/Users/Emilie Foged Larsen/Dropbox/Pc/Desktop/DTU/Kandidat/BIM/CES_BLD_24_06_ARC.ifc")
print("model loaded")



floorResult=GeometryRule.checkRule(model)


for result in floorResult:
    print(result)
