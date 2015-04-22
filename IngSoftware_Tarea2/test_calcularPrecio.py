'''
Created on 21/4/2015

@author: Dani
'''
import unittest
from calcularPrecio import Tarifa,calcularPrecio
from datetime import datetime

class Test_calcularPrecio(unittest.TestCase):


    def test0Timer(self):
        # Caso de prueba tiempo de reservacion = (0) minutos
        tarifa_de_prueba = Tarifa(5,7)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 21, 6, 15)
        tiempo_reserva = [ini_reserva,fin_reserva]
        calcularPrecio(tarifa_de_prueba, tiempo_reserva)
        
    def test0Tarifa(self):
        # Caso de prueba Tarifa(0,0)
        tarifa_de_prueba = Tarifa(0,0)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 28, 6, 10)
        tiempo_reserva = [ini_reserva,fin_reserva]
        calcularPrecio(tarifa_de_prueba, tiempo_reserva)    
    
    def test14MinTimer(self):
        # Caso de prueba tiempo de reservacion = (14) minutos
        tarifa_de_prueba = Tarifa(5,7)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 21, 6, 29)
        tiempo_reserva = [ini_reserva,fin_reserva]
        calcularPrecio(tarifa_de_prueba, tiempo_reserva)           
        
    def test15MTimeSmallT(self):
        # Caso de prueba tiempo de reservacion = (15) minutos, tarifa pequenia
        tarifa_de_prueba = Tarifa(0.01,0.01)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 21, 6, 30)
        tiempo_reserva = [ini_reserva,fin_reserva]
        d = calcularPrecio(tarifa_de_prueba, tiempo_reserva)
        self.assertEqual(d,5) 
            
    def test7DaysTimer(self):
        # Caso de prueba tiempo de reservacion = (7) dias
        tarifa_de_prueba = Tarifa(5,7)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 28, 6, 15)
        tiempo_reserva = [ini_reserva,fin_reserva]
        calcularPrecio(tarifa_de_prueba, tiempo_reserva)
    
    def test7Days1MinTimer(self):
        # Caso de prueba tiempo de reservacion = (7) dias, (1) minuto
        tarifa_de_prueba = Tarifa(5,7)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 28, 6, 16)
        tiempo_reserva = [ini_reserva,fin_reserva]
        calcularPrecio(tarifa_de_prueba, tiempo_reserva)
       
    
    def testNegativeTimer(self):
        # Caso de prueba tiempo de reservacion Negativo
        tarifa_de_prueba = Tarifa(5,7)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 20, 6, 15)
        tiempo_reserva = [ini_reserva,fin_reserva]
        calcularPrecio(tarifa_de_prueba, tiempo_reserva)
        
    def testNegativeTarifa(self):
        # Caso de prueba tarifa negativa
        tarifa_de_prueba = Tarifa(-2,-1)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 27, 6, 15)
        tiempo_reserva = [ini_reserva,fin_reserva]
        calcularPrecio(tarifa_de_prueba, tiempo_reserva)
        
    def testImaginaryTarifa(self):
        # Caso de prueba tarifa imaginaria
        tarifa_de_prueba = Tarifa(5j,7j)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 27, 6, 15)
        tiempo_reserva = [ini_reserva,fin_reserva]
        calcularPrecio(tarifa_de_prueba, tiempo_reserva)
        
    def testCharTimer(self):
        # Caso de prueba tiempo de reservacion con caracteres
        tarifa_de_prueba = Tarifa("a","b")
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 27, 6, 15)
        tiempo_reserva = [ini_reserva,fin_reserva]
        calcularPrecio(tarifa_de_prueba, tiempo_reserva)
        
    def testDecimalTimer(self):
        # Caso de prueba tiempo de reservacion decimal
        tarifa_de_prueba = Tarifa(5,7)
        ini_reserva = datetime(2015, 4, 21, 6, 15.3)
        fin_reserva = datetime(2015, 4, 27, 6, 16.5)
        tiempo_reserva = [ini_reserva,fin_reserva]
        calcularPrecio(tarifa_de_prueba, tiempo_reserva)
    
    def testDecimal1Tarifa(self):
        # Caso de prueba Tarifa decimal 1
        tarifa_de_prueba = Tarifa(0.001,0.001)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 27, 6, 15)
        tiempo_reserva = [ini_reserva,fin_reserva]
        calcularPrecio(tarifa_de_prueba, tiempo_reserva)
        
    def testDecimal2Tarifa(self):
        # Caso de prueba Tarifa decimal 2
        tarifa_de_prueba = Tarifa(5.4,7.6)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 27, 6, 15)
        tiempo_reserva = [ini_reserva,fin_reserva]
        calcularPrecio(tarifa_de_prueba, tiempo_reserva)
        
    def testSecondsTimer(self):
        # Caso de prueba tiempo de reservacion con segundos
        tarifa_de_prueba = Tarifa(5,7)
        ini_reserva = datetime(2015, 4, 21, 6, 15, 2)
        fin_reserva = datetime(2015, 4, 22, 6, 15, 3)
        tiempo_reserva = [ini_reserva,fin_reserva]
        calcularPrecio(tarifa_de_prueba, tiempo_reserva)

    def testBigTarifa(self):
        # Caso de prueba tarifa muy grande
        tarifa_de_prueba = Tarifa(2**31,2**64)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 27, 6, 15)
        tiempo_reserva = [ini_reserva,fin_reserva]
        calcularPrecio(tarifa_de_prueba, tiempo_reserva)
        
    def testTimerMax(self):
        # Caso de prueba tiempo de resevacion maximo
        tarifa_de_prueba = Tarifa(2,3)
        ini_reserva = datetime.max + 1
        fin_reserva = datetime(2015, 4, 27, 6, 15)
        tiempo_reserva = [ini_reserva,fin_reserva]
        calcularPrecio(tarifa_de_prueba, tiempo_reserva)
    
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()