import unittest
from main import sumar, restar, multiplicar, dividir

class TestSumar(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(5,4),9)
        self.assertEqual(sumar(5,1),6)
        self.assertEqual(sumar(0,-3),-3)

    def test_restar(self):
        self.assertEqual(restar(5,2),3)
        self.assertEqual(restar(7, 0),7)
        self.assertEqual(restar(2, 2),0)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(5,8),40)
        self.assertEqual(multiplicar(5,-2),-10)
        self.assertEqual(multiplicar(-1,-3),3)

    def test_dividir(self): #El divisor nunca va a ser 0 ya que el usuario nunca va a poder insertar el 0 (Mirar el main.py)
        self.assertEqual(dividir(5,5),1)
        self.assertEqual(dividir(5,-1),-5)
        self.assertEqual(dividir(10,3),3.33)

    

if __name__ == '__main__':
    unittest.main()
    

