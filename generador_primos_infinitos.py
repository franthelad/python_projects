def contador_infinito(num):
    while True:
        yield num
        num += 1

contador = contador_infinito(2)

def primos():
    
    for numerador in contador: 
        divisores = []
        for divisor in range(1, numerador+1): 
            if numerador % divisor == 0:
                divisores.append(divisor)
            if len(divisores) > 2:
                break
        if len(divisores) == 2:
            yield numerador     

enumerador_primos = primos()
print(next(enumerador_primos))
