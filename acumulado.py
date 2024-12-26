import openpyxl as xls
from shareplum import Office365
from config import *
import json

class ExtractorInventario:
    def __init__(self):
        self.username, self.password = self._credencials()
        self.authcookie = Office365(SITE, self.username, self.password).get_cookies()
        self.inventario = pd.concat(
            [pd.read_csv(DF_COSTA), pd.read_csv(DF_CENTRO_SUR)],
            ignore_index=True
            )

    def _credencials(self):
        with open("secrets\\microsoft.json") as file:
            credencials = json.load(file)
            return credencials["username"], credencials["password"]
        
       
if __name__=="__main__":
    pass