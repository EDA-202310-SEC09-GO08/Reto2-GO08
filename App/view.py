"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def crear_diccionario_de_TAD (TAD ,categoria,tamanio):
    
    i =0
    dic = {}
    
    while i < tamanio:
        variable = lt.getElement(TAD,i)
        momento = variable[categoria]
        if variable[categoria] not in dic.keys():
            dic[momento] = lt.newList(datastructure="ARRAY_LIST")
            lt.addLast(dic[momento], variable )
        elif variable[categoria] in dic.keys():
            lt.addLast(dic[momento], variable  )
        
        i +=1
    return dic
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
""" Funciones para filtrar datos a mostrar"""


######Filtra diccionarios por columnas a mostrar
def filtrar_dic_con_por_llaves(dic, lista_de_columnas_aMostrar):
    dic_filt ={}
    for llave in lista_de_columnas_aMostrar:
        dic_filt[llave]=dic[llave]

    return dic_filt

def filtrar_lista_dics_por_columnas(lista_dics,lista_columnas):
    lista_filt = []
    
    tamanio_lista = len(lista_dics)
    i = 0
    
    while i<tamanio_lista:
        dic_filt_dado = filtrar_dic_con_por_llaves(lista_dics[i],lista_columnas)
        lista_filt.append(dic_filt_dado)
        i+=1
    return lista_filt


def filtrar_lista_dics_por(lista_dics,lista_columnas):
    lista_filt = []

    tamanio_lista = lt.size(lista_dics)
    i = 0

    while i<tamanio_lista:
        a = lt.getElement(lista_dics,i)
        dic_filt_dado = filtrar_dic_con_por_llaves(a,lista_columnas)
        lista_filt.append(dic_filt_dado)
        i+=1
    return lista_filt
def new_controller(tipo,factor):
    """
        Se crea una instancia del controlador
    """
    control = controller.new_controller(tipo,factor)

    return control

def devolver_value(map, key):
    llave_valor = mp.get(map, key)
    valor = me.getValue(llave_valor)
    
    return valor 
def print_3_primeros_3_ultimos(control):
    
    mapa = control['model']['Años']

    ### Crear lista para cada año a imprimir
    tamanio_mapa =lt.size(mp.keySet(mapa))
    anio = 2012

    while anio <2012+tamanio_mapa:
        array_anio = devolver_value(mapa,anio)['Lista']
        tamanio_array = lt.size(array_anio)
        lista_imprimir_anio = []

        if tamanio_array>=6:
            lista_imprimir_anio.append(lt.getElement(array_anio,1))
            lista_imprimir_anio.append(lt.getElement(array_anio,2))
            lista_imprimir_anio.append(lt.getElement(array_anio,3))
            lista_imprimir_anio.append(lt.getElement(array_anio,tamanio_array-2))
            lista_imprimir_anio.append(lt.getElement(array_anio,tamanio_array-1))
            lista_imprimir_anio.append(lt.getElement(array_anio,tamanio_array))

        else:
            i =1
            while i<=tamanio_array:
                lista_imprimir_anio.append(lt.getElement(array_anio,i))
                i+=1

        lista_filtrada = filtrar_lista_dics_por_columnas(lista_imprimir_anio,['Año', "Código actividad económica","Nombre actividad económica","Código sector económico","Nombre sector económico",
    "Código subsector económico","Nombre subsector económico","Total ingresos netos", "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor"])
        
        tabulate_respuesta = tabulate(lista_filtrada, headers='keys', maxcolwidths =[10]*11, maxheadercolwidths=[10]*11)
        print('Las primeras y últimas actividades económicas para ',anio,' son: ')
        print(tabulate_respuesta)
        anio += 1




def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Obtener la actividad econónomica con mayor saldo a favor de un sector economico y año especifico ")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Encontrar el subsector económico con los mayores descuentos tributarios en un año especifico ")
    print("7- Ejecutar Requerimiento 6")
    print("8- Listar el TOP (N) de las actividades económicas con el menor total de costos y gastos para un subsector economico en unos años especificos ")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")

def menu_nombre_archivo():
    print("Que porcentage de datos ")
    print("1-1%")
    print("2-5%")
    print("3-10%")
    print("4-20%")
    print("5-30%")
    print("6-50%")
    print("7-100%")

def menu_archivo():
    menu_nombre_archivo()
    porcentaje = input('Seleccione una opción para continuar\n')
    try:
        if int(porcentaje) == 2:
            
            size ="Salida_agregados_renta_juridicos_AG-5pct.csv"
            return size
        elif int(porcentaje) == 3:
            size = "Salida_agregados_renta_juridicos_AG-10pct.csv"
            return size
        elif int(porcentaje) == 4:
            size = "Salida_agregados_renta_juridicos_AG-20pct.csv"
            return size
        elif int(porcentaje) == 5:
            size = "Salida_agregados_renta_juridicos_AG-30pct.csv"
            return size
        elif int(porcentaje) == 6:
            size = "Salida_agregados_renta_juridicos_AG-50pct.csv"
            return size
        elif int(porcentaje) == 1:
            size = "Salida_agregados_renta_juridicos_AG-small.csv"
            return size
        elif int(porcentaje) == 7:
            size = "Salida_agregados_renta_juridicos_AG-large.csv"
            return size
    except ValueError:
            print(" una opción válida.\n")
            traceback.print_exc()

def menu_maptype_opciones():
    print("Qué tipo de mapa desea cargar? ")
    print("1-Linear Probing")
    print("2-Separate Chaining")


def menu_maptype():
    menu_maptype_opciones()
    tipo = input('Seleccione una opción para continuar\n')
    try:
        if int(tipo) == 1:
            
            size ="PROBING"
            return size
        elif int(tipo) == 2:
            size = "CHAINING"
            return size
        
    except ValueError:
            print(" una opción válida.\n")
            traceback.print_exc()

def menu_opciones_factor_PROBING():
    print("Que factor de carga PROBING quiere? ")
    print("1-0,1")
    print("2-0,5")
    print("3-0,7")
    print("4-0,9")

def menu_factor_PROBING():
    menu_opciones_factor_PROBING()
    porcentaje = input('Seleccione una opción para continuar\n')
    try:
        if int(porcentaje) == 1:
            
            size =0.1
            return size
        elif int(porcentaje) == 2:
            size = 0.5
            return size
        elif int(porcentaje) == 3:
            size = 0.7
            return size
        elif int(porcentaje) == 4:
            size = 0.9
            return size
    except ValueError:
            print(" una opción válida.\n")
            traceback.print_exc()


def menu_opciones_factor_CHAINING():
    print("Que factor de carga CHAINING quiere? ")
    print("1-2.0")
    print("2-4.0")
    print("3-6.0")
    print("4-8.0")

def menu_factor_CHAINING():
    menu_opciones_factor_CHAINING()
    porcentaje = input('Seleccione una opción para continuar\n')
    try:
        if int(porcentaje) == 1:
            
            size =2
            return size
        elif int(porcentaje) == 2:
            size = 4
            return size
        elif int(porcentaje) == 3:
            size = 6
            return size
        elif int(porcentaje) == 4:
            size = 8
            return size
    except ValueError:
            print(" una opción válida.\n")
            traceback.print_exc()   


def menu_decision_espacio():
    print("Desea saber cuanto espacio se ocupo? ")
    print("1- Si desea saberlo")
    print("2- Si no desea saberlo")

def menu_espacio():
    menu_decision_espacio()
    decision_v = input('Seleccione una opción para continuar\n')
    try:
        if int(decision_v) == 1:
            decision = True
            return decision
        elif int(decision_v) == 2:
            decision = False
            return decision
    except ValueError:
            print(" una opción válida.\n")
            traceback.print_exc()
            


def load_data(control,filename,memory):
    """
    Carga los datos
    """

    control_1 =controller.load_data(control,filename,memory)
    return control_1


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    anio = input("En que año desea buscar la informacion ")
    sector = input("En que sector desea buscarlo ")

    respuesta = controller.req_2(control, anio, sector)

    print(tabulate([respuesta], headers="keys", tablefmt= "grid", maxcolwidths=15, maxheadercolwidths=15  ))


def print_req_3(control,anio,memory):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    req_3 = controller.req_3(control,anio,memory)

    respuesta = [req_3[0]]

    

    

    

    respuesta_filtrada =filtrar_lista_dics_por_columnas( respuesta,['Código sector económico',
                                              'Nombre sector económico','Código subsector económico',
                                          'Nombre subsector económico', 'Total retenciones','Total ingresos netos',
                                          'Total costos y gastos','Total saldo a pagar','Total saldo a favor'])

    #res_esp_2019 = respuesta[1]['Primeras y últimas 3 actividades en contribuir']

    tabulate_respuesta = tabulate(respuesta_filtrada, headers='keys', maxcolwidths =[10]*6, maxheadercolwidths=[10]*6)
    print(tabulate_respuesta)
    i=0
    tamanio_lista = len(respuesta)
    while i<tamanio_lista:

        anio_subsect = respuesta[i]['Año']
        lista_por_subsec = filtrar_lista_dics_por_columnas(respuesta[i]['Primeras y últimas 3 actividades en contribuir'],['Código actividad económica',
                                                            'Nombre actividad económica','Total retenciones','Total ingresos netos',
                                          'Total costos y gastos','Total saldo a pagar','Total saldo a favor'])
        
        lista_subsect_tabulete = tabulate(lista_por_subsec,headers='keys', maxcolwidths =[10]*7, maxheadercolwidths=[10]*7)
        print('Actividades que más y menos contribuyeron al subsector para ',anio_subsect)
        print(lista_subsect_tabulete)

        i+=1


    #print(type(res_esp_2016))
    #print(res_esp_2016)
    #df_2019 = pd.DataFrame(res_esp_2019)
    #df = pd.DataFrame(respuesta)
    #df_fil = df[['Año','Nombre subsector económico','Total retenciones']]
    #df_filt_2019 = df_2019[['Código actividad económica','Nombre actividad económica']]
    #print(df_fil)
    #print(df_filt_2019)
    print('Tiempo:  ',req_3[1])
    print('Memoria:  ',req_3[2])


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    anios = input("En que año desea encontrar el mayor descuento tributario ")
    respuesta = controller.req_5(control, anios)
    print( "The subsector with the highest total witholdings (Descuentos Tributarios) in " + anios)
    print(tabulate([respuesta[0]], headers="keys", tablefmt= "grid", maxcolwidths=15, maxheadercolwidths=15  ))
    tamanio = len(respuesta[1])

    if tamanio >=6:
        i = 0 
        menores =[]
        while i < 3:
            menores.append(respuesta[1][i])
            i +=1
        print("The three economic activities that contributed the least in " + anios + " in the subsector " + str(respuesta[2]) )
        print(tabulate(menores, headers="keys", tablefmt= "grid", maxcolwidths=15, maxheadercolwidths=15  ))
        largo = tamanio - i 
        mayores =[]
        while largo < tamanio:
            mayores.append(respuesta[1][largo])
            largo +=1
        print("The three economic activities that contributed the most in " + anios + " in the subsector " + str(respuesta[2]) )
        print(tabulate(mayores, headers="keys", tablefmt= "grid", maxcolwidths=15, maxheadercolwidths=15  ))
    else:
        print("There are only " + str(tamanio)+" economic activities in " + anios +  " in the subsector " + str(respuesta[2]) )
        print(tabulate(respuesta[1], headers="keys", tablefmt= "grid", maxcolwidths=15, maxheadercolwidths=15  ))
    


def print_req_6(control,anio,memory):
    req_6 = controller.req_6(control,anio,memory)
    respuesta = req_6[0]
    req_6_lista = [req_6[0]]
    req_6_tiempo = req_6[1]
    req_6_memory = req_6[2]

    respuesta_filtrada =filtrar_lista_dics_por_columnas( req_6_lista,['Código sector económico',
                                              'Nombre sector económico','Total ingresos netos',
                                          'Total costos y gastos','Total saldo a pagar','Total saldo a favor'])


    tabulate_respuesta = tabulate(respuesta_filtrada, headers='keys', maxcolwidths =[15]*6, maxheadercolwidths=[15]*6)
    print(tabulate_respuesta)

   

    subsector_mayor = respuesta['Subsector que más contribuyó']
        #print(subsector_mayor)
    subsector_mayor_filt = filtrar_dic_con_por_llaves(subsector_mayor,['Código subsector económico',
                                              'Nombre subsector económico','Total ingresos netos',
                                          'Total costos y gastos','Total saldo a pagar','Total saldo a favor'])
        
        #print(subsector_mayor_filt)
        
    subsect_mayor_tab = tabulate([subsector_mayor_filt], headers='keys', maxcolwidths =[15]*6, maxheadercolwidths=[15]*6)
    print(subsect_mayor_tab)
        
    print('Para el dicho subsector que más aporto, las actividades que más y menos aportaron respectivamente son:')

    actividad_mas_subsector_mayor = subsector_mayor['Actividad que más contribuyó']
    actividad_menos_subsector_mayor = subsector_mayor['Actividad que menos contribuyó']

    actividad_mas_subsector_mayor_filt = filtrar_dic_con_por_llaves(actividad_mas_subsector_mayor,['Código actividad económica',
                                              'Nombre actividad económica','Total ingresos netos',
                                          'Total costos y gastos','Total saldo a pagar','Total saldo a favor'])
        
        #print(actividad_mas_subsector_mayor_filt)
        
    actividad_menos_subsector_mayor_filt = filtrar_dic_con_por_llaves(actividad_menos_subsector_mayor,['Código actividad económica',
                                              'Nombre actividad económica','Total ingresos netos',
                                          'Total costos y gastos','Total saldo a pagar','Total saldo a favor'])
        

    tab_mayor_mayor = tabulate([actividad_mas_subsector_mayor_filt], headers='keys', maxcolwidths =[15]*6, maxheadercolwidths=[15]*6)
    tab_mayor_menor = tabulate([actividad_menos_subsector_mayor_filt], headers='keys', maxcolwidths =[15]*6, maxheadercolwidths=[15]*6)
    print(tab_mayor_mayor)
    print(tab_mayor_menor)



        ### Ahora con menor

    subsector_menor = respuesta['subsector que menos aportó']
        #print(subsector_mayor)
    subsector_menor_filt = filtrar_dic_con_por_llaves(subsector_menor,['Código subsector económico',
                                              'Nombre subsector económico','Total ingresos netos',
                                          'Total costos y gastos','Total saldo a pagar','Total saldo a favor'])
        
        #print(subsector_mayor_filt)
        
    subsect_menor_tab = tabulate([subsector_menor_filt], headers='keys', maxcolwidths =[15]*6, maxheadercolwidths=[15]*6)
    print(subsect_menor_tab)
        
    print('Para el dicho subsector que MENOS aporto, las actividades que MÁS y MENOS aportaron respectivamente son:')

    actividad_mas_subsector_menor = subsector_menor['Actividad que más contribuyó']
    actividad_menos_subsector_menor = subsector_menor['Actividad que menos contribuyó']

    actividad_mas_subsector_menor_filt = filtrar_dic_con_por_llaves(actividad_mas_subsector_menor,['Código actividad económica',
                                              'Nombre actividad económica','Total ingresos netos',
                                          'Total costos y gastos','Total saldo a pagar','Total saldo a favor'])
        
        #print(actividad_mas_subsector_mayor_filt)
        
    actividad_menos_subsector_menor_filt = filtrar_dic_con_por_llaves(actividad_menos_subsector_menor,['Código actividad económica',
                                              'Nombre actividad económica','Total ingresos netos',
                                          'Total costos y gastos','Total saldo a pagar','Total saldo a favor'])
        

    tab_menor_mayor = tabulate([actividad_mas_subsector_menor_filt], headers='keys', maxcolwidths =[15]*6, maxheadercolwidths=[15]*6)
    tab_menor_menor = tabulate([actividad_menos_subsector_menor_filt], headers='keys', maxcolwidths =[15]*6, maxheadercolwidths=[15]*6)
    print(tab_menor_mayor)
    print(tab_menor_menor)



    
      

    #df_sectores = pd.DataFrame(req_6_lista)
    #df_sectores_imprimir = df_sectores[['Nombre sector económico','Total ingresos netos']]

    
    #print(df_sectores_imprimir)

    print('TAMAÑO: ',req_6_tiempo)
    print('TIEMPO: ', req_6_memory)



def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    anios = input("Ingrese el año que se desea saber informacion ")
    codigo = input("Ingrese el código subsector económico que desea saber sus actividades ")
    numero_acti = input("Ingrese cuantas actividades desea investigar ")
    respuesta = controller.req_7(control, anios,codigo, numero_acti)
    tamanio = len(respuesta)
    if tamanio < int(numero_acti):
        print ("There are only " + str(tamanio)+ " economic activities in subsector " + str(codigo) + " and in the year " + str(anios) )
        print(tabulate(respuesta, headers="keys", tablefmt= "grid", maxcolwidths=15, maxheadercolwidths=15  ))
    else:
        print("These are the " + str(numero_acti) + " lowest cost and expenses in the subsector " + str(codigo) + " in the year " + str(anios))
        print(tabulate(respuesta, headers="keys", tablefmt= "grid", maxcolwidths=15, maxheadercolwidths=15  ))


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista


# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                
                print("Cargando información de los archivos ....\n")
                filename = menu_archivo()
                tipo = menu_maptype()
                factor =0
                memory = menu_espacio()
                if tipo == 'PROBING':
                    factor = menu_factor_PROBING()

                elif tipo == 'CHAINING':
                    factor = menu_factor_CHAINING()

                control = new_controller(tipo,factor)
                tupla = load_data(control,filename,memory)
                print_3_primeros_3_ultimos(control)
                
                print('Tamaño: ')
                print(lt.size(control['model']['Lista actividades general']))
                print('Tiempo: ')
                print(tupla[1])
                print('memoria: ')
                print(tupla[2])
                #dat =mp.get(control['model']['Años'],2015)
                #llaves = mp.keySet(control['model']['Años'])
                

                #print(llaves)
               # print(dat)
            elif int(inputs) == 2:
                print_req_1(control)

            elif int(inputs) == 3:
                print_req_2(control)

            elif int(inputs) == 4:
                anio = input('Ingrese un año: ')
                memory = menu_espacio()
                print_req_3(control,anio,memory)

            elif int(inputs) == 5:
                print_req_4(control)

            elif int(inputs) == 6:
                print_req_5(control)

            elif int(inputs) == 7:
                anio = input('Ingrese un año: ')
                memory = menu_espacio()               
                print_req_6(control,anio,memory)

            elif int(inputs) == 8:
                print_req_7(control)

            elif int(inputs) == 9:
                print_req_8(control)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)
