"""
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs(tipo,factor):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_structs = {'Lista actividades general':None,
                    'Años':None}
    
    data_structs['Lista actividades general']=lt.newList('ARRAY_LIST')

    data_structs['Años']=mp.newMap(40, maptype=tipo , loadfactor=factor)
    return(data_structs)


# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    lt.addLast(data_structs['Lista actividades general'],data)

    add_impuesto_anio(data_structs,data)

    

    
def add_impuesto_anio(data_structs, impuesto):
    years = data_structs['Años']
    anio = impuesto['Año']
    anio = int(float(anio))

    existyear = mp.contains(years,anio)
    if existyear:
        entry = mp.get(years,anio)
        year = me.getValue(entry)
    else:
        year = newYear(anio)
        mp.put(years,anio,year)
    
    lt.addLast(year['Lista'],impuesto)

def newYear(year):
    """
    Esta funcion crea la estructura de libros asociados
    a un año.
    """
    entry = {'Año': "", "Lista": None}
    entry['Año'] = year
    entry['Lista'] = lt.newList('ARRAY_LIST', compareYears)
    return entry

def organizar_sector(data_structs,subdivision):
    llaves = mp.keySet(data_structs["model"]["Años"])
    #los años de los datos, en una lista
    date = mp.newMap()
    # el diccionario que tendra los datos(respuesta)
    
    
    i = 1 
    while i <= lt.size(llaves):
        fecha = lt.getElement(llaves,i)
        #cada llave en los datos, va de uno en uno por la lista
        sector = mp.newMap()
        #se crea para organizar sectores
        
        
        especifico = mp.get(data_structs["model"]["Años"], fecha)
        #da un dic de llave valor acorde al año dado
        valores = especifico["value"]["Lista"]
        #devuelve el valor de cada año 

        a = 1 
        
        
        while a <= lt.size(valores):
            lista = lt.getElement(valores,a)
            #cada dato dentro del año especifico 
            numero_sec = lista[subdivision]
            # cada numero del sector 
            
            
            esta = mp.contains(sector,numero_sec)
            #verificar si esta 
            if esta == False:
                #crea una nueva lista y le agrega el valor dado 
                list_sec = lt.newList()
                lt.addLast(list_sec, lista)
                mp.put(sector,numero_sec,list_sec)
            else:
                #solo agrega el valor dado 
                
                agregar = devolver_value(sector,numero_sec)
                lt.addLast(agregar,lista)
            a+=1
        i +=1
        mp.put(date,fecha,sector)
    return date



def new_data(anio, cod_acti, nom_acti, cod_sector, nom_sector, cod_subsec, nom_subsec, costos_gastos_nom, apor_seguridad, apor_entidades, efec_equivalentes,inv_instru, 
             cuentas_cob, inventario, propiedades, otros_act, total_patrim_bruto, pasivos, total_patrim_liquido, ingresos_ordin, ingresos_finan, ingresos_otr, total_ingresos_brut,
             devoluciones_rebaj, ingresos_no_renta, total_netos, costos, gastos_ad, gastos_dist, gastos_finan, gastos_otr, total_c_g, renta_liq_ord, perdida_liq, compensaciones, 
             renta_liq, renta_presu, renta_exen, renta_grava, renta_liq_grava, ingreso_ganan_oca, costos_ganan_oca, ganan_oca_no_grava, ganan_oca_grava, impuesto_rlg, 
             descuentos_trib, imp_net_rent, imp_ganan_oca, total_imp_carg, antic_anio_ant, saldo_afav_ant, autoreten, otras_reten, total_reten, anti_rent_sig, 
             saldo_paga_imp, sanciones, total_s_pagar, total_favor):
    
    data = {'Año': 0, "Código actividad económica": "","Nombre actividad económica": "","Código sector económico": "","Nombre sector económico": "",
    "Código subsector económico": "","Nombre subsector económico": "", "Costos y gastos nómina": "", "Aportes seguridad": "", "Aportes a entidades": "", "Efectivo y equivalentes": "",
    "Inversiones e instrumentos":"", "Cuentas y otros por cobrar":"", "Inventarios": "", "Propiedades": "", "Otros activos":"", "Total patrimonio bruto":"", "Pasivos":"", 
    "Total patrimonio líquido":"", "Ingresos ordinarios":"", "Ingresos financieros":"", "Otros ingresos": "", "Total ingresos brutos":"", "Devoluciones, rebajas":"", 
    "Ingresos no renta":"","Total ingresos netos": "",  "Costos":"", "Gastos administración":"", "Gastos distribución":"", "Gastos financieros":"", "Otros gastos":"",
    "Total costos y gastos": "", "Renta líquida ordinaria":"","Pérdida líquida":"",  "Compensaciones":"", "Renta líquida":"","Renta presuntiva":"",  "Renta exenta":"",
    "Rentas gravables":"", "Renta líquida gravable":"", "Ingresos ganancias ocasionales":"", "Costos ganancias ocasionales":"", "Ganancias ocasionales no gravadas":"", 
    "Ganancias ocasionales gravables":"", "Impuesto RLG":"", "Descuentos tributarios":"", "Impuesto neto de renta":"", "Impuesto ganancias ocasionales":"", 
    "Total Impuesto a cargo":"", "Anticipo renta año anterior":"", "Saldo a favor año anterior":"", "Autorretenciones":"", "Otras retenciones":"", "Total retenciones":"",
    "Anticipo renta siguiente año":"", "Saldo a pagar por impuesto":"", "Sanciones":"", "Total saldo a pagar": "","Total saldo a favor": ''}

    data["Año"] = anio
    data["Código actividad económica"] = cod_acti
    data["Nombre actividad económica"] = nom_acti
    data["Código sector económico"] = cod_sector
    data["Nombre sector económico"] = nom_sector
    data["Código subsector económico"] = cod_subsec
    data["Nombre subsector económico"] = nom_subsec
    data["Costos y gastos nómina"] = costos_gastos_nom
    data["Aportes seguridad"] = apor_seguridad
    data["Aportes a entidades"] = apor_entidades
    data["Efectivo y equivalentes"] = efec_equivalentes
    data["Inversiones e instrumentos"] = inv_instru
    data["Cuentas y otros por cobrar"] = cuentas_cob
    data["Inventarios"] = inventario
    data["Propiedades"] = propiedades
    data["Otros activos"] = otros_act
    data["Total patrimonio bruto"] = total_patrim_bruto
    data["Pasivos"] = pasivos
    data["Total patrimonio líquido"] = total_patrim_liquido
    data["Ingresos ordinarios"] = ingresos_ordin
    data["Ingresos financieros"] = ingresos_finan
    data["Otros ingresos"] = ingresos_otr
    data["Total ingresos brutos"] = total_ingresos_brut
    data["Devoluciones, rebajas"] =devoluciones_rebaj
    data["Ingresos no renta"] = ingresos_no_renta
    data["Total ingresos netos"] = total_netos
    data["Costos"] = costos
    data["Gastos administración"] = gastos_ad
    data["Gastos distribución"] = gastos_dist
    data["Gastos financieros"] = gastos_finan
    data["Otros gastos"] = gastos_otr
    data["Total costos y gastos"] = total_c_g
    data["Renta líquida ordinaria"] = renta_liq_ord
    data["Pérdida líquida"] = perdida_liq
    data["Compensaciones"] = compensaciones
    data["Renta líquida"] = renta_liq
    data["Renta presuntiva"] = renta_presu
    data["Renta exenta"] = renta_exen
    data["Rentas gravables"] = renta_grava
    data["Renta líquida gravable"] = renta_liq_grava
    data["Ingresos ganancias ocasionales"] = ingreso_ganan_oca
    data["Costos ganancias ocasionales"] = costos_ganan_oca
    data["Ganancias ocasionales no gravadas"] = ganan_oca_no_grava
    data["Ganancias ocasionales gravables"] = ganan_oca_grava
    data["Impuesto RLG"] = impuesto_rlg
    data["Descuentos tributarios"] = descuentos_trib
    data["Impuesto neto de renta"]= imp_net_rent
    data["Impuesto ganancias ocasionales"] = imp_ganan_oca
    data["Total Impuesto a cargo"] = total_imp_carg
    data["Anticipo renta año anterior"] = antic_anio_ant
    data["Saldo a favor año anterior"] = saldo_afav_ant
    data["Autorretenciones"] = autoreten
    data["Otras retenciones"] = otras_reten
    data["Total retenciones"] = total_reten
    data["Anticipo renta siguiente año"] = anti_rent_sig
    data["Saldo a pagar por impuesto"] = saldo_paga_imp
    data["Sanciones"] = sanciones
    data["Total saldo a pagar"] = total_s_pagar
    data["Total saldo a favor"] = total_favor

    return data


# Funciones de consulta
def devolver_value(map, key):
    llave_valor = mp.get(map, key)
    valor = me.getValue(llave_valor)
    return valor 

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs, anio, codigo):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    dic = organizar_sector(data_structs, "Código sector económico")
    #dic con sector y anios organizados
    anio_buscado = devolver_value(dic, int(anio))
    #dic del anio
    sector_buscado = devolver_value(anio_buscado, codigo)
    #devuelve acorde al anio y el sector, en este caso una lista 
    final = encontrar_mayor_criterio(sector_buscado, "Total saldo a favor")
    #el mayor
    res = filtrar_dic_con_por_llaves(final,["Código actividad económica", "Nombre actividad económica", "Código sector económico","Nombre sector económico",
                 "Código subsector económico", 'Nombre subsector económico', "Total ingresos netos", "Total costos y gastos",
                 "Total saldo a pagar", "Total saldo a favor"])
    # organiza a lo que quiero que muestre 

    return res
                






     ####### REQ 3 Y FUNCIONES ASOCOIADAS





def crear_lista_subsectores_por_anio(lista_actividades):
   
    dic_subsecs ={}
    ## primero crea diccionario
    lista_actividades = lt.iterator(lista_actividades)
    
    for impuesto in lista_actividades:
        llave_subsector_dado =impuesto['Código subsector económico']
        if llave_subsector_dado not in dic_subsecs.keys():
            
            dict_subsector_dado = {}
            dict_subsector_dado['Año']=impuesto['Año']
            dict_subsector_dado['Código sector económico']=impuesto['Código sector económico']
            dict_subsector_dado['Nombre sector económico']=impuesto['Nombre sector económico']
            dict_subsector_dado['Código subsector económico']=impuesto['Código subsector económico']
            dict_subsector_dado['Nombre subsector económico']=impuesto['Nombre subsector económico']
            dict_subsector_dado['Total retenciones']=float(impuesto['Total retenciones'])
            dict_subsector_dado['Total ingresos netos']=float(impuesto['Total ingresos netos'])
            dict_subsector_dado['Total costos y gastos']=float(impuesto['Total costos y gastos'])
            dict_subsector_dado['Total saldo a pagar']=float(impuesto['Total saldo a pagar'])
            dict_subsector_dado['Total saldo a favor']=float(impuesto['Total saldo a favor'])
            dict_subsector_dado['Primeras y últimas 3 actividades en contribuir'] = 0

            dic_subsecs[llave_subsector_dado]=dict_subsector_dado
        else:
            ## Va contando los totales
            dict_subsector_dado =dic_subsecs[llave_subsector_dado]
            dict_subsector_dado['Total retenciones']+=float(impuesto['Total retenciones'])
            dict_subsector_dado['Total ingresos netos']+=float(impuesto['Total ingresos netos'])
            dict_subsector_dado['Total costos y gastos']+=float(impuesto['Total costos y gastos'])
            dict_subsector_dado['Total saldo a pagar']+=float(impuesto['Total saldo a pagar'])
            dict_subsector_dado['Total saldo a favor']+=float(impuesto['Total saldo a favor'])
    
     ### Lista Tad       
    lista_subsects=lt.newList(datastructure="ARRAY_LIST")
    for llave in dic_subsecs.keys():
        lt.addLast(lista_subsects,dic_subsecs[llave])

    return lista_subsects

def agregar_lista_de_6_a_subsector(subsector, lista_de_actividades_un_anio):
        
        ### vuelve array en objeto iterable
        lista_de_actividades_un_anio_1 = lt.iterator(lista_de_actividades_un_anio)
        codigo_subsect = subsector['Código subsector económico']
       
       
       
        #### Crear sublista del año solo de 1 subsecto Array
        lista_acotada_de_ACTIVIDADES_anio_y_subsector = lt.newList('ARRAY_LIST')
        #print(lt.size(lista_de_actividades_un_anio))
        #print(codigo_subsect)
       
       
       
       
        ### Agrega a la lista acotada los elementos filtrados por subsector
        for actividad in lista_de_actividades_un_anio_1:
           # print(type(actividad))
           # print(actividad['Código subsector económico'])

           ##Compara que sea del subsector dado
            if codigo_subsect == actividad['Código subsector económico']:
                lt.addLast(lista_acotada_de_ACTIVIDADES_anio_y_subsector,actividad)
                
        ### Ordena lista acotada por RETENCION
        quk.sort(lista_acotada_de_ACTIVIDADES_anio_y_subsector,sort_criteria_retenciones)
        #print(lista_acotada_de_ACTIVIDADES_anio_y_subsector)
        tamanio = lt.size(lista_acotada_de_ACTIVIDADES_anio_y_subsector)
        #print(tamanio)
        #### Crea lista PYTHON de 6 actividades relevantes 
        lista_6_activ_por_anio = []

        ### Condición para prevenir error out of range
        if tamanio>=6:
        
        
            
        
            lista_6_activ_por_anio.append(lt.getElement(lista_acotada_de_ACTIVIDADES_anio_y_subsector,1))
            lista_6_activ_por_anio.append(lt.getElement(lista_acotada_de_ACTIVIDADES_anio_y_subsector,2))
            lista_6_activ_por_anio.append(lt.getElement(lista_acotada_de_ACTIVIDADES_anio_y_subsector,3))
            lista_6_activ_por_anio.append(lt.getElement(lista_acotada_de_ACTIVIDADES_anio_y_subsector,tamanio-2))
            lista_6_activ_por_anio.append(lt.getElement(lista_acotada_de_ACTIVIDADES_anio_y_subsector,tamanio-1))
            lista_6_activ_por_anio.append(lt.getElement(lista_acotada_de_ACTIVIDADES_anio_y_subsector,tamanio))
        else:
            i =1
            while i<=tamanio:
                lista_6_activ_por_anio.append(lt.getElement(lista_acotada_de_ACTIVIDADES_anio_y_subsector,i))
                i+=1
        ### Añade la lista como elemento al dict subsect
        subsector['Primeras y últimas 3 actividades en contribuir']= lista_6_activ_por_anio
        #print(len(lista_6_activ_por_anio))
        return subsector


def encontrar_menor(lista, criterio):
    
    i =0
    tamanio = lt.size(lista)
    respuesta ={}
    menor = 9999999999999
    while i <= tamanio:
        exacto = lt.getElement(lista,i)
        if float(exacto[criterio])<float(menor):
            respuesta = exacto
            menor = exacto[criterio]
        i+=1
    return respuesta

def sort_criteria_retenciones(a,b):

        cod_1 = a['Total retenciones'].split()[0].split('/')[0]
        cod_2 = b['Total retenciones'].split()[0].split('/')[0]
        return(float(cod_1)<float(cod_2))

def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    lista_dicts_menores_anios = lt.newList('ARRAY_LIST')
    
    mapa_anios = data_structs['Años']

    lista_llaves_anios = quk.sort(mp.keySet(mapa_anios))
    
    tamanio_lista_llaves = lt.size(lista_llaves_anios)
    i = 1

    while i <= tamanio_lista_llaves:

        llave_anio_dado = lt.getElement(lista_llaves_anios,i)

        lista_actividades_un_anio_dado = devolver_value(mapa_anios,lista_llaves_anios)

        ####crea lista subsectkores patra el año dado
        lista_subsects_un_anio_dado = crear_lista_subsectores_por_anio(lista_actividades_un_anio_dado)

        ##encuentra menor subsect por retenciones
        menor = encontrar_menor(lista_subsects_un_anio_dado, 'Total retenciones')
        agregar_lista_de_6_a_subsector(menor,lista_actividades_un_anio_dado)
        lt.addLast(lista_dicts_menores_anios,menor)

        i +=1
    quk.sort(lista_dicts_menores_anios,sort_criteria)
    return lista_dicts_menores_anios



def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs, anio):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    dic = organizar_sector(data_structs, "Código subsector económico" )
    #dic subdividido
    
    
    dic_del_anio = devolver_value(dic,int(anio))
    #dic del subsector en el año
    llaves = mp.keySet(dic_del_anio)

    i = 1
    sumas = lt.newList(cmpfunction="ARRAY_LIST")
    #estara la suma del descuento
    sectores = lt.newList()
    #estara cual sector (mismo orden al de arriba)

    while i<=lt.size(llaves):
        numero = 0
        pos = lt.getElement(llaves, i )
        # pos es igual a el numero del subsector 

        lt.addLast(sectores, i)
        #posicion en la lista de llaves 

        valor = devolver_value(dic_del_anio,pos)
        #lista de dicionarios 
        numero = suma_variable(valor,"Descuentos tributarios" )
        #suma descuentos totales por subsector 

        lt.addLast(sumas, numero)
        i+=1
    
    posicion = encontrar_mayor_list(sumas)
    #en que posicion de las llaves(subsector) esta el de mayores descuentos 

    sector_mayor = lt.getElement(llaves,posicion[1])
    #nombre del subsector 

    para_organizar = devolver_value(dic_del_anio, sector_mayor)
    #lista de los subsectores 
    merg.sort(para_organizar,sort_criteria_descuentos_tributarios)
    #lista subsectores organizados de menor a mayor por descuento 

    sacar_basicos = lt.getElement(para_organizar,1)
    #encontrar las cosas ue comparten todos

    
    
    respuesta = {"Código sector económico": sacar_basicos["Código sector económico"],
                 "Nombre sector económico":sacar_basicos["Nombre sector económico"] ,
                  "Código subsector económico": sacar_basicos["Código subsector económico"],
                   "Código subsector económico":sacar_basicos["Código subsector económico"],
                   "Descuentos tributarios": posicion[0]
                   }
    
    #diccionario con todo lo necesario
    codigos= [ "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor" ]

    for cod in codigos:
        #sumar cada variable 
        la_suma=suma_variable(para_organizar,cod)
        respuesta[cod] = la_suma
    
    heads = ["Código actividad económica", "Nombre actividad económica", "Código sector económico","Nombre sector económico",
                 "Código subsector económico", 'Nombre subsector económico',"Descuentos tributarios", "Total ingresos netos", "Total costos y gastos",
                 "Total saldo a pagar", "Total saldo a favor"]
    
    final = filtrar_lista_dics_por(para_organizar, heads)
    #asignarle diccionario a cada uno por lo que quiero que muestre 
    

    return respuesta, final, sector_mayor


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs, anio, codigo, num_actividades):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    dic = organizar_sector(data_structs, "Código subsector económico" )
    #dic subdividido
    
    
    dic_del_anio = devolver_value(dic,int(anio))
    #dic segun el año pedido
    esta = mp.contains(dic_del_anio,codigo)
    if esta:
        lista_sub_sector = devolver_value(dic_del_anio, str(codigo))
     #lista segun el codigo pedido

        merg.sort(lista_sub_sector, sort_criteria_total_costos_gastos)
     #organizado 

        tamanio = lt.size(lista_sub_sector)
        respuesta = lt.newList(cmpfunction="ARRAY_LIST")

        if int(num_actividades) < tamanio:
            i =1
            while i <= int(num_actividades):
                valor = lt.getElement(lista_sub_sector,i)
                lt.addLast(respuesta,valor)
                i+=1
        else:
            respuesta = lista_sub_sector
    
        heads = ["Código actividad económica", "Nombre actividad económica", "Código sector económico","Nombre sector económico",
                    "Código subsector económico", 'Nombre subsector económico', "Total ingresos netos", "Total costos y gastos",
                    "Total saldo a pagar", "Total saldo a favor"]
        final = filtrar_lista_dics_por(respuesta,heads)
    else:
        final = "No hay ese subsector en el año indicado "
    return final 
        




def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass


def compareYears(year1, year2):
    if (int(year1) == int(year2)):
        return 0
    elif (int(year1) > int(year2)):
        return 1
    else:
        return -1
    

def sort_criteria_descuentos_tributarios(a,b):

        cod_1 = a["Descuentos tributarios"].split()[0].split('/')[0]
        cod_2 = b["Descuentos tributarios"].split()[0].split('/')[0]
        return(float(cod_1)<float(cod_2))

def sort_criteria_total_costos_gastos(a,b):

        cod_1 = a["Total costos y gastos"].split()[0].split('/')[0]
        cod_2 = b["Total costos y gastos"].split()[0].split('/')[0]
        return(float(cod_1)<float(cod_2))

def encontrar_mayor_list (list):
    i = 1 
    tamanio = lt.size(list)
    mayor = 0 
    
    
    while i<=tamanio:
        exacto = lt.getElement(list,i)
        if float(exacto)>float(mayor):
            mayor = exacto
            
            pos = i
        i+=1

    return mayor, pos

def encontrar_mayor_criterio(lista,criterio):
    i = 1 
    tamanio = lt.size(lista)
    mayor = 0 
    respuesta = {}
    
    while i<=tamanio:
        exacto = lt.getElement(lista,i)
        if float(exacto[criterio])>float(mayor):
            mayor = exacto[criterio]
            respuesta = exacto
        i+=1

    
    return respuesta

def suma_variable(lista, suma):
    tamanio = lt.size(lista)
    i = 1
    valor = 0

    while i <= tamanio:
        pos = lt.getElement(lista, i)
        valor += int(pos[suma])
        i+=1
    
    
    
    return valor
                

def filtrar_lista_dics_por(lista_dics,lista_columnas):
    
    lista_filt = []

    tamanio_lista = lt.size(lista_dics)
    i = 1

    while i<=tamanio_lista:
        a = lt.getElement(lista_dics,i)
        dic_filt_dado = filtrar_dic_con_por_llaves(a,lista_columnas)
        lista_filt.append(dic_filt_dado)
        i+=1
    return lista_filt

def filtrar_dic_con_por_llaves(dic, lista_de_columnas_aMostrar):
    dic_filt ={}
    for llave in lista_de_columnas_aMostrar:
        dic_filt[llave]=dic[llave]

    return dic_filt