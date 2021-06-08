"""
Nombre: invertirLista
Entradas: Una lista
Salidas: Retornar la inversa de una lista
Restrecciones: Debe ser una lista
"""
def invertirLista(lista):
    if isinstance (lista, list): 
        if lista==[]:
            return 0
        else:
            return invertirLista_aux(lista,[])
    else:
        print ("Error: Porfavor ingrese una lista")
def invertirLista_aux(lista,newList):
    if lista == []:
        return newList
    else:
        return invertirLista_aux(lista[:-1],newList + [lista[-1]])
        
#--------------------------------------------------------------------------------------#

"""
Nombre: extremosLista
Entradas: Una lista
Salidas: Retornar el numero mayor y el numero menor de la lista.
Restricciones: El parametro debe ser una lista
"""
def extremosLista(lista) :
    if isinstance(lista, list):
        NumMayor = numero_mayor(lista, lista[0])
        NumMMenor = numero_menor(lista, lista[0])
        if (mayor == menor):
            print([mayor])
        else:
            print([menor, mayor])
    else:
        return('Debe ingresar una lista')

 

def num_mayor(lista, num) :
    if (lista == []):
        return num
    elif (num >= lista[0]):
        return num_mayor(lista[1:], num)
    else :
        return num_mayor(lista[1:], lista[0])

 

def num_menor(lista, num) :
    if lista == [] :
        return num
    elif num <= lista[0] :
        return num_menor(lista[1:], num)
    else :
        return num_menor(lista[1:], lista[0])

#==================================================================   
"""
Nombre: eliminarDigitos
Entradas: dos parametros de entradas
Salidas: Retornar el numero sin los numeros eliminados
Restricciones: Las entradas deben ser numeros
"""

def eliminarDigito(num, borrarNumero) :
    if isinstance(num, int) and isinstance(borrarNumero, int) :
        if num == 0 :
            print('Error: debe introducir un digito que no sea cero')
        else :
            cantidadCaracteres = cuentaDigitos(borrarNumero, 0)
            return eliminarDigito_AuxV2(num, borrarNumero, 0, 0, cantidadCaracteres)
    else :
        print('Error: las entradas Num y el borrarNumero deben ser enteros') 

 

def eliminarDigito_Aux(numero, borrarNumero, potencia, nuevoNumero, cantidad) :
    if numero == 0 :
        return nuevoNumero
    elif numero % 10 ** cantidad == borrarNumero :
        return eliminarDigito_Aux(numero // 10 ** cantidad, borrarNumero, potencia, nuevoNumero, cantidad)
    else :
        return eliminarDigito_Aux(numero // 10, borrarNumero, potencia + 1, nuevoNumero + ((numero % 10) * 10 ** potencia), cantidad)

 

def cuentaDigitos(numero, cantidad) :
    if numero == 0 :
        return cantidad
    else :
        return cuentaDigitos(numero // 10, cantidad + 1)

#============================================================================================================================================#
"""
Nombre: nivelesLista
Entradas: Una lista con sublistas
Salidas: Retornar la cantidad de sublistas que contenga cada elemento de la lista
Restricciones: El parametro de entrada debe ser una lista
"""

def nivelesLista(lista) :
    if isinstance(lista, list) :
        return nivelesListaAux(lista, [])
    else :
        print('Debe ingresar una sublista')

 

def nivelesListaAux(lista, contenido):
    if (lista == []):
        return contenido
    else :
        return ListaAux(lista, lista[0], contenido, 0)

 

def ListaAux(lista, sublista, contenido, cantidad) :
    if (sublista == []):
        return nivelesListaAux(lista[1:],contenido+[cantidad+1])
    
    elif isinstance(sublista, list) :
        if (not(isinstance(sublista[0], list))) :
            return ListaAux(lista, sublista[1:], contenido, cantidad)

        else:
            return ListaAux(lista,sublista[0]+sublista[1:],contenido,cantidad+ 1)
    else:
        return ListaAux(lista,sublista[1:],contenido,cantidad)

#========================================================================================#
"""
Nombre: obtenerIndiceslistaVectores
Entradas: Tendra de entrada 3 vectores que elija el usuario
Salidas: Devolver los índices de una lista de vectores cuyo valor sean CERO o un número NEGATIVO
Restricciones: Los vectores deben ser listas

"""



def obtenerIndiceslistaVectores(v1,v2,v3):
    if(isinstance(v1,list) and isinstance(v2,list) and isinstance(v3,list)):
        if (tamañodelista(v1) == tamañodelista(v2) == tamañodelista(v3)):
            if (validarint1(v1,v2,v3)):
                v4=indince(v1,0,[])
                v5=indince(v2,0,[])
                v6=indince(v3,0,[])
                v7=[v4]+[v5]+[v6]
                return v7
            else:
                return -1
        else:
            return -1
    else:
        return "Debe ser una lista"
            
           
def indince(vector,cont,lista):
    if vector== []:
        return lista
    elif vector[0]<=0:
        return indince (vector[1:],cont+1,lista+[cont])
    else:
        return indince(vector[1:],cont+1,lista)

def tamañodelista(v1):
    if v1 == 0:
        print ("La lista no puede estar vacia")
    else:
        return tamañodelistaA(v1,0)

def tamañodelistaA(vector,resultado):
    if vector==[]:
        return resultado
    else:
        return tamañodelistaA(vector[1:],resultado+1)

def validarint1(vector1,vector2,vector3):
    if vector1 ==[] and vector2== [] and vector3==[]:
        return "La lista no debe estar vacia"
    else:
        if (isinstance(vector1[0],int) and isinstance(vector2[0],int) and isinstance(vector3[0],int)):
            return validarint1(vector1[1:],vector2[1:],vector3[1:])
        else:
            return False


    
