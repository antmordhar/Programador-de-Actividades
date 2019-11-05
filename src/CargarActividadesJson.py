import json
from ListaActividades import ListaActividades

class CargarActividadesJson(ListaActividades): 
    
    def __init__(self,fichero):
        self.my_fichero=fichero
        super().activity_list=json.loads(self.my_fichero)
    def __reescribirfichero(self):
        self.my_fichero=json.dumps(super().activity_list)