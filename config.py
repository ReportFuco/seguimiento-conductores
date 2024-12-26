import folium
import pandas as pd

# URLS Inventario nacional


# URLS Sharepoint
SITE = "https://gbconnect.sharepoint.com/"
SITE_KARDEX = "https://gbconnect.sharepoint.com/sites/MovimientosKardex/"


# Iconos del mapa
TRUCK_ICON = folium.CustomIcon(
    icon_image="image\\camion.png",
    icon_size=(45,45)
)

DF_MARKETS = pd.read_csv("database\\direcciones_locales.csv", sep=";")