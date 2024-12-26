import folium
import pandas as pd

# URLS Inventario nacional
DF_COSTA = "https://docs.google.com/spreadsheets/d/18xa5ajZsuwYpFRe9OCglfAY9oxs5nxEVs_5fpvfifmA/export?format=csv"
DF_CENTRO_SUR = "https://docs.google.com/spreadsheets/d/1Aae9GM7MXF0n5tWuagNIqWLPKyAKpr-3urMpluT4zPI/export?format=csv"

# URLS Sharepoint
SITE = "https://gbconnect.sharepoint.com/"
SITE_KARDEX = "https://gbconnect.sharepoint.com/sites/MovimientosKardex/"

# Iconos del mapa
TRUCK_ICON = folium.CustomIcon(
    icon_image="image\\camion.png",
    icon_size=(45,45)
)

DF_MARKETS = pd.read_csv("database\\direcciones_locales.csv", sep=";")