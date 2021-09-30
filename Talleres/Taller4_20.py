#!/usr/bin/env python
# coding: utf-8

# <img src="Archivos/miad4.png" width=800x>
# 
# # Manejo de archivos
# 
# En este taller importarás y manejarás archivos y la información que contienen al resolver diversos ejercicios.
# 
# ## Habilidades en práctica
# 
# **1.** Aplicar los métodos y los atributos principales de las cadenas de texto. <br>
# **2.** Importar y exportar archivos de texto en formato .txt o .csv por medio de un *file handle*. <br>
# **3.** Procesar archivos de texto delimitados y no delimitados valiendose del uso de los métodos de las cadenas de texto y de los *file handle*. <br>
# 
# ## Instrucciones
# 
# En cada uno de los siguientes ejercicios deberás escribir el código solicitado estrictamente en las celdas indicadas para ello, teniendo en cuenta las siguientes recomendaciones:
# 
# * No crear, eliminar o modificar celdas de este Notebook (salvo lo que se te indique), pues puede verse afectado el proceso de calificación automática.
# * La calificación se realiza de manera automática con datos diferentes a los proporcionados en este taller. Por consiguiente, tu código debe funcionar para diferentes instancias de cada uno de los ejercicios; una instancia hace referencia al valor de los parámetros.
# * La calificación de cada ejercicio depende del valor que retorne la función especificada en su enunciado. Por lo tanto, aunque implementes funciones adicionales, es escencial que utilices los nombres propuestos en los enunciados de los ejercicios para implementar la función definitiva.
# 
# Esta es una actividad calificada y, por lo tanto, debe ser resuelta individualmente.
# 
# A continuación puedes ver un ejemplo de los ejercicios que encontrarás en este taller.

# ### Ejemplo
# 
# Implementa una función llamada `multiplicacion` que reciba dos números ingresados por parámetro y retorne la multiplicación de estos dos.
# 
# *Esta función debería retornar un número*

# In[ ]:


# Implementa tu respuesta en esta celda

def multiplicacion(num1, num2):
    
    respuesta = num1 * num2
    
    return respuesta


# ### Ejercicio 1
# 
# En la siguiente celda encuentras declarada una variable que almacena una cadena de caracteres.

# In[111]:


# No modifiques esta celda

cadena = "Archivos de texto"


# Implementa una función llamada `sustituir` que reciba por parámetro una cadena de texto (por ejemplo, la variable `cadena`) y retorne otra cadena en la cual se intercambien el segundo caracter y el penúltimo caracter.
# 
# *Esta función debe retornar una cadena de texto.*

# In[112]:


# YOUR CODE HERE
def sustituir(texto):
    texto= list(texto)
    sc = texto[1]
    pc= texto [-2]
    texto[1]= pc
    texto[-2]=sc
    
    textofinal = "".join(texto)
    return textofinal

print(sustituir(cadena))

#raise NotImplementedError()


# In[113]:


## AUTO-CALIFICADOR

# Base variables
cadena = "Archivos de texto"
cadena_prueba = "Una cadena con mayor cantidad de caracteres"

# Caso 1: no existe la función.
try:
    sustituir
    assert type(sustituir) == type(lambda:None)
except:
    raise NotImplementedError("No existe una función llamada sustituir.",)
    
# Caso 2: la función es interrumpida por errores durante su ejecución.
try:
    sustituir(cadena)
    sustituir(cadena_prueba)
except:
    raise RuntimeError("Tu función produce un error al ejecutarse.")

# Caso 3: no retorna una cadena
assert type(sustituir(cadena_prueba)) == str, f"Tu función debe retornar un valor de tipo {str.__name__}."

# Caso 4: respuesta explicita
assert sustituir(cadena_prueba) != "Atchivos de texro", "Tu respuesta es incorrecta para una instancia diferente. Utiliza el parámetro."

# Caso 5: retorna la misma cadena
assert sustituir(cadena_prueba) != cadena_prueba, "Tu función retorna la misma cadena que recibe por parámetro sin alterar."

# Caso 6: devuelve una cadena de longitud errada
assert len(sustituir(cadena_prueba)) == len(cadena_prueba), "Tu función puede no estar tomando en cuenta todos los caracteres de la cadena que recibe por parámetro."

# Caso 7: asigna el mismo valor a ambas posiciones
assert sustituir(cadena_prueba)[1] != sustituir(cadena_prueba)[-2], "Tu función asigna el mismo caracter en las posiciones segunda y penúltima."

# Caso 8: confunde indexación iniciada en cero
assert sustituir(cadena_prueba)[2] != "s", "Tu función una posición que no debería. Recuerda que en python la indexación inicia en 0"

# Caso 9: retorna una cadena distinta de la esperada
assert sustituir(cadena_prueba) == "Uea cadena con mayor cantidad de caracterns", "Tu función no retorna la cadena correcta."
assert sustituir(cadena) == "Atchivos de texro", "Tu función no retorna la cadena correcta."

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ### Ejercicio 2 
# 
# En la siguiente celda encuentras declarada una variable que almacena una cadena de caracteres representativa de la ruta relativa para el archivo `"tesoro.txt"`. Recuerda que para los talleres, los archivos necesarios están en el subdirectorio `"Archivos"`.

# In[2]:


# No modifiques esta celda

directorio = "./Archivos/tesoro.txt"


# Implementa una función llamada `archivo_a_lista` que reciba por parámetro una cadena de texto que represente la dirección de un archivo (por ejemplo, la variable `directorio`) y retorne una lista donde cada elemento es una linea del archivo encontrado.
# 
# *Esta función debe retornar una lista de cadenas de texto.*

# In[67]:


# YOUR CODE HERE
def archivo_a_lista(archivo):
    f = open(archivo, "r")
    return f.readlines()

print(archivo_a_lista(directorio))
    
#raise NotImplementedError()


# In[68]:


## AUTO-CALIFICADOR

# Base variables
directorio = "./Archivos/tesoro.txt"
directorio_prueba = "./Archivos/tesoro_2.txt"

# Caso 1: no existe la función.
try:
    archivo_a_lista
    assert type(archivo_a_lista) == type(lambda:None)
except:
    raise NotImplementedError("No existe una función llamada archivo_a_lista.",)
    
# Caso 2: la función es interrumpida por errores durante su ejecución.
try:
    archivo_a_lista(directorio)
    archivo_a_lista(directorio_prueba)
except:
    raise RuntimeError("Tu función produce un error al ejecutarse. Asegurate de que estés usando una dirección relativa a la ubicación de este notebook.")

# Caso 3: no retorna una lista
assert type(archivo_a_lista(directorio_prueba)) == list, f"Tu función debe retornar un valor de tipo {list.__name__}."

# Caso 4: retorna una lista vacía
assert len(archivo_a_lista(directorio_prueba)) != 0, "Tu función retorna una lista vacía, cuando debería devolver una lista con las filas del archivo .txt"

# Caso 5: respuesta explicita
assert archivo_a_lista(directorio_prueba)[0] != "Principales tenedores de títulos del tesoro americano en lo que se lleva del 2020\n", "Tu respuesta es incorrecta para una instancia diferente. Asegurate de utilizar el parámetro."
assert archivo_a_lista(directorio)[0] != 'Estimado estudiante.\n', "Tu respuesta es incorrecta para una instancia diferente. Asegurate de utilizar el parámetro."

# Caso 7: devuelve una lista de longitud errada
assert len(archivo_a_lista(directorio_prueba)) == 8, "Tu función puede no estar tomando en cuenta todas las filas del archivo de texto deseado."

# Caso 8: la lista es incorrecta
resultado_prueba = ['Estimado estudiante.\n',
                    '\n',
                    'Este archivo de texto es para uso exclusivo del auto-calificador.\n',
                    'Evite borrar, mover o editar de cualquier forma su contenido.\n',
                    '\n',
                    '\n',
                    'Agradecemos su colaboración,\n',
                    'Equipo de Laboratorio Computacional de Analytics.\n']

assert archivo_a_lista(directorio_prueba) == resultado_prueba, "Tu función devuelve una lista errada."

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ### Ejercicio 3 
# 
# En la siguiente celda encuentras declarada una variable que almacena una lista de paises y otra que guarda el resultado de ejecutar tu respuesta al [ejercicio 2](#Ejercicio-2).

# In[114]:


# No modifiques esta celda

lista_paises = ['Japón', 'Francia']
lineas = archivo_a_lista(directorio)


# Implementa una función llamada `filtrar_paises` que reciba por parámetro una lista de nombres de paises (por ejemplo, la variable `lista_paises`) y retorne una lista donde cada elemento es la linea del archivo `"tesoro.txt"`, correspondiente a cada país de la lista que se recibe por parámetro. Asegurate de haber realizado el ejercicio 2 correctamente y de usar la variable `lineas` en tu implementación para este ejercicio. A continuación, un ejemplo:
# 
# Ejecutar la función `filtrar_paises(["Suiza","Noruega"])` debe resultar en la siguiente lista:
# 
# ```python
# ['Suiza\t247.4\t243.1\t241.3\t244.6\t243.7\t238.1\t237.5\t\n',
#  'Noruega\t89.5\t87.6\t93.2\t98.0\t103.3\t97.7\t90.1\t\n']
# ```
# 
# *Esta función debe retornar una lista de cadenas de texto.*

# In[115]:


# YOUR CODE HERE
def filtrar_paises(lista_paises):
    resultado = []
    for i in lista_paises:
        for j in range(len(lineas)):
            if lineas[j].find(i)!=-1:
                resultado.append(lineas[j])
    return resultado

print(filtrar_paises(lista_paises))


# In[116]:


## AUTO-CALIFICADOR

# Base variables
directorio = "./Archivos/tesoro.txt"
directorio_prueba = "./Archivos/tesoro_2.txt"
lista_paises = ['Japón', 'Francia']
lista_paises_prueba = ['Suiza', 'Noruega', 'Tailandia', 'Kuwait']
resultado_prueba_ej_2 = ['Estimado estudiante.\n',
                         '\n',
                         'Este archivo de texto es para uso exclusivo del auto-calificador.\n',
                         'Evite borrar, mover o editar de cualquier forma su contenido.\n',
                         '\n',
                         '\n',
                         'Agradecemos su colaboración,\n',
                         'Equipo de Laboratorio Computacional de Analytics.\n']


# Caso 0: no ha implementado el ejercicio 2:
try:
    assert archivo_a_lista(directorio_prueba) == resultado_prueba_ej_2
except:
    raise NotImplementedError("Debes haber implementado correctamente el ejercicio 2.")

lineas = archivo_a_lista(directorio)

# Caso 1: no existe la función.
try:
    filtrar_paises
    assert type(filtrar_paises) == type(lambda:None)
except:
    raise NotImplementedError("No existe una función llamada filtrar_paises.",)
    
# Caso 2: la función es interrumpida por errores durante su ejecución.
try:
    filtrar_paises(lista_paises)
    filtrar_paises(lista_paises_prueba)
except:
    raise RuntimeError("Tu función produce un error al ejecutarse.")

# Caso 3: no retorna una lista
assert type(filtrar_paises(lista_paises_prueba)) == list, f"Tu función debe retornar un valor de tipo {list.__name__}."

# Caso 4: retorna una lista vacía
assert len(filtrar_paises(lista_paises_prueba)) != 0, "Tu función retorna una lista vacía, cuando debería devolver una lista con las filas solicitadas del archivo .txt."

# Caso 5: respuesta explicita
assert filtrar_paises(lista_paises_prueba)[0] != 'Japón\t1261.5\t1260.4\t1266.5\t1272.6\t1268.6\t1211.8\t1155.2\t\n', "Tu respuesta es incorrecta para una instancia diferente. Asegurate de utilizar el parámetro."

# Caso 6: devuelve una lista de longitud errada
assert len(filtrar_paises(lista_paises_prueba)) == len(lista_paises_prueba), "Tu función puede no estar tomando en cuenta todos los paises de la lista que recibe por parámetro."

# Caso 7: la lista es incorrecta
resultado = ['Japón\t1261.5\t1260.4\t1266.5\t1272.6\t1268.6\t1211.8\t1155.2\t\n',
             'Francia\t144.2\t130.5\t137.7\t156.0\t147.6\t134.0\t127.7\t\n']

resultado_prueba = ['Suiza\t247.4\t243.1\t241.3\t244.6\t243.7\t238.1\t237.5\t\n',
                    'Noruega\t89.5\t87.6\t93.2\t98.0\t103.3\t97.7\t90.1\t\n',
                    'Tailandia\t85.5\t85.8\t80.5\t81.8\t91.3\t96.0\t90.5\t\n',
                    'Kuwait\t44.9\t43.6\t44.5\t40.1\t43.6\t41.9\t43.3\t\n']

assert filtrar_paises(lista_paises) == resultado, "Tu función devuelve una lista errada."
assert filtrar_paises(lista_paises_prueba) == resultado_prueba, "Tu función devuelve una lista errada."

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ### Ejercicio 4
# 
# Jorge y Juan apostaron al que hiciera la mejor predicción de la tabla final de las eliminatorias sudamericanas para el mundial de Rusia 2018. Jorge definió el siguiente pronóstico: 
# 
# |Puesto|<center>País</center>|
# |-------|-----------|
# |1| Brasil|
# |2| Argentina|
# |3 | Uruguay|
# |4| Colombia|
# |5| Chile|
# |6| Ecuador|
# |7| Perú|
# |8| Paraguay|
# |9| Venezuela|
# |10| Bolivia|
# 
# Mientras que Juan definió el siguiente pronóstico:
# 
# |Puesto|<center>País</center>|
# |-------|-----------|
# |1| Brasil|
# |2| Uruguay|
# |3 | Colombia|
# |4| Argentina|
# |5| Ecuador|
# |6| Chile|
# |7| Paraguay|
# |8| Perú|
# |9| Venezuela|
# |10| Bolivia|
# 
# 
# El criterio elegido para decidir quién gana la apuesta fue el error cuadrático medio (ECM). El cual, para este ejemplo específico, tendría la siguiente ecuación: 
# 
# $$
# ECM= \frac{EC}{N} = \frac{\sum \limits _{j=1} ^{10} (Y_{j}-\hat{Y}_{j})^2}{10}
# $$
# 
# 
# Para calcular el ECM primero se calcula y eleva al cuadrado la diferencia entre la posición predicha ($\hat{Y}_{j}$) y la posición que realmente ocupó el equipo ($Y_{j}$). Por ejemplo, supongamos que esta fue la tabla final de las eliminatorias de Rusia 2018. Los errores cuadráticos (EC) asociados con cada predicción serían los siguientes.
# 
# 
# |Puesto|<center>País</center>|EC(Jorge)|EC(Juan)|
# |-----|--------|-----|-----|
# |1|Brasil|0|0|
# |2|Uruguay|1|0|
# |3|Argentina|1|1|
# |4|Paraguay|16|9|
# |5|Colombia|1|4|
# |6|Chile|1|0|
# |7|Ecuador|1|4|
# |8|Perú|1|0|
# |9|Venezuela|0|0|
# |10|Bolivia|0|0|
# 
# 
# Después se calcula el promedio de los errores cuadráticos que en este caso sería de 2.2 para la predicción realizada por Jorge y de 1.8 para la predicción realizada por Juan. Siendo que el error cuadrático medio de Juan fue inferior al de Jorge, Juan sería el ganador.
# 
# Jorge y Juan decidieron entonces usar la informaciòn del artículo de Wikipedia (2020) sobre las eliminatorias a Rusia2018. Puntualmente copiaron y pegaron la "Tabla de Posiciones Final" disponible en el artículo, en un archivo de texto llamado `"Eliminatorias.txt"`. Este archivo contiene la tabla ordenada con la clasificación final de los países así como otros datos deportivos que en este caso no nos interesa analizar (puntos, goles a favor, goles en contra, etc.).
# 
# En la siguiente celda encuentras declaradas dos variables que almacenan en orden la clasificación pronosticada de Jorge y Juan respectivamente.

# In[154]:


# No modifiques esta celda

pronostico_jorge = ["Brasil", "Argentina", "Uruguay", "Colombia", "Chile", "Ecuador", "Perú", "Paraguay", "Venezuela", "Bolivia"]
pronostico_juan = ["Brasil", "Uruguay", "Colombia", "Argentina", "Ecuador", "Chile", "Paraguay", "Perú", "Venezuela", "Bolivia"]


# Implementa una función llamada `ECM` que reciba por parámetro una lista con el prónostico de Juan, una con el pronóstico de Jorge (en ese orden, por ejemplo, las variables `pronostico_jorge` y `pronostico_juan`). Tu función debe importar los resultados del archivo `"Eliminatorias.txt"` y retornar una tupla con el $ ECM $ de Jorge y Juan (en ese orden).

# In[174]:


# YOUR CODE HERE
def ECM(pronostico_jorge,pronostico_juan):
    lista_col2 = []        
    with open("./Archivos/Eliminatorias.txt",'r') as archivo:
        archivo = archivo.readlines()
        for i in archivo[1:]: 
            # Separamos cada línea en sus dos columnas de interes
            archivo_lineas = i.split()
            # Añadimos el valor que toma el registro actual a la lista correspondiente a cada columna.
            lista_col2.append(archivo_lineas[1])
        
        EC1=0
        EC2=0
        for i in lista_col2:
            real= lista_col2.index(i)
            forecastjorge = pronostico_jorge.index(i)
            forecastjuan = pronostico_juan.index(i)
            EC1 += (forecastjorge-real)**2
            EC2 += (forecastjuan-real)**2
        
        return (EC1/10,EC2/10)       

print(ECM(pronostico_jorge,pronostico_juan))


#raise NotImplementedError()


# In[176]:


## AUTO-CALIFICADOR

# Base variables
pronostico_jorge = ["Brasil", "Argentina", "Uruguay", "Colombia", "Chile", "Ecuador", "Perú", "Paraguay", "Venezuela", "Bolivia"]
pronostico_juan = ["Brasil", "Uruguay", "Colombia", "Argentina", "Ecuador", "Chile", "Paraguay", "Perú", "Venezuela", "Bolivia"]

pronostico_jorge_prueba = ["Argentina", "Chile", "Ecuador", "Perú", "Uruguay", "Colombia", "Paraguay", "Venezuela", "Brasil", "Bolivia"]
pronostico_juan_prueba = ["Argentina", "Uruguay", "Brasil", "Ecuador", "Chile", "Paraguay", "Colombia", "Perú", "Venezuela", "Bolivia"]

# Caso 1: no existe la función.
try:
    ECM
    assert type(ECM) == type(lambda:None)
except:
    raise NotImplementedError("No existe una función llamada ECM.")
    
# Caso 2: la función es interrumpida por errores durante su ejecución.
try:
    ECM(pronostico_jorge, pronostico_juan)
    ECM(pronostico_jorge_prueba, pronostico_juan_prueba)
except:
    raise RuntimeError("Tu función produce un error al ejecutarse.")

# Caso 3: no retorna una tupla
assert type(ECM(pronostico_jorge_prueba, pronostico_juan_prueba)) == tuple, f"Tu función debe retornar un valor de tipo {tuple.__name__}."

# Caso 4: retorna una tupla de tamaño incorrecto
assert len(ECM(pronostico_jorge_prueba, pronostico_juan_prueba)) == 2, "Tu función debe retornar una tupla de dos elementos."

# Caso 5: retorna una tupla pero no de floats
assert type(ECM(pronostico_jorge_prueba, pronostico_juan_prueba)[0]) == float and type(ECM(pronostico_jorge_prueba, pronostico_juan_prueba)[1]) == float, f"Los elementos de la tupla que retorna tu función no son de tipo {float.__name__}."

# Caso 6: respuesta explicita
assert ECM(pronostico_jorge_prueba, pronostico_juan_prueba) != (1.4, 2.2), "La respuesta de tu función es incorrecta para una instancia diferente. Asegurate de utilizar el parámetro."

# Caso 7: orden incorrecto parámetros
assert ECM(pronostico_juan, pronostico_jorge) == (2.2, 1.4), "La respuesta de tu función es correcta pero presenta los resultados en el orden equivocado."

# Caso 8: valores incorrectos
assert ECM(pronostico_jorge, pronostico_juan) == (1.4, 2.2), "El cálculo de tus EMC es errado."
assert ECM(pronostico_jorge_prueba, pronostico_juan_prueba) == (12.8, 4.6), "El cálculo de tus EMC es errado."

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ## Referencias 
#  
#  Clasificación de Conmebol para la Copa Mundial de Fútbol de 2022. (12 de noviembre de 2020). En Wikipedia. https://es.wikipedia.org/wiki/Clasificaci%C3%B3n_de_Conmebol_para_la_Copa_Mundial_de_F%C3%BAtbol_de_2022

# ## Créditos
# 
# __Autor(es)__: Jorge Esteban Camargo Forero, Alejandro Mantilla Redondo, Diego Alejandro Cely Gómez
#  
#  __Fecha última actualización__: 17/08/2021
