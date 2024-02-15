from math import sqrt

class Primes:

    def __init__(self, rango):

        self.__rango = rango
        self.__numero = 1

    def __iter__(self):

        return self

    def __next__(self):

        while True:
            
            self.__numero += 1

            if self.__numero > self.__rango:
                raise StopIteration

            cuadrado = sqrt(self.__numero)
            valido = True
            for i in range(2, int(cuadrado) + 1):
                if self.__numero % i == 0:
                    valido = False

            if valido == True:
                return self.__numero


for i in Primes(10000):
    print(i, end = ',')
    

