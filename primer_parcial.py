
import json
import re
import csv

def leer_json(ruta_archivo):
    lista = []
    with open(ruta_archivo,"r") as archivo: 
        dict =json.load(archivo)
        lista = dict["jugadores"]
    return lista

lista_jugadores_dream_team = leer_json(r"C:\Users\RODRIGO\Desktop\Parcial Dream Team\tu_usuario-pp_lab1_Rodrigo_Ruiz\dt.json")

def generar_archivo_csv(diccionario, nombre_archivo):
    with open(nombre_archivo, 'w', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        
        # Obtener las claves del diccionario como encabezados
        encabezados = diccionario.keys()
        encabezados_formateados = [encabezado.replace("_", " ") for encabezado in encabezados]
        
        # Escribir los encabezados
        writer.writerow(encabezados_formateados)
        
        # Obtener los valores del diccionario
        valores = diccionario.values()
        valores_formateados = [str(valor).ljust(len(encabezado)) for valor, encabezado in zip(valores, encabezados)]
        
        # Escribir los valores
        writer.writerow(valores_formateados)

def quick_sort_lista_diccionarios(lista_diccionarios_original:list[dict],flag_orden:bool,clave:str)->list:
    lista_de = []
    lista_iz = []
    lista_dict_aux = lista_diccionarios_original 
    if(len(lista_dict_aux)<=1): 
        return lista_dict_aux
    else:
        pivot = lista_dict_aux[0]
        for diccionario in lista_dict_aux[1:]:
            if flag_orden:
                if(diccionario[clave] > pivot[clave]):
                    lista_de.append(diccionario)
                else:
                    lista_iz.append(diccionario)
            else:
                if(diccionario[clave] < pivot[clave]):
                    lista_de.append(diccionario)   
                else:
                    lista_iz.append(diccionario)
                                
    lista_iz = quick_sort_lista_diccionarios(lista_iz,flag_orden,clave)
    lista_iz.append(pivot) 
    lista_de = quick_sort_lista_diccionarios(lista_de,flag_orden,clave)
    lista_iz.extend(lista_de) 
    return lista_iz

def imprimir_menu_opciones():
    '''
    Imprime un menu de opciones por consola
    '''
    print("Menu:")
    print(" 1) Mostrar integrantes del Dream Team")
    print(" 2) Buscar jugador por nombre y mostrar sus estadisticas")
    print(" 3) Generar archivo con estadisticas")
    print(" 4) Buscar logros por nombre de jugador")
    print(" 5) Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente.")
    print(" 6) Buscar por nombre y comprobar si es Hall of Fame")
    print(" 7) Calcular y mostrar el jugador con la mayor cantidad de rebotes totales")
    print(" 8) Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo")
    print(" 9) Calcular y mostrar el jugador con la mayor cantidad de asistencias totales")
    print("10) Ingresar cantidad de puntos por partido y mostrar jugadores que los hayan superado ")
    print("11) Mostrar jugadores con mayor promedio de rebotes por partido que el nro ingresado")
    print("12) Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos")
    print("13) Calcular y mostrar el jugador con la mayor cantidad de robos totales.")
    print("14) Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.")
    print("15) Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.")
    print("16) Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.")
    print("17) Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos")
    print("18) Ingresar porcentaje de acierto en triples por partido y mostrar jugadores que los hayan superado")
    print("19) Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas")
    print("20) Permitir al usuario ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.")
    print("21) Salir")

def menu_principal():
    '''
    llama a la funcion para imprimir un menu de opciones por consola
    Le solicita al usuario el ingreso de un numero para seleccionar en el menu
    retorna el numero(str) validado
    '''
    imprimir_menu_opciones()
    opcion = input("Ingrese una opción: ")
    while True:
        patron = r'^(1[0-9]|20|[1-9])$'
        if bool(re.match(patron,opcion)):
            resultado = opcion
            break
        else:
            opcion = input("Ingrese una opción: ")
    return resultado

#1     
def mostrar_datos_jugador(lista_jugadores:list[dict],clave_uno,clave_dos): 
    '''
    Recibe una lista de jugadores y dos claves en str
    imprime por consola el numero de linea junto a a los valores de las dos claves pasardas
    por parámetro    
    '''
    contador = 1
    for jugador in lista_jugadores:
        print("{0})nombre: {1} posicion: {2}".format(contador,jugador[clave_uno],jugador[clave_dos]))
        contador += 1
    
    
def imprimir_roster_con_indice(lista):
    '''
    recibe una lista de jugadores
    Imprime por pantalla el nombre de cada jugador
    '''
    for i in range(len(lista)):
        print('{0}) {1}'.format(i+1,lista[i]["nombre"]))

def pedir_ingreso_de_dato_y_validar():  
    '''
    Le solicita al usuario que ingrese y un numero entre el 1 y el 12
    lo valida, y una vez que lo obtiene lo castea a int y lo retorna
    '''
    while True:
        dato_ingresado = input("Seleccione el nro del jugador en la lista para ver sus estadisticas: ")
        if re.match(r"^(1[0-2]|[1-9])$",dato_ingresado):
            dato_ingresado = int(dato_ingresado)
            break
    return dato_ingresado

def imprimir_lista(lista):
    '''
    Recibe una lista por parametro
    e imprime todos sus elementos por consola
    '''
    for item in lista:
        print(item)

def imprimir_diccionario(diccionario):
    '''
    Recibe un diccionario por parametro e imprime
    todas los pares clave-valor por pantalla
    '''
    for clave,valor in diccionario.items():
        print("{0}: {1}".format(clave,valor).replace("_"," "))
        


# def validacion_por_indice(dato:str):
#     return re.match(r"^(1[0-2]|[1-9])$",dato)

def filtar_jugador_por_indice_estadisticas(lista:list[dict])->str: #esto esta mal
    dict_retorno = {}
    indice_buscado = pedir_ingreso_de_dato_y_validar()
    dict_retorno = lista[indice_buscado-1].copy()
    return dict_retorno
       

def filtar_jugador_por_indice_logros(lista:list[dict])->str:
    imprimir_roster_con_indice(lista)   
    str_retorno = ""
    indice_buscado = pedir_ingreso_de_dato_y_validar()
    nombre = lista[indice_buscado-1]["nombre"] + "\n"
    for logro in lista[indice_buscado-1]["logros"]:
        str_retorno += logro + "\n"
    return nombre+str_retorno

'''
Permitir al usuario buscar un jugador por su nombre y mostrar sus logros, como campeonatos de la NBA, participaciones en el All-Star y pertenencia al Salón de la Fama del Baloncesto, etc.
'''
def listar_nombres_del_dream_team(list_jugadores:list[dict])->list:
    '''
    Retorna una lista con todos los nombres de los jugadores que forman parte del dream team
    '''
    lista_nombres = []
    for jugador in list_jugadores:
        if "nombre" in jugador: #probar quedarme con el indice
            lista_nombres.append(jugador["nombre"])
    return lista_nombres


def recorrer_lista_dicc_y_extraer_indice(lista_de_diccionarios,clave,valor)->int:
    '''
    Recibe una lista de diccionarios, una clave y un valor
    si la lista de diccionarios contiene el par clave valor pasado por parametro
    retorna el indice donde lo encontró
    si no encuentra ese par clave valor o la lista es vacia, retorna -1
    '''
    if not lista_de_diccionarios:
        return -1
    else:
        for i in range(len(lista_de_diccionarios)):
            if lista_de_diccionarios[i][clave] == valor:
                return i
    return -1



def buscar_jugador_por_nombre(lista_jugadores)->dict:
    lista_nombres_validos = listar_nombres_del_dream_team(lista_jugadores_dream_team)
    nombre_ingresado = ""
    while True:
        nombre_ingresado = input("ingrese el nombre completo del jugador: ").title()
        if nombre_ingresado in lista_nombres_validos:
            break
        print("Jugador no encontrado, vuelva a intentarlo: ")
    indice_del_jugador_buscado = recorrer_lista_dicc_y_extraer_indice(lista_jugadores,"nombre",nombre_ingresado)
    return lista_jugadores[indice_del_jugador_buscado]
    


'''
5)	Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente. 
'''
def excluir_al_peor_segun(lista_jugadores,apartado:str)->list[dict]:
    el_peor_en_algun_apartado = buscar_max_min_segun_estadistica(lista_jugadores,apartado,False)
    indice_del_peor = recorrer_lista_dicc_y_extraer_indice(lista_jugadores_dream_team,"nombre",el_peor_en_algun_apartado["nombre"])
    lista_sin_el_peor_segun = []
    lista_sin_el_peor_segun = lista_jugadores.copy()
    del lista_sin_el_peor_segun[indice_del_peor]
    return lista_sin_el_peor_segun
    

def generar_string_desde_lista_diccionarios(lista_de_diccionarios,clave_uno,clave_dos)->str: #tratar de incluirlo en las funciones precios
    string_retorno = ""
    for elemento in lista_de_diccionarios:
        string_retorno += "{0}: {1}\n".format(elemento[clave_uno],elemento[clave_dos])
    return string_retorno
        
def calcular_y_mostrar_promedio_de_equipo(lista_jugadores:list[dict],apartado:str)->float:
    cantidad_jugadores = 0
    acumulador = 0
    if not lista_jugadores:                   
        return lista_jugadores
    else:
        for jugador in lista_jugadores:
            acumulador += jugador["estadisticas"][apartado]
            cantidad_jugadores += 1
    return acumulador/cantidad_jugadores


def mostrar_promedio_puntos_por_partido_por_jugador(lista_jugadores,clave_para_ordenar,menor_a_mayor=True):
    '''
    recibe una lista de jugadroes, una clave de tipo string que se usará como criterio para ordenar
    y un booleano, que si esta en True ordena de forma ascendente, caso contrario, descendente
    retorna un string indicando el nombre de cada jugador junto a la cantidad de puntos por partido
    Ordenados alfabeticamente
    '''
    lista_promedios = []
    for jugador in lista_jugadores:
        dict_aux = {}
        dict_aux["nombre"] = jugador["nombre"]
        dict_aux["promedio_puntos_por_partido"] =jugador["estadisticas"]["promedio_puntos_por_partido"]
        lista_promedios.append(dict_aux)
        lista_promedios_ordenada = quick_sort_lista_diccionarios(lista_promedios,menor_a_mayor,clave_para_ordenar)
    return generar_string_desde_lista_diccionarios(lista_promedios_ordenada,"nombre","promedio_puntos_por_partido")


'''
6)	Permitir al usuario ingresar el nombre de un jugador y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto.
'''
def is_hall_of_fame(jugador:dict)->bool:
    '''
    recibe un jugador y retorna True si ser hall of fame está entre sos logros
    Retorno False en caso contrario
    '''
    mensaje = "Miembro del Salon de la Fama del Baloncesto"
    return mensaje in jugador["logros"]
    

def buscar_hall_oh_fame_por_nombre(lista_jugadores)->dict:
    mensaje = ""
    jugador_consultado = buscar_jugador_por_nombre(lista_jugadores_dream_team)
    if is_hall_of_fame(jugador_consultado):
        mensaje = "Es miembro del NBA Hall of Fame"
    else:
        mensaje = "No es miembro del NBA Hall of Fame"
    print(mensaje)
            
 
 
def buscar_max_min_segun_estadistica(lista_jugadores:list[dict],apartado:str,estoy_buscando_el_max=True)->dict:#solo busca dentro del diccionario estadisticas
    '''
    Recibe una l
    '''
    jugador_buscado = lista_jugadores[0]
    for jugador in lista_jugadores[1:]:
            if estoy_buscando_el_max:
                if jugador["estadisticas"][apartado] > jugador_buscado["estadisticas"][apartado]:
                    jugador_buscado = jugador.copy()
            else:
                if jugador["estadisticas"][apartado] < jugador_buscado["estadisticas"][apartado]:
                    jugador_buscado = jugador.copy()
    return jugador_buscado

def buscar_max_min_segun_longitud_de_lista(lista_jugadores:list[dict],apartado:str,estoy_buscando_el_max=True)->dict:#lo mismo que la de arriba pero fuera de estadisticas
    jugador_buscado = lista_jugadores[0]
    for jugador in lista_jugadores[1:]:
            if estoy_buscando_el_max:
                if len(jugador[apartado]) > len(jugador_buscado[apartado]):
                    jugador_buscado = jugador.copy()
            else:
                if len(jugador[apartado]) < len(jugador_buscado[apartado]):
                    jugador_buscado = jugador.copy()
    return jugador_buscado

def imprimir_listas_de_diccionarios(lista_de_diccionarios,): #desarrollar
    pass

def es_un_numero_valido(numero:str)->bool:
    '''
    recibe un nuemero en formato string
    y verifica que sea un numero positivo
    en caso afirmativo retorna True sino False
    '''
    return re.match(r"^(?:0|[1-9][0-9]*)(?:\.\d+)?$",numero)


def buscar_jugadores_con_apartado_mayor_a(lista_jugadores,apartado)->list[dict]:
    '''
    Recibe una lista de jugadores y una apartado estadistico
    le pide al usuario que ingrese un numero y verifica si hay algun jugador
    que supere ese numero en el apartado estadistico pasado como parametro
    En caso afirmatativo retorna la lista de jugadores que lo lograron
    caso contrario retorna un mensaje informativo
    '''
    lista_retorno = []
    while True:
        numero_ingresado = input("ingrese el numero de {0}: ".format(apartado).replace("_"," "))
        if es_un_numero_valido(numero_ingresado):
            numero_ingresado = float(numero_ingresado)
            break
    for jugador in lista_jugadores:
        if numero_ingresado < jugador["estadisticas"][apartado]:
            lista_retorno.append(jugador)
    if not lista_retorno:
        print("Ningun jugador pertences a este selecto grupo") 
    return lista_retorno
    
 
                     
def dream_team_app(lista_heroes):
    while True:
        respuesta = menu_principal()
        match(respuesta):
            case "1":
                mostrar_datos_jugador(lista_jugadores_dream_team,"nombre","posicion")
            case "2":  
                imprimir_roster_con_indice(lista_jugadores_dream_team)
                imprimir_diccionario(filtar_jugador_por_indice_estadisticas(lista_jugadores_dream_team)["estadisticas"])
            case "3":
                nombre_archivo = input("Ingrese el nombre con el que desea guardar el archivo")
                generar_archivo_csv(buscar_jugador_por_nombre(lista_jugadores_dream_team)["estadisticas"],nombre_archivo) #pulir  
            case "4":
                imprimir_lista(buscar_jugador_por_nombre(lista_jugadores_dream_team)["logros"])         
            case "5":
                print(mostrar_promedio_puntos_por_partido_por_jugador(lista_jugadores_dream_team,"nombre",True))
                print("{0}: {1}".format("Promedio de equipo",calcular_y_mostrar_promedio_de_equipo(lista_jugadores_dream_team,"promedio_puntos_por_partido")))           
            case "6":
                buscar_hall_oh_fame_por_nombre(lista_jugadores_dream_team)          
            case "7":
                jugador_buscado = buscar_max_min_segun_estadistica(lista_jugadores_dream_team,"rebotes_totales",True)      
                print(jugador_buscado["nombre"])
                print(jugador_buscado["estadisticas"]["rebotes_totales"])
            case "8":
                jugador_buscado = buscar_max_min_segun_estadistica(lista_jugadores_dream_team,"porcentaje_tiros_de_campo",True)      
                print(jugador_buscado["nombre"])
                print(jugador_buscado["estadisticas"]["porcentaje_tiros_de_campo"])         
            case "9":
                jugador_buscado = buscar_max_min_segun_estadistica(lista_jugadores_dream_team,"asistencias_totales",True)      
                print(jugador_buscado["nombre"])
                print(jugador_buscado["estadisticas"]["asistencias_totales"])  
            case "10":
                jugadores_buscados = buscar_jugadores_con_apartado_mayor_a(lista_jugadores_dream_team,"promedio_puntos_por_partido")
                for jugador in jugadores_buscados: #meter dentro de otra funcion
                    print("{0}: {1}".format(jugador["nombre"],jugador["estadisticas"]["promedio_puntos_por_partido"]))
            case "11":
                jugadores_buscados = buscar_jugadores_con_apartado_mayor_a(lista_jugadores_dream_team,"promedio_rebotes_por_partido") #meter dentro de otra funcion para validar si es vacia
                for jugador in jugadores_buscados: #meter dentro de otra funcion
                    print("{0}: {1}".format(jugador["nombre"],jugador["estadisticas"]["promedio_rebotes_por_partido"]))
            case "12":
                jugadores_buscados = buscar_jugadores_con_apartado_mayor_a(lista_jugadores_dream_team,"promedio_asistencias_por_partido") #meter dentro de otra funcion para validar si es vacia
                for jugador in jugadores_buscados: #meter dentro de otra funcion
                    print("{0}: {1}".format(jugador["nombre"],jugador["estadisticas"]["promedio_asistencias_por_partido"]))
            case "13":
                jugador_buscado = buscar_max_min_segun_estadistica(lista_jugadores_dream_team,"robos_totales",True)      
                print(jugador_buscado["nombre"])
                print(jugador_buscado["estadisticas"]["robos_totales"]) 
            case "14":
                jugador_buscado = buscar_max_min_segun_estadistica(lista_jugadores_dream_team,"bloqueos_totales",True)      
                print(jugador_buscado["nombre"])
                print(jugador_buscado["estadisticas"]["bloqueos_totales"]) 
            case "15":
                jugadores_buscados = buscar_jugadores_con_apartado_mayor_a(lista_jugadores_dream_team,"porcentaje_tiros_libres") #meter dentro de otra funcion para validar si es vacia
                for jugador in jugadores_buscados: #meter dentro de otra funcion
                    print("{0}: {1}".format(jugador["nombre"],jugador["estadisticas"]["porcentaje_tiros_libres"]))
            case "16":
                jugadores_buscados = excluir_al_peor_segun(lista_jugadores_dream_team,"promedio_puntos_por_partido")
                for jugador in jugadores_buscados: #meter dentro de otra funcion
                    print("{0}: {1}".format(jugador["nombre"],jugador["estadisticas"]["promedio_puntos_por_partido"]))
            case "17":
                jugador_buscado = buscar_max_min_segun_longitud_de_lista(lista_jugadores_dream_team,"logros",True)
                print("{0}".format(jugador_buscado["nombre"]))
                imprimir_lista(jugador_buscado["logros"])
            case "18":
                jugadores_buscados = buscar_jugadores_con_apartado_mayor_a(lista_jugadores_dream_team,"porcentaje_tiros_triples") #meter dentro de otra funcion para validar si es vacia
                for jugador in jugadores_buscados: #meter dentro de otra funcion
                    print("{0}: {1}".format(jugador["nombre"],jugador["estadisticas"]["porcentaje_tiros_triples"]))
            case "19":
                jugador_buscado = buscar_max_min_segun_estadistica(lista_jugadores_dream_team,"temporadas",True)      
                print(jugador_buscado["nombre"])
                print(jugador_buscado["estadisticas"]["temporadas"]) 
            case "20":
                jugadores_buscados = buscar_jugadores_con_apartado_mayor_a(lista_jugadores_dream_team,"porcentaje_tiros_de_campo") #meter dentro de otra funcion para validar si es vacia120
                jugadores_buscados = quick_sort_lista_diccionarios(jugadores_buscados,True,"posicion")
                for jugador in jugadores_buscados: #meter dentro de otra funcion
                    print("{0}: {1}".format(jugador["nombre"],jugador["estadisticas"]["porcentaje_tiros_de_campo"]))
            case "21":
                break
                
        input("\nPulse enter para continuar\n")
            
                       

dream_team_app(lista_jugadores_dream_team)