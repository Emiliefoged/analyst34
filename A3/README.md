# Introduction
BIManalyst group 34
This tool is made for calculating the carbon footprint (CO2) of tree different floor materials. Before using the tool you need to have access to an IFC file with specific volumens for the materials. In this cide we used CES_BLD_24_06_ARC which is available in this course. You also have to be familiar with an LCA database, in this case we used Ecoinvent where the global warming potential is defined with the unit kg CO2-eq.
# Using the tool
You'll need to know the density [kg/m3] and CO2 emmisions [kgCO2-eq] for every material. This is essential for the calculation to work. When using this code this information is already included, so it's easy to run it. If you would like to calculate the CO2 emmision from other materials, the element in GeometryRule.py need to be changed in addition to that 
