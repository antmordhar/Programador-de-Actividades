class Actividad:
    def __init__(self, nombre,descripcion,fecha):
        self.nombre=nombre
        self.descripcion=descripcion
        self.fecha=fecha
        self.activa=True

    def cerrar_actividad(self):
        if self.activa==True:
            self.activa=False
    
    def cambiar_descripcion(self,new_descripcion):
        self.descripcion=new_descripcion
    
    def cambiar_nombre(self,new_nombre):
        self.nombre=new_nombre

    def cambiar_fecha(self,new_fecha):
        self.fecha=new_fecha
    
    def get_nombre(self): 
        return self.nombre
    
    def get_descripcion(self): 
        return self.descripcion
    
    def get_fecha(self):
        return self.fecha
    
    def get_estado(self):
        return self.activa

    
