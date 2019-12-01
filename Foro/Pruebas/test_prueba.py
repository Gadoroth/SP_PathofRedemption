import unittest
from prueba import ValidUser,ValidPass

class  TestValidUser(unittest.TestCase):
    def test_usuario(self):
        self.assertAlmostEqual(ValidUser("j.perez"),"j.perez")
        self.assertAlmostEqual(ValidUser("p.munoz"),"p.munoz")
        self.assertAlmostEqual(ValidUser("asd"),"dsa") #ERROR


class TestValidPass(unittest.TestCase):
    def test_contraseña(self):
        self.assertAlmostEqual(ValidPass("Duoc.2019"),"Duoc.2019")
        self.assertAlmostEqual(ValidPass("Duoc.2019"),"asd") #ERROR


