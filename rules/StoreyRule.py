import ifcopenshell

def checkRule(model):
    levels = model.by_type('IfcBuildingStorey')

    #Definer loftshøjde-grænsen i millimeter
    elevation_threshold = 1500  # 1,5 meter er 1500 mm
    #Filtrer etager baseret på loftshøjde
    filtered_levels = [level for level in levels if level.Elevation is not None and level.Elevation > elevation_threshold]
    # Print antallet af etager der opfylder kraven
    result = f"Number of storeys including basements: {len(filtered_levels)}"

    return result

