class Menu:

    def __init__(self):
        #CREO UNA LISTA PARA ALMACENAR LOS TABLEROS QUE SE VAYAN GENERANDO
        self.lista_tableros = []

    def mostrar_menu(self):
        
        print('\nBIENVENIDO AL MUNDO DE LOS TABLEROS DE DAMAS!!')

        while True:
            print('''
Que quieres hacer?
1) Crear un tablero
2) Borrar un tablero
3) Ver lista de tableros
4) Seleccionar un tablero
5) Cerrar programa

    Si cierras el programa y quieres volver escribe "jugar" y pulsa intro. \n''')

            ans = input('Selecciona una opcion: ')

            if ans == '1':
                self.crear_tablero()
            elif ans == '2':
                self.borrar_tablero()
            elif ans == '3':
                self.mostrar_tableros()
            elif ans == '4':
                self.seleccionar_tablero()
            elif ans == '5':
                break
            else:
                print('Esa opcion no es valida ceporrin!')
            

    def crear_tablero(self):
        #CREO UNA INSTANCIA DE TABLERO 
        tablero = Tablero()
        
        #LLENO EL TABLERO DE CASILLAS Y LA ALMACENO EN LA LISTA DE TABLEROS
        tablero.crear_casillas()
        self.lista_tableros.append(tablero)
        print('\nTablero {} creado!'.format(self.lista_tableros[-1]))

    def borrar_tablero(self):
        #SI NO HAY TABLEROS DISPONIBLES LANZA MENSAJE AL RESPECTO.
        if len(self.lista_tableros) == 0:
            print('\nNo tienes tableros operativos =(')
        else:
            #PIDO AL USUARIO QUE ME INDIQUE EL TABLERO QUE DESEA ELIMINAR Y LO ELIMINAMOS DE LA LISTA
            #GENERO UN BUCLE WHILE PARA ASEGURARNOS QUE EL USUARIO NO INTRODUCE UN INDICE DE TABLERO INVALIDO
            elim = int(input('\nSelecciona el tablero a eliminar acorde a su posicion en la lista: ')) - 1
            while (elim >= len(self.lista_tableros)) or (elim < 0):
                elim = int(input('\nIndice invalido, introduce un tablero valido. Si quieres volver atras introduce "999" ')) - 1
                if elim == 998:
                    return None
                
            print('\nTablero {} fue eliminado!!'.format(self.lista_tableros[elim]))
            del self.lista_tableros[elim]
        
    def mostrar_tableros(self):
        #IMPRIMO LA LISTA DE TABLEROS
        print(self.lista_tableros)

    def seleccionar_tablero(self):

        tab = int(input('\nSelecciona un tablero acorde a su posicion en la lista: ')) - 1
        while (tab >= len(self.lista_tableros)) or (tab < 0):
            tab = int(input('\nIndice invalido, introduce un tablero valido: ')) - 1

        submenu = SubMenuTablero(self.lista_tableros[tab])
        return submenu.mostrar_opciones()

class SubMenuTablero(Menu):

    def __init__(self, tablero: object):

        self.tablero = tablero

    def mostrar_opciones(self):

        print('\nHas seleccionado el tablero, que quieres hacer ahora?')
        while True:
            print('''
1) Ocupar Casilla
2) Desocupar Casilla
3) Volver atras''')
        
            ans = input('\nElige una opcion de las dadas: ')
            if ans == '1':
                  self.ocupar_casilla()
            elif ans == '2':
                self.vaciar_casilla()
            elif ans == '3':
                break
            else:
                print('\nOpcion invalida, repetimos...')
                

    def ocupar_casilla(self):
        #PIDO AL USUARIO QUE INDIQUE LA CASILLA
        cas = input('\nQue casilla quieres ocupar? Utiliza la nomenclatura (fila)_(columna), "2_5", "4_7", "8_2", etc. Si quieres volver a atras introduce "999" ')
        if cas == '999':
            return self.mostrar_opciones()
            
        while (cas[0].isdigit() == False) or (cas[2].isdigit() == False) or (cas[1] != '_') or (len(cas) != 3) or (int(cas[0]) not in range(1, 9)) or (int(cas[2]) not in range(1, 9)):
            print('\nHas introducido una casilla incorrecta, prueba otra vez.')
            cas = input('\nQue casilla quieres ocupar? Utiliza la nomenclatura (fila)_(columna), "2_5", "4_7", "8_2", etc.  Si quieres volver a atras introduce "999" ')
            if cas == '999':
                return self.mostrar_opciones()
            
        for fila in self.tablero.casillas:
            for casilla in fila:
                if cas == casilla.nombre:
                    if casilla.ocupado == True:
                        print('\nYa ocupaste esta casilla anteriormente.')
                    else:
                        casilla.ocupado = True
                        print('\nCasilla {} ocupada!'.format(cas))
        

    def vaciar_casilla(self): 
        cas = input('\nQue casilla quieres desocupar? Utiliza la nomenclatura (fila)_(columna), "2_5", "4_7", "8_2", etc. Si quieres volver a atras introduce "999"')
        while (int(cas[0]) not in range(1, 9)) and (int(cas[2]) not in range(1, 9)) and (cas[1] != '_'):
            print('\nHas introducido una casilla incorrecta, prueba otra vez.')
            cas = input('\nQue casilla quieres desocupar? Utiliza la nomenclatura (fila)_(columna), "2_5", "4_7", "8_2", etc.  Si quieres volver a atras introduce "999"')

        if cas == '999':
            self.mostrar_opciones()
            
        for fila in self.tablero.casillas:
            for casilla in fila:
                if cas == casilla.nombre:
                    if casilla.ocupado == False:
                        print('\nEsta casilla no esta ocupada.')
                    else:
                        casilla.ocupado = False
                        print('\nCasilla {} desocupada!'.format(cas))



class Tablero():

    def __init__(self):
        #CREO UNA LISTA PARA ALMACENAR LAS CASILLAS DEL TABLERO, LA IDEA ES UNA MATRIZ 8X8 / FILASxCOLUMNAS
        self.casillas = []

    def crear_casillas(self):
        #GENERO LAS 64 CASILLAS DEL TABLERO EN UNA MATRIZ 8X8
        #SE NOMBRAN EN RELACION (FILA)_(COLUMNA)
        for row in range(1, 9):
            self.casillas.append([])
            for col in range(1, 9):
                self.casillas[-1].append(Casilla('{}_{}'.format(row, col)))


class Casilla():

    def __init__(self, nombre: str, ocupado = False):
        #BOOLEANO QUE INDICA SI ESTA OCUPADA O LIBRE Y NOMBRE POR DEFECTO
        self.nombre = nombre
        self.ocupado = ocupado


menu = Menu()
menu.mostrar_menu()







    
