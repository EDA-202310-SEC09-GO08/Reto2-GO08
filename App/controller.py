﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import time
import csv
import tracemalloc

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller(tipo, factor):
    """
    Crea una instancia del modelo
    """

    control = {
        "model": None
    }
    control["model"] = model.new_data_structs(tipo,factor)
    
    return control
    


# Funciones para la carga de datos

def load_data(control, filename,memory):
    """
    Carga los datos del reto
    """
    start_time = get_time()

    delta_m = None
    if memory is True:
        tracemalloc.start()
        start_memory = get_memory()  

    file = cf.data_dir + filename
    input_file = csv.DictReader(open(file, encoding='utf-8'))
    catalog = control['model']
    for line in input_file:
        model.add_data(catalog, line)

    model.ordenar_map_anios_para_view(control['model'])
    stop_time =get_time()

    delta = delta_time(start_time, stop_time)

    # finaliza el proceso para medir memoria
    if memory is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        delta_m = delta_memory(stop_memory, start_memory)
        # respuesta con los datos de tiempo y memoria
    return control,delta, delta_m



# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control, anio, sector):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    tiempo_i = get_time()
    columnas = ["Código actividad econñomica", "Nombre actividad económica", "Código subsector económico"
                "Nombre subsector económico", " Total ingresos netos", "Total costos y gastos" , 
                "Total saldo por pagar" , "Total saldo a favor"]
    resultado = model.req_1(control, anio, sector)
    respuesta = model.filtrar_dic_con_por_llaves(resultado , columnas)
    tiempo_f = get_time()
    delta_t = delta_time(tiempo_i, tiempo_f)
    tamanio = 1
    return respuesta , delta_t , tamanio 


def req_2(control,anio, sector):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    tracemalloc.start()  
    start_memory = get_memory()  

    start_time = get_time()
    res = model.req_2(control, anio, sector)
    stop_time =get_time()

    delta = delta_time(start_time, stop_time)
    stop_memory = get_memory()
    tracemalloc.stop()
       
    delta_m = delta_memory(stop_memory, start_memory)

    print("el tiempo " + str(delta))
    print("con memoria " + str(delta_m))
    return res


def req_3(control,anio,memory):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    delta_m = None
    if memory is True:
        tracemalloc.start()
        start_memory = get_memory() 
    start_time = get_time()
    req_3 = model.req_3(control["model"],anio)
    if memory is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        delta_m = delta_memory(stop_memory, start_memory)
        # respuesta con los datos de tiempo y memoria
    
    end_time = get_time()
    delta_t = delta_time(start_time,end_time)
   
    

    return req_3,delta_t, delta_m


def req_4(control , anio):
    """
    Retorna el resultado del requerimiento 4
    """
    tiempo_i = get_time()
    memo_i = get_memory()
    columnas1 = ["Código sector económico", "Nombre sector económico", "Código subsector económico", "Nombre subsector económico",
                 "Total ingresos nectos" , "Total costos y gastos" , "Total saldo por pagar", "Total saldo a favor"]
    columnas2 = ["Código actividad econnómica" , "Nombre actividad económica",
                 "Total costos y gastos nómina", "Total ingresos netos" , 
                 "Total costos y gastos" , "Total saldo por pagar" , "Total saldo a favor"] 
    resultado = model.req_4(control, anio)
    resp_sec = model.filtrar_dic_con_por_llaves(resultado , columnas1)
    resp_act = model.filtrar_dic_con_por_llaves(resultado, columnas2)
    tiempo_f = get_time()
    delta_t = delta_time(tiempo_i , tiempo_f)
    memo_f = get_memory()
    tamanio = delta_memory(memo_f, memo_i)
    return resp_sec ,resp_act ,delta_t , tamanio


def req_5(control, anios):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    tracemalloc.start()  
    start_memory = get_memory()  
    start_time = get_time()
    respuesta = model.req_5(control,anios)
    stop_time =get_time()

    delta = delta_time(start_time, stop_time)
    stop_memory = get_memory()
    tracemalloc.stop()
       
    delta_m = delta_memory(stop_memory, start_memory)
    

    print("el tiempo " + str(delta))
    print("con memoria " + str(delta_m))
    return respuesta 

def req_6(control,anio,memory):
    """
    Retorna el resultado del requerimiento 6
    """
    
     
    delta_m = None
    if memory is True:
        tracemalloc.start()
        start_memory = get_memory() 
    start_time = get_time()
    req_6 = model.req_6(control["model"],anio)
    if memory is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        delta_m = delta_memory(stop_memory, start_memory)
        # respuesta con los datos de tiempo y memoria
    
    end_time = get_time()
    delta_t = delta_time(start_time,end_time)
   
    

    return req_6,delta_t, delta_m

def req_7(control, anios, codigo, num_actividades):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    tracemalloc.start()  
    start_memory = get_memory()  
    start_time = get_time()

    final = model.req_7(control, anios, codigo, num_actividades)
    stop_time =get_time()

    delta = delta_time(start_time, stop_time)
    stop_memory = get_memory()
    tracemalloc.stop()
       
    delta_m = delta_memory(stop_memory, start_memory)

    print("el tiempo " + str(delta))
    print("con memoria " + str(delta_m))
    return final


def req_8(control , anio):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    tiempo_i = get_time()
    memo_i = get_memory()
    columnas1 = ["Código sector económico", "Nombre sector económico", "Código subsector económico", "Nombre subsector económico",
                 "Total impuestos a cargo"
                 "Total ingresos nectos" , "Total costos y gastos" , "Total saldo por pagar", "Total saldo a favor"]
    columnas2 = ["Código actividad econnómica" , "Nombre actividad económica",
                 "Total impuestos a cargo","Total costos y gastos nómina", "Total ingresos netos" , 
                 "Total costos y gastos" , "Total saldo por pagar" , "Total saldo a favor"] 
    resultado = model.req_8(control, anio)
    resp_sec = model.filtrar_dic_con_por_llaves(resultado , columnas1)
    resp_act = model.filtrar_dic_con_por_llaves(resultado, columnas2)
    tiempo_f = get_time()
    delta_t = delta_time(tiempo_i , tiempo_f)
    memo_f = get_memory()
    tamanio = delta_memory(memo_f, memo_i)
    return resp_sec ,resp_act ,delta_t , tamanio

def aux_req8(sector):
    resultado = model.au
    


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
