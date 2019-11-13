import unittest
import filecmp

import sys
sys.path.append('../src/')
from CargarActividadesJson import CargarActividadesJson
from actividad import Actividad

class test_cargar_actividades(unittest.TestCase):
    def setUp(self):
        self.cargador = CargarActividadesJson("fichero_test.json")

    def test_add(self):
        self.cargador.add(Actividad("Prueba","Prueba","11/11/11"))
        self.assertTrue(filecmp.cmp('fichero_test.json','fichero_resultado_add.json'))

    def test_rmv(self):
        self.cargador.rmv(Actividad("Prueba","Prueba","11/11/11"))
        self.assertTrue(filecmp.cmp('fichero_test.json','fichero_resultado_rmv.json'))

if __name__=='__main__':
    unittest.main()