from geotab import ExtractorGeotab
from streamlit_folium import st_folium
from config import *
import folium
import streamlit as st


class InterfazVehiculos:
    """
    ### Interfaz de la app de seguimiento de conductores
    
    >>> muestra el mapa de los camiones.
    >>> muestra la ubicación de los locales y su inventario teórico.

    """
    def __init__(self):
        st.set_page_config(
            page_title="Seguimiento vehiculos - IDEAL", 
            page_icon="image\\Logo ideal SA.jfif", 
            layout="wide", 
            initial_sidebar_state="expanded")

    @staticmethod
    @st.cache_data(ttl=120)
    def obtener_ubicacion_cache(filtro):
        return ExtractorGeotab().obtener_ubicaciones(filtro)
    
    @staticmethod
    @st.cache_data(ttl=120)
    def camiones():
        return ExtractorGeotab().base_conductores()

    def main(self):
        st.title("Seguimiento camiones Ideal")

        tab1, tab2 = st.tabs(["Manual de uso", "Seguimiento recogidas"])
        
        with tab2:

            truck = st.selectbox(
                "Elije el número de camión", 
                self.camiones()["NUMERO"].to_list())
            
            filtro = self.camiones()[self.camiones()["NUMERO"] == truck].reset_index().loc[0, "id"]
            camion = self.obtener_ubicacion_cache(filtro=filtro)
            mapa = folium.Map(location=[camion["latitud"], camion["longitud"]], zoom_start=12)

            folium.Marker(
                location=[camion["latitud"], camion["longitud"]],
                popup=f"Camión {truck}",
                icon=TRUCK_ICON
            ).add_to(mapa)

            for index, row in DF_MARKETS.iterrows():
                try:
                    folium.Marker(
                        location=[float(row["Lat"]), float(row["Lng"])],
                        popup=f"""Ruta {row['Código de Dirección']}\n{row["Nombre de Dirección"]}""",
                        icon=folium.Icon(color="red", icon="info-sign")
                        ).add_to(mapa)
                except Exception as e:
                    print(f"Error al procesar la fila {index}: {e}")

            st_folium(mapa, width=1980, height=600)
        
if __name__=="__main__":
    InterfazVehiculos().main()