from geotab import ExtractorGeotab
import streamlit as st


class InterfazVehiculos:
    """
    ### Interfaz de la app de seguimiento de conductores
    
    >>> muestra el mapa de los camiones.
    >>> muestra la ubicación de los locales y su inventario teórico.

    """
    def __init__(self):
        st.set_page_config("Seguimiento vehiculos - IDEAL", "image\\Logo ideal SA.jfif", "wide", "collapsed")
        self.pag = ["Menú principal", "Mapa conductores"]
        self.seleccion_pag = st.sidebar.selectbox("Páginas", self.pag)
        self.geotab = ExtractorGeotab()

    def main(self):
        if self.seleccion_pag == "Menú principal":
            st.title("Este es el el titulo del Menu principal")
            st.text(self.geotab.obtener_ubicaciones())

        elif self.seleccion_pag == "Mapa conductores":
            st.title("Este es el mapa de los conductores")


if __name__=="__main__":
    InterfazVehiculos().main()