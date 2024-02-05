'''
Un tablero de damas consta de 64 cuadros distribuidos en una cuadricula de 8x8
filas y columnas.

Necesitamos construir un objeto TABLERO.

El objeto TABLERO debe disponer de los siguientes metodos y atributos:
	1) Poder dibujar su contenido en pantalla
	2) Poder cambiar el contenido de una celda
	3) Debe disponer de un menu con el que puedas decidir que accion
	ejecutar
	4) Debe poder guardar el tablero actual con un nombre cualquiera en
	formato .txt y permitir recargarlo
	5) Debe poder borrar todo el tablero
	6) Debe poder rellenar todo el tablero
	7) Los cuadros vacios y los cuadros rellenos deben ser indicados por
	una variable determinada para cada caracter
	8) Crear un objeto usuario

Utilice la libreria BeautifulTable 
	from beautifultable import BeautifulTable
	table = BeautifulTable(maxwidth=1000)
	table.columns.header = ['A1', 'A2', .....]
	table.rows.append([1, 2])
	table.rows.append([3,4])	
	print(table)
'''

from beautifultable import BeautifulTable
import sys

class Tablero_damas:

    def __init__(self):
        
        self.t_celdas = BeautifulTable(maxwidth=1000)
        self.t_celdas.columns.header = [chr(letter) for letter in range(65, 73)]
        for row in range(1, 9):
            self.t_celdas.rows.append([chr(letter) + str(row) for letter in range(65, 73)])

        self.nombres_ins_casillas = []
        for letter in range(65, 73):
            for num in range(1, 9):
                self.nombres_ins_casillas.append('{}{}'.format(chr(letter), num))

        self.casillas = {}
        for nombre in self.nombres_ins_casillas:
            instancia = Casilla_damas(nombre, self)
            self.casillas[nombre] = instancia


    def borrar_todo(self):

        self.__init__()
            
    def contar_vacios(self):

        empties = []

        for row in self.t_celdas.rows:
            for spot in row:
                if spot != '##':
                    empties.append(spot) 

        return len(empties)
                    
    def imprimir(self):
        
        print(self.t_celdas)

    def exportar(self):

        nombre_archivo = input('Pon un nombre al archivo .txt a exportar: ') + '.txt'
        stdout_original = sys.stdout
        with open(nombre_archivo, 'w') as archivo:

            sys.stdout = archivo
            self.imprimir()
            
        sys.stdout = stdout_original
        print('Archivo exportado')
        
class Casilla_damas:

    def __init__(self, valor:str, tablero: object):

        self.valor = valor
        self.tablero = tablero

    def borrar(self):

        row = [str(num) for num in range(1, 9)].index(self.valor[1])
        col = [chr(letter) for letter in range(65, 73)].index(self.valor[0])

        self.tablero.t_celdas.rows[row][col] = self.valor

    def asignar(self):

        row = [str(num) for num in range(1, 9)].index(self.valor[1])
        col = [chr(letter) for letter in range(65, 73)].index(self.valor[0])

        if self.tablero.t_celdas.rows[row][col] == '##':
            print('Esta casilla ya estaba asignada de antes.')
        else:
            self.tablero.t_celdas.rows[row][col] = '##'


intro = '''REGLAS:
1) Esta practica esta diseñada para un tablero de damas 8x8 con 64 casillas.
2) En un principio no existe un tablero creado, de modo que lo primero que haremos sera crear nuestro tablero con el comando:
nombre_que_queramos = Tablero_damas()
3) Una vez creado el tablero, las casillas vacias estan indicadas con su nombre siguiendo el esquema de tableros de ajedrez (A3, H8, C5 o la que sea) y las casillas ocupadas estan indicadas mediante '##'
4)Podemos generar tantos tableros como queramos
5)METODOS DEL TABLERO:
- si queremos echar un ojo al tablero utilizamos el metodo .imprimir() y se nos mostrara el estado actual en consola.
- si queremos resetearlo utilizamos el metodo .borrar_todo().
- si queremos exportar el estado actual del tablero utilizamos el metodo .exportar(). Este nos pedira que nombremos el archivo de salida (no hay necesidad de poner la terminacion .txt. Si exportamos el mismo tablero u otro distinto indicando el mismo nombre al archivo de salida sobreescribiremos el archivo anterior)
- el archivo se exportara a la carpeta donde almecenamos este programa .py
- si queremos comprobar cuantas casillas permanecen vacias utilizamos el metodo .contar_vacios()

6)METODOS DE LAS CASILLAS:
- si queremos ocupar/rellenar una de las casillas debemos utilizar el metodo .asignar() con la siguiente linea de codigo
nombre_del_tablero.casillas.get(casilla_a_ocupar).asignar()  *Poner la letra en mayuscula
si introducimos una casilla inexistente dara error, si introducimos una casilla ya ocupada nos lo notificara.
- si queremos ocupar varias casillas a la vez podemos utilizar un bucle for como por ejemplo:
for casilla in ['A1', 'A2', 'A3']:
    nombre_del_tablero.casillas.get(casilla).asignar()
    
en este caso es necesario presionar enter un par de veces.
- si queremos liberar una casilla rellena anteriormete utilizamos el metodo .borrar() con la siguiente linea de codigo:
nombre_del_archivo.casillas.get(casilla_a_liberar).borrar()

ESTE TABLERO ESTA DISEÑADO PARA UTILIZARSE DIRECTAMENTE DESDE LA TERMINAL UTILIZANDO LOS METODOS INDICADOS.'''

print(intro)




