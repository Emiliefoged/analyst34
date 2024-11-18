import ifcopenshell
import ifcopenshell.util.element

def checkRule(model):
    elements = model.by_type('IfcSlab')  # Gets all IfcSlab objects
    result = []  # List to save volume for each item
    
    # Variables to sum the volume and CO2 emissions for each category
    laminate_volume = 0
    tile_volume = 0
    wood_volume = 0

    laminate_co2 = 0
    tile_co2 = 0
    wood_co2 = 0

   # Densities (kg/m³) and CO2 emissions for each material
    laminate_density = 850  # kg/m³
    laminate_co2_factor = 0.051  # kgCO2e/kg

    tile_density = 4000  # kg/m³
    tile_co2_factor = 0.757  # kgCO2e/kg

    #wood_density = 600  # kg/m³ - not relevant as we have another another unit for the CO2
    wood_co2_factor = 91.9  # kgCO2e/m3

    for element in elements:
         # Retrieve Property Sets (psets) for the element
        psets = ifcopenshell.util.element.get_psets(element)
        
        # Check if there is a Dimensions pset with a 'Volume' property
        if 'Dimensions' in psets and 'Volume' in psets['Dimensions']:
            volume = psets['Dimensions']['Volume']  # Hent volumen
            name_lower = element.Name.lower() if element.Name else ""  # Name in lowercase to avoid case sensitivity
            
            # Check and assign volume and CO2 emissions to the correct category
            if "laminate" in name_lower:
                laminate_volume += volume
                mass = volume * laminate_density
                laminate_co2 += mass * laminate_co2_factor
            elif "tile" in name_lower:
                tile_volume += volume
                mass = volume * tile_density
                tile_co2 += mass * tile_co2_factor
            elif "wood" in name_lower:
                wood_volume += volume
                wood_co2 += volume* wood_co2_factor

    # Add the total volumes and CO2 emissions for each category to the results list
    if laminate_volume > 0:
        result.append(f"Total volume of Laminate flooring: {laminate_volume} m³, total CO2 contribution from laminate flooring: {laminate_co2} kgCO2eq")
    if tile_volume > 0:
        result.append(f"Total volume of Tile flooring: {tile_volume} m³, total CO2 contribution from tile flooring: {tile_co2} kgCO2eq")
    if wood_volume > 0:
        result.append(f"Total volume of Wood flooring: {wood_volume} m³, total CO2 contribution from wood flooring: {wood_co2} kgCO2eq")
        
    return result
