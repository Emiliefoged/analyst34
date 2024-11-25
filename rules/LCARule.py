import pandas as pd
import numpy as np

# Definer den fulde sti til CSV-filen (inklusive filnavn)
csvfil = "C:/Users/Emilie Foged Larsen/Dropbox/Pc/Documents/GitHub/analyst34/rules/materials.csv" 

# Indlæs CSV-filen direkte
try:
    df = pd.read_csv(csvfil)

    volumen = 10

    # Beregn vægten (Density * Volume)
    df["Weight [kg]"] = df["Density [kg/m3]"] * volumen

    # Beregn CO₂-ækvivalenten (Weight * CO2 per kg)
    df["CO2 Equivalent [kgCO2]"] = df["Weight [kg]"] * df["CO2 [kgCO2]"]

    # Vis kun kolonnerne Material, Weight, og CO2 Equivalent
    print(df[["Material", "Weight [kg]", "CO2 Equivalent [kgCO2]"]])

except FileNotFoundError:
    print("CSV-filen blev ikke fundet. Tjek stien og filnavnet.")
except KeyError as e:
    print(f"En kolonne blev ikke fundet i dataframen: {e}")
except Exception as e:
    print(f"Der opstod en fejl: {e}")