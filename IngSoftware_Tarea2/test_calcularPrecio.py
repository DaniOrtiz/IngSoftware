'''
Created on 21/4/2015

@author: Dani
'''
import unittest
from calcularPrecio import Tarifa,calcularPrecio
import datetime

class Test_calcularPrecio(unittest.TestCase):


    def test0Timer(self):
    # Caso de prueba tiempo de reservación = (0) minutos
        tarifa_de_prueba = Tarifa(5,7)
        ini_reserva = datetime.datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime.datetime(2015, 4, 21, 6, 15)
        tiempo_reserva = [ini_reserva,fin_reserva]
        calcularPrecio(tarifa_de_prueba, tiempo_reserva)
        
    def test15MinTimer(self):
    # Caso de prueba tiempo de reservación = (15) minutos
        tarifa_de_prueba = Tarifa(5,7)
        ini_reserva = datetime.datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime.datetime(2015, 4, 21, 6, 30)
        tiempo_reserva = [ini_reserva,fin_reserva]
        d = calcularPrecio(tarifa_de_prueba, tiempo_reserva)
        self.assertEqual(d,5) # Arroja un error, la función calcularPrecio 
                              # realiza los cálculos en función a los minutos 
        
    def test1Hour1MinTimer(self):
    # Caso de prueba tiempo de reservación = (1) hora, (1) minuto
        tarifa_de_prueba = Tarifa(5,7)
        ini_reserva = datetime.datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime.datetime(2015, 4, 21, 7, 16)
        tiempo_reserva = [ini_reserva,fin_reserva]
        d = calcularPrecio(tarifa_de_prueba, tiempo_reserva)
        self.assertEqual(d,10) # Arroja un error, la función calcularPrecio 
                               # realiza los cálculos en función a los minutos 
                               # Me da el precio de exactamente 1h1min no el de 
                               # 2 horas.
        
    def test7DaysTimer(self):
     # Caso de prueba tiempo de reservación = (7) días
        tarifa_de_prueba = Tarifa(5,7)
        ini_reserva = datetime.datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime.datetime(2015, 4, 28, 6, 15)
        tiempo_reserva = [ini_reserva,fin_reserva]
        calcularPrecio(tarifa_de_prueba, tiempo_reserva)
    
    def test7Days1MinTimer(self):
    # Caso de prueba tiempo de reservación = (7) días, (1) minuto
        tarifa_de_prueba = Tarifa(5,7)
        ini_reserva = datetime.datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime.datetime(2015, 4, 28, 6, 16)
        tiempo_reserva = [ini_reserva,fin_reserva]
        d = calcularPrecio(tarifa_de_prueba, tiempo_reserva)
    
    def testNegativeTimer(self):
    # Caso de prueba tiempo de reservación Negativo
        tarifa_de_prueba = Tarifa(5,7)
        ini_reserva = datetime.datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime.datetime(2015, 4, 20, 6, 15)
        tiempo_reserva = [ini_reserva,fin_reserva]
        calcularPrecio(tarifa_de_prueba, tiempo_reserva)
        
    def testNegativeTarifa(self):
    # Caso de prueba tarifa negativa
        tarifa_de_prueba = Tarifa(-5,-7)
        ini_reserva = datetime.datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime.datetime(2015, 4, 27, 6, 15)
        tiempo_reserva = [ini_reserva,fin_reserva]
        calcularPrecio(tarifa_de_prueba, tiempo_reserva)
        
    def testImaginaryTarifa(self):
    # Caso de prueba tarifa imaginaria
        tarifa_de_prueba = Tarifa(5j,7j)
        ini_reserva = datetime.datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime.datetime(2015, 4, 27, 6, 15)
        tiempo_reserva = [ini_reserva,fin_reserva]
        calcularPrecio(tarifa_de_prueba, tiempo_reserva)
        
    def testDecimalTimer(self):
    # Caso de prueba tiempo de reservación decimal
        tarifa_de_prueba = Tarifa(5,7)
        ini_reserva = datetime.datetime(2015, 4, 21, 6, 15.3)
        fin_reserva = datetime.datetime(2015, 4, 27, 6, 15.3)
        tiempo_reserva = [ini_reserva,fin_reserva]
        calcularPrecio(tarifa_de_prueba, tiempo_reserva)
        
    def testSecondsTimer(self):
    # Caso de prueba tiempo de reservación con segundos
        tarifa_de_prueba = Tarifa(5,7)
        ini_reserva = datetime.datetime(2015, 4, 21, 6, 15, 2)
        fin_reserva = datetime.datetime(2015, 4, 22, 6, 15, 2)
        tiempo_reserva = [ini_reserva,fin_reserva]
        calcularPrecio(tarifa_de_prueba, tiempo_reserva)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()