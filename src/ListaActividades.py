class ListaActividades: 
   
   def __init__(self):
       self.activity_list = []

    def add_actividad(self,actividad):
        self.activity_list.append(actividad)
    
    def rmv_actividad(self,actividad):
        self.activity_list.remove(actividad)

