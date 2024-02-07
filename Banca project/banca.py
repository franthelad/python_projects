'''Creo varios objetos para trabajar con ellos:
-User, desde aqui arrancaremos la salida de inicio para validar usuario principalmente.
-Banco, que conformara un atributo de los usuarios
-Tipo de usuarios (Administrador, Cajero y Usuario) con distintas funcionalidades
'''
class User:
    
    lista_users = [] #Una lista para almacenar los users que se vayan creando (Administradores, Cajeros y Usuarios)
    
    def __init__(self):

        pass

    def validacion(self): #Para validar User y  password

        while True: #Bucle para pedir validacion continuamente. Programa en continua ejecucion hasta que forcemos un error
            print('\n--BIENVENIDO A LA APP DE GESTION BANCARIA--\n')
            nombre = input('Introduce nombre de user: ')
            for user in User.lista_users: #Verificamos que el nombre de user introducido existe en nuestra lista de users 
                existe = False #Salida del bucle for 
                if user.nombre == nombre:
                    existe = True #Cuando encontramos el nombre del user podemos romper el bucle de busqueda
                    usuario = user
                    break
            if existe == False:
                print('\nEste usuario no existe.\n')
                continue #si no encuentra el user nombre en la lista reiniciamos bucle de inicio
            
            password = input('Introduce tu contraseña: ') #verificamos password
            if password != usuario.password:
                print('\nContraseña erronea\n')
                continue #si la password es incorrecta reiniciamos bucle de inicio
            
            #segun el tipo de user iniciamos un menu con funcionalidades especificas
            elif type(usuario) == Administrador:
                usuario.mostrar_menu_adm()
            elif type(usuario) == Cajero:
                usuario.mostrar_menu_caj()
            elif type(usuario) == Usuario:
                usuario.mostrar_menu_usu()
        
class Banco: #objeto banco

    lista_bancos = [] #almacenamiento de objetos banco
    
    def __init__(self, nombre: str):
        #asignamos atributos de nombre y listas de almacenamiento de usuarios(clientes) y cajeros(trabajadores) del banco
        self.nombre = nombre
        #usuarios y cajeros son diferentes para cada banco
        self.lista_usuarios = []
        self.lista_cajeros = []
        Banco.lista_bancos.append(self) #al crear un objeto banco se almacena

    def __str__(self):

        return self.nombre #en caso de impresion imprimimos el nombre del objeto
    
    def mostrar_menu_ban(self): #menu de opciones de interaccion con el user

        while True:
            
            print('''\nMENU DEL BANCO {}\n
    1) listar cajeros disponibles.
    2) listar clientes de la entidad.
    3) Comprobar balance total de la entidad.
    4) Salir.\n'''.format(self.nombre))

            opt = input('que desea hacer? ') #en funcion de la eleccion del user utilizamos una funcionalidad espeifica
            if opt == '1':
                self.listar_cajeros()
            elif opt == '2':
                self.listar_usuarios()
            elif opt == '3':
                print('\n-- SALDO TOTAL ENTIDAD --\n')
                print(self.balance_total(), 'Dolares')
            elif opt == '4': #opcion de salida del menu (y banco)
                break

    def listar_cajeros(self):

        print('\n--LISTA DE CAJEROS--\n')
        for caj in self.lista_cajeros: #recorremos la lista de almacenamiento de objetos banco y enumeramos sus nombres en columna
            print(caj)

    def listar_usuarios(self): #funcionalidad como la anterior pero para enumeracion de usuarios del banco

        print('\n--LISTA DE USUARIOS--\n')
        for usu in self.lista_usuarios:
            print(usu)

    def balance_total(self): #mostrar el saldo total de los usuarios del objeto banco especifico

        balance = 0 #iniciamos en 0 

        for usu in self.lista_usuarios: #y sumamos saldos usuario por usuario
            balance += usu.dinero_cuenta

        return balance #devolvemos el total sumado
    
class Administrador(User): #objeto Administrador
    
    def __init__(self, nombre: str, password: str):

        #atributos de nombre y password para validacion
        self.nombre = nombre
        self.password = password
        User.lista_users.append(self) #adjuntamos a lista de almacenamiento de users

    def __str__(self):

        return self.nombre
        
    def mostrar_menu_adm(self): #menu de interaccion con user Administrador

        while True:
            print('''\nBienvenido {}.\n
        Que desea hacer?
        1) Generar un nuevo banco.
        2) Generar un nuevo cajero.
        3) Eliminar un cajero.
        4) Acceder al menu de banco.
        5) Salir.\n'''.format(self.nombre))
            opt = input('Selecciona una de las opciones: ')
            if opt == '1':
                self.crear_banco()
            elif opt == '2':
                self.crear_cajero()
            elif opt == '3':
                self.eliminar_cajero()
            elif opt == '4':
                self.mostrar_menu_bank()
            elif opt == '5': #opcion de salida del menu (y administrador)
                break
            
    def crear_banco(self): #crear objeto Banco

        while True:
            new_bank = input('Introduce el nombre de la nueva entidad: ')
            if len(new_bank) >= 1: #si introduciomos nombre vacio pide nuevamente insercion de nombre
                break #si inserta nombre salimos de bucle
        banco = Banco(new_bank)
        print('\nNueva entidad {} generada con exito!\n'.format(banco.nombre))

    def crear_cajero(self): #crear objeto Cajero

        #si insertamos nombre o password vacios pide nuevamente
        while True:
            new = input('Introduce el nombre del nuevo cajero: ')
            if len(new) >= 1:
                break
        while True:
            new_pass = input('Introduce una contraseña de acceso para el nuevo cajero: ')
            if len(new_pass) >= 1:
                break
        print('A que banco pertenece {}?\n'.format(new)) #mensaje para elegir banco del nuevo cajero {nombre de nuevo cajero}. mensaje personalizado
        for bank in Banco.lista_bancos:
            contador = Banco.lista_bancos.index(bank) + 1
            print(contador,') ', bank) #recorremos la lista de objetos Bancoe imprimimos en columna con un indice para su seleccion por el administrador

        while True:
            index = input('\nIntroduce la entidad bancaria de {}: '.format(new)) #pedimos al administrador que elija banco apoyandose en la lista impresa de antes
            try: #bloque try para limitar eleccion a numeros int y dentro de estos numeros dentro de las opciones dadas (1, 2, 3... acorde a longitud de lista bancos)
                index = int(index)
                if index not in range(1, len(Banco.lista_bancos) + 1):
                    print('\nEsa no es una opcion valida.\n')
                    continue #si insertamos opcion invalida (no numerico o fuera de rango) reiniciamos peticion de eleccion de banco
                break #si insertamos opcion valida rompemos bucle
            except ValueError:
                print('\nEsa no es una opcion valida.\n')
                
        banco = Banco.lista_bancos[index - 1] #banco como objeto elegido por el administrador (-1 porque indices comienzan en 0 y eleccion del administrador comienza en 1)
        
        new_user = Cajero(new, new_pass, banco) #creamos objeto Cajero. atributos nombre, password y objeto Banco ya definidos en esta funcion

        print('\nNuevo usuario creado. Nombre: {}, contraseña: {}, entidad: {}.\n'.format(new, new_pass, banco)) #mensaje de 'todo ok'

    def eliminar_cajero(self):

        print('\n') #estetico
        for bank in Banco.lista_bancos: #enumeramos bancos para eleccion de cajero en ese objeto Banco especifico
            contador = Banco.lista_bancos.index(bank) + 1
            print(contador,') ', bank)

        entidad = input('\nA que banco pertenece el cajero que deseas eliminar: ') #seleccionamos banco (aqui deberia poner un try/except para no admitir char no numericos o fuera de rango)
        banco = Banco.lista_bancos[int(entidad) - 1]

        print('\nEstos son los cajeros en la entidad seleccionada:\n')

        cont = 0
        for caj in banco.lista_cajeros: #enumeramos objetos Cajero en el banco seleccionado
            cont +=1
            print(cont, ') ', caj)
        while True: #seleccionamos objeto Cajero de los enumerados para eliminar. 
            index = input('\nCual de estos vas a eliminar? ')
            try: #bloque try para evitar selecciones erroneas
                index = int(index)
                if index not in range(1, len(banco.lista_cajeros) + 1):
                    print('\nEsa no es una opcion valida.\n')
                    continue
                break
            except ValueError:
                print('\nEsa no es una opcion valida.\n')
                
        caj = banco.lista_cajeros[index - 1] #acorde a seleccion del user orientamos a objeto Cajero seleccionado
        banco.lista_cajeros.remove(caj) #eliminamos objeto Cajero de lista de almacenamiento de cajeros en objeto Banco
        User.lista_users.remove(caj) #eliminamos objeto Cajero de lista de almacenamiento en objeto User
        del caj #double check
        
        print('\nCajero eliminado con exito.\n')

    def mostrar_menu_bank(self): #menu de interaccion de objeto Banco a traves de objeto Administrador

        if (len(Banco.lista_bancos) == 0): #si no existen objetos Banco creados salta mensaje de no objetos Banco
            print('\nDe momento no existen bancos operativos.')
            print(len(Banco.lista_bancos))
        else: #si SI existen objetos Banco los enumeramos

            print('\nEstos son los bancos existentes: ')

            for bank in Banco.lista_bancos: #enumeracion con indice para su seleccion
                contador = Banco.lista_bancos.index(bank) + 1
                print(contador,') ', bank)

            entidad = input('\nPara que banco te gustaria acceder a su menu?  ') #eleccion por parte del user
            
            while (entidad.isdigit() == False) or (int(entidad) not in range(1, (len(Banco.lista_bancos) + 1))): #verificacion de opcion valida, como anteriormente pero sin try. por variar
                entidad = input('\nHas introducido un valor erroneo. Introduce una opcion valida: ')
                                                   
            banco = Banco.lista_bancos[int(entidad) - 1] #acorde a seleccion del user orientamos a objeto Banco seleccionado
 
            banco.mostrar_menu_ban() #mostramos menu de interaccion con el objeto Banco seleccionado

class Cajero(User): #objeto Cajero

    def __init__(self, nombre: str, password: str, banco: object):

        #atributos de nombre, password, banco (objeto Banco donde trabaja el cajero en cuestion)
        self.nombre = nombre
        self.password = password
        self.banco = banco
        banco.lista_cajeros.append(self) #al crear objeto Cajero, se alamcena automaticamente en lista de cajeros de objeto Banco en que trabaja
        User.lista_users.append(self) #y lista de almacenamiento de users en general (objeto User)

    def __str__(self):

        return self.nombre

    def mostrar_menu_caj(self): #menu de interracion como anteriormente

        while True:
            print('''
    Bienvenido {}

    ¿En que puedo ayudar?

    1) Crear nuevo usuario.
    2) Realizar ingreso a cuenta.
    3) Retirada de efectivo.
    4) Cerrar sesion.'''.format(self.nombre))

            opt = input('\nSelecciona una de las opciones: ')
            if opt == '1':
                self.nuevo_usuario()
            elif opt == '2':
                self.ingresar_cuenta()
            elif opt == '3':
                self.retirada_efectivo()
            elif opt == '4': #opcion de salida del menu (y cajero)
                break

    def nuevo_usuario(self): #creamos nuevo objeto Usuario. Funcionalidad similar a creacion objeto Cajero

        while True:
            new = input('Introduce el nombre del nuevo usuario: ')
            if len(new) >= 1:
                break
        while True:
            new_pass = input('Introduce una contraseña de acceso para el nuevo usuario: ')
            if len(new_pass) >= 1:
                break
            
        banco = self.banco

        new_user = Usuario(new, new_pass, banco)

        print('Nuevo usuario creado. Nombre: {}, contraseña: {}, entidad: {}.\n'.format(new, new_pass, banco))

        ans = input('Quiere realizar un ingreso en la cuenta de este nuevo usuario? Si/No   ') #preguntamos al cajero si quiere ingresar dinero en cuenta de este nuevo objeto Usuario al crearse
        while ans not in ['Si', 'No']: #limitamos opciones a Si o No
            ans = input('Formato incorrecto, selecciona "Si" o "No".\nQuiere realizar un ingreso en la cuenta de este nuevo usuario? Si/No   ')

        if ans == 'Si': #si queremos realizar ingreso...
            q = input('Que cantidad desea ingresar? Si no deseas hacer un ingreso inserta 0. ')
            while True: #limitamos eleccion a valores numericos
                try:
                    q = float(q)
                    if q == 0: #si el user cambia de idea y no desea realizar ingreso finalmente puede salir insertando 0
                        print('\nIngreso cancelado.\n')
                        return None
                    break
                except ValueError:
                    print('\nEso no es una cantidad.\n')
                    q = input('Ingresa una cantidad. Si no quieres realizar un ingreso inserta 0. ')
                
                
            new_user.dinero_cuenta += q #añadimos ingreso a saldo del nuevo objeto Usuario
            
            print('Ingreso de {} Dolares realizado en la c/c de {}, gracias!\n'.format(q, new_user.nombre)) #'todo ok'

    def ingresar_cuenta(self):
            
        client = input('Indiqueme el nombre del usuario a realizar el ingreso: ') #solicitamos nombre del usuario a realizar ingreso
        for usu in self.banco.lista_usuarios: #iteramos lista de almacenamiento de usuarios en objeto Banco donde trabaja el cajero 
            existe = False #para romper el bucle cuando encontramos el usuario
            if usu.nombre == client:
                client = usu
                existe = True #rompemos
                break
        if existe == False: #si usuario no existe en el objeto Banco 
            print('\nEste usuario no existe en esta entidad.\n')
            return None
        
        passw = input('\nIndique la contraseña del usuario: ') #solicitamos clave de usuario para realizar ingreso
        if passw == client.password: #verificamos clave/password
            print('''\nUsuario validado. Vamos a realizar un ingreso en su cuenta de ahorro.
Recuerda que los ingresos deben ser superiores a 25 USD e inferiores a 10000 USD.''')
    
            while True: #bucle para insertar cantidad(q de ahora en adelante) de ingreso y limitar opciones a numericos con o sin decimales en rango de max i min establecidos por el banco 
                q = input('\nDe cuanto desea realizar el ingreso? Si no quieres realizar ingreso inserta 0. ')
                try:
                    q = float(q)
                    if (q < 25) or (q >= 10000): #max y min del banco(todos los bancos) de 10000 y 25 USD
                        if q == 0:
                            print('\nOperacion cancelada.')
                            return None
                        print('\nEl ingreso minimo es de 25 USD y el maximo de 10000 USD.')
                    else:
                        break        
                
                except ValueError:
                    print('\nEso no es una cantidad.\n')
            
            client.dinero_cuenta += q #añadimos ingreso a saldo del usuario
            print('Ingreso realizado, su saldo actual en cuenta es de {} Dolares. \n\nGracias y buen dia.'.format(client.dinero_cuenta)) #'todo ok'

        else:
            print('\nClave incorrecta.\n') #en caso de password introducida erronea. cierre de if iniciado al solicitar password

    def ingresar_cuenta_desde_cajero(self, cliente: object): 

    '''
objeto Usuario tiene funcionalidad para ingresar dinero a cuenta a traves de un objeto Cajero
mas adelante en objeto Usuario direccionaremos a esta funcionalidad para realizar ingreso'''
        
            while True: #limitamos opciones de ingreso a numericos y en rango de max i min del banco
                q = input('\nDe cuanto desea realizar el ingreso? Si no quieres realizar ingreso inserta 0. ')
                try:
                    q = float(q)
                    if (q < 25) or (q >= 10000):
                        if q == 0:
                            print('\nOperacion cancelada.')
                            return None
                        print('\nEl ingreso minimo es de 25 USD y el maximo de 10000 USD.')
                    else:
                        break        
                
                except ValueError:
                    print('\nEso no es una cantidad.\n')
            
            cliente.dinero_cuenta += q #añadimos a saldo de objeto Usuario
            print('Ingreso realizado, su saldo actual en cuenta es de {} Dolares. \n\nGracias y buen dia.'.format(cliente.dinero_cuenta)) #'todo ok'
            
    def retirada_efectivo(self):
            
        client = input('Indiqueme el nombre del usuario del banco: ') #pedimos objeto Usuario para realizar retirada
        
        for usu in self.banco.lista_usuarios: #buscamos el usuario dado en lista de almacenamiento de usuarios del objeto Banco donde trabaja el cajero con que operamos
            existe = False #rompedor
            if usu.nombre == client: #cuando encontramos el usuario rompemos bucle de busqueda
                existe = True
                client = usu
                break
        if existe == False: #si el usuario no existe finaliza la funcion
            print('\nNo existe usuario con ese nombre en esta entidad.\n')
            return None
        
        passw = input('\nIndique la contraseña del usuario: ') #solicitamos clave du usuario
        if passw == client.password: #verificamos
            print('\nUsuario validado. Vamos a realizar una retirada de efectivo de su cuenta de ahorro.')
            while True: #bucle en caso de introducir importe invalido. limitamos opcion de retirada a numericos y superiores a saldo en cuenta de usuario
                q = input('Cuanto efectivo desea retirar? Si desea cancelar la operacion introduzca 0. ')
                try:
                    q = float(q) #limitamos a numericos
                    if q == 0:
                        print('\nOperacion cancelada.') #opcion de salida de retirada_efectivo si hay cambio de idea
                        return None
                    elif q > client.dinero_cuenta: #limitamos a saldo en cuenta de usuario
                        print('{} no dispone de esa cantidad en su cuenta de ahorro.\nCantidad disponible -> {} USD.'.format(client.nombre, client.dinero_cuenta))
                    else:
                        break        
                
                except ValueError:
                    print('\nEso no es una cantidad.\n')
                
            client.dinero_cuenta -= q #retiramos importe de cuenta de usuario
            client.dinero_fisico += q #abonamos a importe de efectivo de usuario

            print('Retirada realizada, su saldo actual en cuenta es de {} USD. Su Saldo efectivo es de {} USD. \n\nGracias y buen dia.'.format(client.dinero_cuenta, client.dinero_fisico))
        else: #si la password solicitada antes es erronea
            print('Clave incorrecta')
    
class Usuario(User): #objeto Usuario(cliente del banco)

    def __init__(self, nombre: str, password, banco: object):

        #atributos de nombre, password, banco donde es cliente(objeto Banco), dinero en cuenta y en efectivo
        self.nombre = nombre
        self.password = password
        self.banco = banco
        self.dinero_fisico = 0
        self.dinero_cuenta = 0
        banco.lista_usuarios.append(self) #añadimos a lista de usuarios de objeto banco
        User.lista_users.append(self) #añadimos a lista de users de objeto User

    def __str__(self):

        return self.nombre
    
    def mostrar_menu_usu(self): #menu de interacion con usuario

        while True:
            
            print('''
    Bienvenido {}

    ¿En que puedo ayudar?

    1) Mostar saldo de cuenta de ahorro.
    2) Mostrar saldo efectivo en cash.
    3) Ingresar en cuenta de ahora a traves de cajero
    4) Cerrar sesion.'''.format(self.nombre))

            option = input('\nSelecciona una de las opciones: ')
            if option == '1':
                print(self.saldo_cuenta(), 'USD.')
            elif option == '2':
                print(self.saldo_fisico(), 'USD.')
            elif option == '3':
                self.ingreso_cajero()
            elif option == '4': #opcion de salida del menu (y usuario)
                break
        

    def saldo_cuenta(self):

        print('\nEl saldo en tu cuenta de ahorro es de:\n')
        return self.dinero_cuenta #devuelve atributo de saldo en cuenta

    def saldo_fisico(self):

        print('\nTu saldo disponible en efectivo es de:\n')
        return self.dinero_fisico #devuelve atributo de saldo en efectivo

    def ingreso_cajero(self): #ingresar a traves de objeto Cajero
        
        print('Estos son nuestros cajeros disponibles:\n ')
        for caj in self.banco.lista_cajeros: #desplegablle de objetos Cajero en banco de cliente para su eleccion
            print(caj.nombre)

        cashier = input('\nA traves de que cajero quieres realizar el ingreso? ') #indicamos cajero (por nombre)
        existe = False
        for caj in self.banco.lista_cajeros: #iteramos los objetos Cajero en el banco del cliente y seleecionamos el indicado por el usuario
            if cashier == caj.nombre:
                cashier = caj
                existe = True
                print('\nCajero {} seleccionado.\n'.format(cashier.nombre)) #'todo ok'
                break
        if existe == False:
            print('\nNo existe ningun cajero con ese nombre en esta entidad.\n')
            return None
        cashier.ingresar_cuenta_desde_cajero(self) # ->
        #llamamos a la funcionalidad del cajero especifica para este proceso
        #como el ingreso debe hacerse con la asistencia/ a traves de cajero, esta funcionalidad esta definida en objeto Cajero

#creamos instancias de User(para almacenamiento e iniciacion de programa), Banco, Administrador, Cajeros y Usuarios
inicio = User()
fran = Administrador('Francisco', '2937')
banco = Banco('Banca Leopoldo')
usuario1 = Usuario('soyla_luna', '1524', banco)
cajero1 = Cajero('pedrito', '0025', banco)
cajero2 = Cajero('juan_p', '7584', banco)
inicio.validacion() #iniciamos programa. llamamos a la funcion de validacion de user para ello

