# Introduction
BIManalyst group 34
This group consists of Emilie Foged (S203742), Ene Holst Møller (S203711) and Freja Thybo (S204847)	

**Focus area**: Materials/LCA

We made a tool for calculating the carbon footprint (CO2) of tree different floor materials. Before using the tool you need to have access to an IFC file with specific volumens for the materials. In this code we used CES_BLD_24_06_ARC which is available in this course. You also have to be familiar with an LCA database, in this case we used Ecoinvent where the global warming potential is defined with the unit kg CO2-eq.

# Using the tool
You'll need to know the density [kg/m3] and CO2 emmisions [kgCO2-eq] for every material. This is essential for the calculation to work. When using this code this information is already included, so it's easy to run it. If you would like to calculate the CO2 emmision from other materials, the element in GeometryRule.py need to be changed in addition to the element type. The code works just by copying it into Visual Studio Code or Blender/Bonsai.

# Tutorials
A video tutorial is made to illustrate how to use the tool, this is found here: **Insert Link**. Before running the script, make sure that your IFC model has quantities added.

Furthermore a Jupitor notebook is made to take you though the code step by step. 

Here is a snapshot of the code:

