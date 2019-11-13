import unittest
import filecmp

import sys
sys.path.append('../src/')
from ListaActividades import ListaActividades
from actividad import Actividad

class test_lista_actividades(unittest.TestCase):
    def setUp(self):
        self.lista = ListaActividades("fichero_test.json")

    def test_add(self):
        self.lista.add_actividad(Actividad("Prueba","Prueba","11/11/11"))
        self.assertTrue(filecmp.cmp('fichero_test.json','fichero_resultado_add.json'))

    def test_rmv(self):
        self.lista.rmv_actividad(Actividad("Prueba","Prueba","11/11/11"))
        self.assertTrue(filecmp.cmp('fichero_test.json','fichero_resultado_rmv.json'))

if __name__=='__main__':
    unittest.main()