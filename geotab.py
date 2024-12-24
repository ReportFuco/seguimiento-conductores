from mygeotab import API
from datetime import timedelta
import json

class ExtractorGeotab:
    """Esta clase es para extraer la información georeferenciada
    de los conductores de control de equipos en tiempo real"""
    def __init__(self):
        self.username, self.password, self.database = self._credencials()
        self.api = API(self.username, self.password, self.database)
        self.api.authenticate()

    @staticmethod
    def hora_actual():
        from datetime import datetime, timezone
        return datetime.now(timezone.utc)

    def _credencials(self):
        with open("secrets\\geotab.json", "r") as file:
            credencials = json.load(file)
            return credencials["username"], credencials["password"], credencials["database"]
        
    def obtener_ubicaciones(self, dispositivo_id):
        ahora = (self.hora_actual() - timedelta(minutes=5)).isoformat()
        try:
            lgo_records = self.api.call(
                "Get", 
                typeName="LogRecord", 
                search={"fromDate": ahora, "deviceSearch": {"id": dispositivo_id}}
            )
            if lgo_records:
                log = lgo_records[0]
                return {
                    "dispositivoId": log["device"]["id"],
                    "latitud": log["latitude"],
                    "longitud": log["longitude"],
                    "tiempo": log["dateTime"]
                }
            else:
                return None
        except Exception as e:
            print(f"Error al obtener ubicaciones: {e}")
            return None
        
    def obtener_dispositivos(self):
        """Lista todos los dispositivos registrados en MyGeotab."""
        try:
            dispositivos = self.api.call("Get", typeName="Device")
            return [{"id": d["id"], "name": d["name"]} for d in dispositivos]
        except Exception as e:
            print(f"Error al obtener dispositivos: {e}")
            return []


if __name__=="__main__":
    print(ExtractorGeotab().obtener_dispositivos())