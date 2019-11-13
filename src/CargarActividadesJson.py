import json
from actividad import Actividad
import os

class CargarActividadesJson: 
    
    def __init__(self, fichero):
        self.my_fichero = fichero
        self.activity_list = {}
        
        with open(self.my_fichero, 'r') as json_file:
            self.activity_list = json.load(json_file)


    def add(self, actividad):
        if actividad.nombre not in self.activity_list.keys():
            self.activity_list[actividad.nombre] = actividad.to_dict()
        
        self.__reescribirfichero()

    def rmv(self, actividad):
        self.activity_list.pop(actividad.nombre, None)
        self.__reescribirfichero()

    def __reescribirfichero(self):
        #js = json.dumps(self.activity_list)
        with open(self.my_fichero, 'w') as outfile:
            outfile = json.dump(self.activity_list, outfile)
        
    
if __name__ == "__main__":
    c = CargarActividadesJson("lista.json")
    act = Actividad("Prueba","Prueba","11/11/11")
    c.add(act)