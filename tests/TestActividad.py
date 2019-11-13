import unittest

import sys
sys.path.append('../src/')
from actividad import Actividad

class test_actividad(unittest.TestCase):

    def test_init(self):
        acttest=Actividad("Hola","Prueba","12/3/1997")
        self.assertEqual(acttest.get_nombre(),"Hola")
        self.assertEqual(acttest.get_descripcion(),"Prueba")
        self.assertEqual(acttest.get_fecha(),"12/3/1997")
        self.assertTrue(acttest.get_estado())
    
    def test_cerrar(self):
        acttest=Actividad("Hola","Prueba","12/3/1997")
        acttest.cerrar_actividad()
        self.assertFalse(acttest.get_estado())

if __name__=='__main__':
    unittest.main()
    