import ifcopenshell

def checkRule2(model):
    Walls = model.by_type('IfcWall')

    result = f"Walls: {len(Walls)}"

    return result

