#clase que almacena una lista de actividades

from CargarActividadesJson import CargarActividadesJson
from actividad import Actividad

class ListaActividades: 
   
     def __init__(self, fichero):
          self.activity_list = []
          self.cargador = CargarActividadesJson(fichero)

     def add_actividad(self,actividad):
          self.cargador.add(actividad)
    
     def rmv_actividad(self,actividad):
          self.cargador.rmv(actividad)
