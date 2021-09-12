#!/usr/bin/env python
# coding: utf-8

# <img src="Archivos/miad4.png" width=800x>
# 
# # Estructuras de control: condicionales y ciclos
# 
# En este taller utilizarás condicionales simples y compuestos, y ciclos para resolver diversos problemas. 
# 
# 
# ## Habilidades en práctica
# 
# Al desarrollar este taller podrás verificar tu progreso para:
# 
# **1.** Utilizar los tres tipos de operadores más frecuentes para construir expresiones lógicas.<br>
# **2.** Implementar condicionales simples y compuestos.<br>
# **3.** Implementar diferentes tipos de ciclos según su condición de parada.<br>
# 
# 
# ## Instrucciones
# 
# En cada uno de los siguientes ejercicios deberás escribir el código solicitado estrictamente en las celdas indicadas para ello, teniendo en cuenta las siguientes recomendaciones:
# 
# * No crear, eliminar o modificar celdas de este Notebook (salvo lo que se te indique), pues puede verse afectado el proceso de calificación automática.
# * La calificación se realiza de manera automática con datos diferentes a los proporcionados en este taller. Por consiguiente, tu código debe funcionar para diferentes instancias de cada uno de los ejercicios; una instancia hace referencia al valor de los parámetros.
# * La calificación de cada ejercicio depende del valor que tome la variable especificada en su enunciado. Por lo tanto, aunque declares variables adicionales en tu código, es escencial que utilices los nombres de las variables propuestas en los enunciados de los ejercicios para guardar el resultado final.
# 
# A continuación puedes ver un ejemplo de los ejercicios que encontrarás en este taller.

# ### Ejemplo
# 
# En la siguiente celda encuentras la edad de Diego y de Felipe.

# In[ ]:


# No modifiques esta celda

Diego = 25
Felipe = 23


# Almacena el nombre del mayor entre Diego y Felipe en una variable llamada `resp`.

# In[ ]:


# Implementa tu respuesta en esta celda

if Diego > Felipe:
    resp = "Diego"
else:
    resp = "Felipe"


# ### Ejercicio 1
# 
# En la siguiente celda encuentras declaradas dos variables que almacenan números enteros.

# In[5]:


# No modifiques esta celda

num_1 = 2
num_2 = 3


# Almacena en una variable, con nombre `mayor`, el mayor número entre los valores de las variables `num_1` y `num_2`. Si ambas variables tienen el mismo valor, puedes escoger almacenar el valor de `num_1` o `num_2` en la variable `mayor`.

# In[8]:


# YOUR CODE HERE
mayor= max(num_1,num_2)

#raise NotImplementedError()


# In[9]:


## PRUEBAS

#--------------
# INSTANCIA 1
#--------------

# Base variables
num_1 = 7
num_2 = 5

try:
    # Caso 1: no existe la variable.
    try:
        mayor
    except:
        raise NotImplementedError("No declaraste una variable llamada mayor.",)
        
    # Caso 2: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
    
    # Caso 3: el código modifica los parametros del problema
    try:
        assert num_1 == 7
        assert num_2 == 5
    except:
        raise AssertionError("Tu código no debe modificar los datos del problema.")
    
    # Caso 4: no es de tipo int.
    assert type(mayor) == int, f"Tu variable mayor no es de tipo {int.__name__}."

    # Caso 5: el código no utiliza las variables num_1 y num_2
    assert _i.find("num_1") >= 0, "Tu código no utiliza la variable num_1."
    assert _i.find("num_2") >= 0, "Tu código no utiliza la variable num_2."

    # Caso 6: la respuesta es correcta
    assert mayor == 7, "Tu implementación presenta errores cuando num_1 es mayor a num_2."
        
except:
    # Restaurar variables base originales
    num_1 = 2
    num_2 = 3
    raise

finally:
    # Restaurar variables base originales
    num_1 = 2
    num_2 = 3

#--------------
# INSTANCIA 2
#--------------

# Base variables
num_1 = 4
num_2 = 5

try:
    # Caso 1: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
    
    # Caso 2: no es de tipo int.
    assert type(mayor) == int, f"Tu variable mayor no es de tipo {int.__name__}."

    # Caso 3: la respuesta es correcta
    assert mayor == 5, "Tu implementación presenta errores cuando num_2 es mayor a num_1."
        
except:
    # Restaurar variables base originales
    num_1 = 2
    num_2 = 3
    raise

finally:
    # Restaurar variables base originales
    num_1 = 2
    num_2 = 3   

#--------------
# INSTANCIA 3
#--------------

# Base variables
num_1 = 2
num_2 = 2

try:
    # Caso 1: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
    
    # Caso 2: no es de tipo int.
    assert type(mayor) == int, f"Tu variable mayor no es de tipo {int.__name__}."

    # Caso 3: la respuesta es correcta
    assert mayor == 2, "Tu implementación presenta errores cuando num_1 y num_2 son iguales."
        
except:
    # Restaurar variables base originales
    num_1 = 2
    num_2 = 3
    raise

finally:
    # Restaurar variables base originales
    num_1 = 2
    num_2 = 3

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ### Ejercicio 2
# 
# En la siguiente celda encuentras declarado un elemento y una lista.

# In[16]:


# No modifiques esta celda

elemento = "e"
lista = ["b", "c", "a", "d"]


# Si `elemento` no pertenece a `lista`, agrégalo. En caso contrario, no modifiques la lista `lista`.

# In[2]:


# YOUR CODE HERE

#variable=0

#for i in range(len(lista)):
    #if elemento == lista[i]:
        #variable=1
        #break

#if variable == 0:
    #lista.append(elemento)

if elemento not in lista :
    lista.append(elemento)
    
lista
        
#raise NotImplementedError()


# In[3]:


## PRUEBAS

#--------------
# INSTANCIA 1
#--------------

# Base variables
elemento = "y"
lista = ["x", "z", "y", "w"]

try:
    # Caso 1: no existe la variable.
    try:
        lista
    except:
        raise NotImplementedError("No existe una variable llamada lista.",)
        
    # Caso 2: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
    
    # Caso 3: el código modifica los parametros del problema
    try:
        assert elemento == "y"
        assert lista == ["x", "z", "y", "w"]
    except:
        raise AssertionError("Tu código no debe modificar los datos del problema.")
    
    # Caso 4: no es una lista.
    assert type(lista) == list, f"Tu variable lista no es de tipo {list.__name__}."
    
    # Caso 5: el código no utiliza las variables lista y elemento
    assert _i.find("lista") >= 0, "Tu código no utiliza la variable lista."
    assert _i.find("elemento") >= 0, "Tu código no utiliza la variable elemento."
        
    # Caso 6: la lista contiene valores de tipo incorrecto
    for i in lista:
        assert type(i) == str, f"Tu lista contiene valores que no son de tipo {str.__name__}."

    # Caso 7: la lista no contiene los valores correctos
    try:
        assert lista.count('x') >= 1
        assert lista.count('y') >= 1
        assert lista.count('z') >= 1
        assert lista.count('w') >= 1
    except AssertionError as e:
        e.args += ("Tu lista no contiene los valores correctos.",)
        raise e

    # Caso 8: la lista tiene el tamaño incorrecto
    assert len(lista) == 4, "Tu lista tiene un tamaño mayor al esperado."

    # Caso 9: la lista es correcta
    try:
        assert lista[0] == 'x'
        assert lista[1] == 'z'
        assert lista[2] == 'y'
        assert lista[3] == 'w'
    except AssertionError as e:
        e.args += ("Los valores de tu lista están desordenados.",)
        raise e
        
except:
    # Restaurar variables base originales
    elemento = "e"
    lista = ["b", "c", "a", "d"]
    raise

finally:
    # Restaurar variables base originales
    elemento = "e"
    lista = ["b", "c", "a", "d"]

#--------------
# INSTANCIA 2
#--------------

# Base variables
elemento = "v"
lista = ["x", "z", "y", "w"]

try:
    # Caso 1: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
    
    # Caso 2: no es una lista.
    assert type(lista) == list, f"Tu variable lista no es de tipo {list.__name__}."
        
    # Caso 3: la lista contiene valores de tipo incorrecto
    for i in lista:
        assert type(i) == str, f"Tu lista contiene valores que no son de tipo {str.__name__}."

    # Caso 4: la lista no contiene los valores correctos
    try:
        assert lista.count('x') >= 1
        assert lista.count('y') >= 1
        assert lista.count('z') >= 1
        assert lista.count('w') >= 1
        assert lista.count('v') >= 1
    except AssertionError as e:
        e.args += ("Tu lista no contiene los valores correctos.",)
        raise e

    # Caso 5: la lista tiene el tamaño incorrecto
    assert len(lista) == 5, "Tu lista tiene un tamaño mayor al esperado."

    # Caso 6: la lista es correcta
    try:
        assert lista[0] == 'x'
        assert lista[1] == 'z'
        assert lista[2] == 'y'
        assert lista[3] == 'w'
        assert lista[4] == 'v'
    except AssertionError as e:
        e.args += ("Los valores de tu lista están desordenados.",)
        raise e
        
except:
    # Restaurar variables base originales
    elemento = "e"
    lista = ["b", "c", "a", "d"]
    raise

finally:
    # Restaurar variables base originales
    elemento = "e"
    lista = ["b", "c", "a", "d"]

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ### Ejercicio 3
# 
# En la siguiente celda encuentras declaradas dos variables que almacenan números enteros.

# In[4]:


# No modifiques esta celda

num = 7
divisor = 3


# Si el resultado de la división entre `num` y `divisor` (`num`/`divisor`) es un número entero, almacénalo en una variable llamada `division_o_residuo`. De lo contrario, almacena en la variable `division_o_residuo` el residuo de la división.

# In[5]:


# YOUR CODE HERE
if num % divisor == 0:
    division_o_residuo = num / divisor
else:
    division_o_residuo = num % divisor
    
#raise NotImplementedError()


# In[6]:


## PRUEBAS

#--------------
# INSTANCIA 1
#--------------

# Base variables
num = 6
divisor = 3

try:
    # Caso 1: no existe la variable.
    try:
        division_o_residuo
    except:
        raise NotImplementedError("No declaraste una variable llamada division_o_residuo.",)
        
    # Caso 2: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
    
    # Caso 3: el código modifica los parametros del problema
    try:
        assert num == 6
        assert divisor == 3
    except:
        raise AssertionError("Tu código no debe modificar los datos del problema.")
    
    # Caso 4: no es de tipo float.
    assert type(division_o_residuo) == float, f"Tu variable division_o_residuo no es de tipo {float.__name__}."

    # Caso 5: el código no utiliza las variables num y divisor
    assert _i.find("num") >= 0, "Tu código no utiliza la variable num."
    assert _i.find("divisor") >= 0, "Tu código no utiliza la variable divisor."

    # Caso 6: la respuesta es correcta
    assert division_o_residuo == 2, "Tu implementación presenta errores cuando el resultado de la división entre num y divisor es un número entero."
        
except:
    # Restaurar variables base originales
    num = 7
    divisor = 3
    raise

finally:
    # Restaurar variables base originales
    num = 7
    divisor = 3

#--------------
# INSTANCIA 2
#--------------

# Base variables
num = 7
divisor = 4

try:
    # Caso 1: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
    
    # Caso 2: no es de tipo int.
    assert type(division_o_residuo) == int, f"Tu variable division_o_residuo no es de tipo {int.__name__}."

    # Caso 3: la respuesta es correcta
    assert division_o_residuo == 3, "Tu implementación presenta errores cuando el resultado de la división entre num y divisor NO es un número entero."
    
except:
    # Restaurar variables base originales
    num = 7
    divisor = 3
    raise

finally:
    # Restaurar variables base originales
    num = 7
    divisor = 3

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ### Ejercicio 4
# 
# En la siguiente celda encuentras la velocidad (km/h) que registraron cuatro competidores en una carrera de atletismo.

# In[8]:


# No modifiques esta celda

vel_Camilo = 10.5
vel_Esteban = 9.3
vel_Alejandro = 9.8
vel_David = 10.2


# Escribe el código que determina cuál fue el competidor más rápido de la carrera y  almacena su nombre en una variable llamada `mas_rapido`.

# In[217]:


# YOUR CODE HERE

if max(vel_Camilo,vel_Esteban,vel_Alejandro,vel_David) == vel_Camilo:
    mas_rapido = 'Camilo'
elif max(vel_Camilo,vel_Esteban,vel_Alejandro,vel_David) == vel_Esteban:
    mas_rapido = 'Esteban'
elif max(vel_Camilo,vel_Esteban,vel_Alejandro,vel_David) == vel_Alejandro:
    mas_rapido = 'Alejandro'
elif max(vel_Camilo,vel_Esteban,vel_Alejandro,vel_David) == vel_David:
    mas_rapido = 'David'


#raise NotImplementedError()


# In[218]:


## PRUEBAS

#--------------
# INSTANCIA 1
#--------------

# Base variables
vel_Camilo = 10
vel_Esteban = 11
vel_Alejandro = 9
vel_David = 9.5

try:
    # Caso 1: no existe la variable.
    try:
        mas_rapido
    except:
        raise NotImplementedError("No declaraste una variable llamada mas_rapido.",)

    # Caso 2: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
    
    # Caso 3: el código modifica los parametros del problema
    try:
        assert vel_Camilo == 10
        assert vel_Esteban == 11
        assert vel_Alejandro == 9
        assert vel_David == 9.5
    except:
        raise AssertionError("Tu código no debe modificar los datos del problema.")
    
    # Caso 4: no es de tipo str.
    assert type(mas_rapido) == str, f"Tu variable mas_rapido no es de tipo {str.__name__}."

    # Caso 5: el código no utiliza las variables vel_Camilo, vel_Alejandro, vel_David y vel_Esteban
    assert _i.find("vel_Camilo") >= 0, "Tu código no utiliza la variable vel_Camilo."
    assert _i.find("vel_Esteban") >= 0, "Tu código no utiliza la variable vel_Esteban."
    assert _i.find("vel_Alejandro") >= 0, "Tu código no utiliza la variable vel_Alejandro."
    assert _i.find("vel_David") >= 0, "Tu código no utiliza la variable vel_David."

    # Caso 6: la respuesta es correcta
    assert mas_rapido == 'Esteban', "Tu respuesta es incorrecta."
        
except:
    # Restaurar variables base originales
    vel_Camilo = 10.5
    vel_Esteban = 9.3
    vel_Alejandro = 9.8
    vel_David = 10.2
    raise

finally:
    # Restaurar variables base originales
    vel_Camilo = 10.5
    vel_Esteban = 9.3
    vel_Alejandro = 9.8
    vel_David = 10.2
    
#--------------
# INSTANCIA 2
#--------------

# Base variables
vel_Camilo = 10.5
vel_Esteban = 9.3
vel_Alejandro = 9.8
vel_David = 10.2

try:
    # Caso 1: no existe la variable.
    try:
        mas_rapido
    except:
        raise NotImplementedError("No declaraste una variable llamada mas_rapido.",)

    # Caso 2: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
    
    # Caso 3: el código modifica los parametros del problema
    try:
        assert vel_Camilo == 10.5
        assert vel_Esteban == 9.3
        assert vel_Alejandro == 9.8
        assert vel_David == 10.2
    except:
        raise AssertionError("Tu código no debe modificar los datos del problema.")
    
    # Caso 4: no es de tipo str.
    assert type(mas_rapido) == str, f"Tu variable mas_rapido no es de tipo {str.__name__}."

    # Caso 5: el código no utiliza las variables vel_Camilo, vel_Alejandro, vel_David y vel_Esteban
    assert _i.find("vel_Camilo") >= 0, "Tu código no utiliza la variable vel_Camilo."
    assert _i.find("vel_Esteban") >= 0, "Tu código no utiliza la variable vel_Esteban."
    assert _i.find("vel_Alejandro") >= 0, "Tu código no utiliza la variable vel_Alejandro."
    assert _i.find("vel_David") >= 0, "Tu código no utiliza la variable vel_David."

    # Caso 6: la respuesta es correcta
    assert mas_rapido == 'Camilo', "Tu respuesta es incorrecta."
        
except:
    # Restaurar variables base originales
    vel_Camilo = 10.5
    vel_Esteban = 9.3
    vel_Alejandro = 9.8
    vel_David = 10.2
    raise

finally:
    # Restaurar variables base originales
    vel_Camilo = 10.5
    vel_Esteban = 9.3
    vel_Alejandro = 9.8
    vel_David = 10.2

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ### Ejercicio 5
# 
# El gerente de una tienda de ropa desea tener información acerca de la ocupación de su local. En la siguiente celda encuentras el número actual de visitantes y la capacidad máxima del local.

# In[214]:


# No modifiques esta celda

num_actual = 20
cap_maxima = 45


# Según las indicaciones del gerente, si el número actual de visitantes es menor o igual al 40% de la capacidad máxima, se considera que el nivel de ocupación es `"Bajo”`; si el número actual de visitantes es mayor al 40% y menor o igual al 80% de la capacidad máxima, se considera que el nivel de ocupación es `"Medio”`; y si el número actual de visitantes es mayor al 80% de la capacidad máxima, se considera que el nivel de ocupación es `"Alto”`. 
# 
# Además, al gerente le interesa saber el valor de un indicador según el nivel de ocupación. Si el nivel de ocupación es `"Bajo”`, le interesa saber el número actual de visitantes; si el nivel de ocupación es `"Medio”`, le interesa saber el porcentaje de ocupación (`num_actual/cap_maxima`); y si el nivel de ocupación es `"Alto”`, le interesa saber la diferencia entre la capacidad máxima y el número actual de visitantes.
# 
# Almacena en una lista con nombre `info` los siguientes dos elementos en el orden en el que se presentan a continuación:
# 1. El nivel de ocupación (`"Bajo”`, `"Medio”`, `"Alto”`).
# 2. El indicador de interés para el gerente según el nivel de ocupación.

# In[215]:


# YOUR CODE HERE

if (num_actual/cap_maxima) <= 0.4:
    info= ['Bajo', num_actual]
elif (num_actual/cap_maxima) > 0.4 and (num_actual/cap_maxima) <= 0.8:
    info= ['Medio', num_actual/cap_maxima]
elif (num_actual/cap_maxima) > 0.8:
    info= ['Alto', (cap_maxima-num_actual)]

print(info)

#raise NotImplementedError()


# In[216]:


## PRUEBAS

#--------------
# INSTANCIA 1
#--------------

# Base variables
num_actual = 35
cap_maxima = 40

try:
    # Caso 1: no existe la variable.
    try:
        info
    except:
        raise NotImplementedError("No declaraste una variable llamada info.",)
    
    # Caso 2: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
    
    # Caso 3: el código modifica los parametros del problema
    try:
        assert num_actual == 35
        assert cap_maxima == 40
    except:
        raise AssertionError("Tu código no debe modificar los datos del problema.")
    
    # Caso 4: no es una lista.
    assert type(info) == list, f"Tu variable info no es de tipo {list.__name__}."
    
    # Caso 5: el código no utiliza las variables num_actual y cap_maxima
    assert _i.find("num_actual") >= 0, "Tu código no utiliza la variable num_actual."
    assert _i.find("cap_maxima") >= 0, "Tu código no utiliza la variable cap_maxima."
    
    # Caso 6: la lista tiene el tamaño incorrecto
    assert len(info) == 2, "Tu lista no tiene el tamaño correcto."
        
    # Caso 7: la lista contiene valores de tipo incorrecto
    assert type(info[0]) == str, f"La primera posición de tu lista contiene un valor que no es de tipo {str.__name__}."
    assert type(info[1]) == int, f"La segunda posición de tu lista contiene un valor que no es de tipo {int.__name__}."

    # Caso 8: la lista es correcta
    assert info[0] == 'Alto', "El nivel de ocupación de tu respuesta es incorrecto cuando el porcentaje de ocupación es mayor al 80%."
    assert info[1] == 5, "El indicador de tu respuesta es incorrecto cuando el nivel de ocupación es: Alto."
        
except:
    # Restaurar variables base originales
    num_actual = 20
    cap_maxima = 45
    raise

finally:
    # Restaurar variables base originales
    num_actual = 20
    cap_maxima = 45

#--------------
# INSTANCIA 2
#--------------

# Base variables
num_actual = 20
cap_maxima = 40

try:
    # Caso 1: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
    
    # Caso 2: no es una lista.
    assert type(info) == list, f"Tu variable info no es de tipo {list.__name__}."
    
    # Caso 3: la lista tiene el tamaño incorrecto
    assert len(info) == 2, "Tu lista no tiene el tamaño correcto."
        
    # Caso 4: la lista contiene valores de tipo incorrecto
    assert type(info[0]) == str, f"La primera posición de tu lista contiene un valor que no es de tipo {str.__name__}."
    assert type(info[1]) == float, f"La segunda posición de tu lista contiene un valor que no es de tipo {float.__name__}."

    # Caso 5: la lista es correcta
    assert info[0] == 'Medio', "El nivel de ocupación de tu respuesta es incorrecto cuando el porcentaje de ocupación es mayor al 40% y menor o igual al 80%."
    assert info[1] == 0.5, "El indicador de tu respuesta es incorrecto cuando el nivel de ocupación es: Medio."
        
except:
    # Restaurar variables base originales
    num_actual = 20
    cap_maxima = 45
    raise

finally:
    # Restaurar variables base originales
    num_actual = 20
    cap_maxima = 45

#--------------
# INSTANCIA 3
#--------------

# Base variables
num_actual = 10
cap_maxima = 40

try:
    # Caso 1: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
    
    # Caso 2: no es una lista.
    assert type(info) == list, f"Tu variable info no es de tipo {list.__name__}."
    
    # Caso 3: la lista tiene el tamaño incorrecto
    assert len(info) == 2, "Tu lista no tiene el tamaño correcto."
        
    # Caso 4: la lista contiene valores de tipo incorrecto
    assert type(info[0]) == str, f"La primera posición de tu lista contiene un valor que no es de tipo {str.__name__}."
    assert type(info[1]) == int, f"La segunda posición de tu lista contiene un valor que no es de tipo {int.__name__}."

    # Caso 5: la lista es correcta
    assert info[0] == 'Bajo', "El nivel de ocupación de tu respuesta es incorrecto cuando el porcentaje de ocupación es menor o igual al 40%."
    assert info[1] == 10, "El indicador de tu respuesta es incorrecto cuando el nivel de ocupación es: Bajo."
        
except:
    # Restaurar variables base originales
    num_actual = 20
    cap_maxima = 45
    raise

finally:
    # Restaurar variables base originales
    num_actual = 20
    cap_maxima = 45

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ### Ejercicio 6
# 
# Pizzeria Uniandes tiene dos tipos de ingredientes para sus pizzas:
# 
# 1. Vegetarianos
# 2. No-vegetarianos
# 
# Un cliente puede pedir tres ingredientes para su pizza. Si ninguno de los ingredientes es vegetariano, la pizza se categoriza como `'No vegetariana'`; si uno o dos de los ingredientes es vegetariano, la pizza se clasifica como `'Semi vegetariana'`; y si todos ingredientes son vegetarianos, la pizza se clasifica como `'Vegetariana'`.
# 
# En la siguiente celda encuentras las dos listas de ingredientes y tres ingredientes para crear una pizza.

# In[222]:


# No modifiques esta celda

vegetarianos = ['Tomate', 'Champiñones', 'Cebolla']
no_vegetarianos = ['Pepperoni', 'Pollo', 'Jamón']

ingrediente_1 = 'Champiñones'
ingrediente_2 = 'Pollo'
ingrediente_3 = 'Cebolla'


# Almacena en una variable, con nombre `tipo`, la categoría (`'No vegetariana'`, `'Semi vegetariana'`, `'Vegetariana'`) correspondiente a la pizza creada a partir de los tres ingredientes declarados en la celda anterior. 

# In[224]:


# YOUR CODE HERE


if ingrediente_1 in vegetarianos and ingrediente_2 in vegetarianos and ingrediente_3 in vegetarianos:
    tipo= 'Vegetariana'
elif ingrediente_1 in no_vegetarianos and ingrediente_2 in no_vegetarianos and ingrediente_3 in no_vegetarianos:
    tipo= 'No vegetariana'
elif ingrediente_1 in vegetarianos or ingrediente_2 in vegetarianos or ingrediente_3 in vegetarianos:
    tipo= 'Semi vegetariana'
        
print(tipo)

#raise NotImplementedError()


# In[225]:


## PRUEBAS

#--------------
# INSTANCIA 1
#--------------

# Base variables
vegetarianos = ['Tomate', 'Champiñones', 'Pimenton']
no_vegetarianos = ['Salami', 'Pollo', 'Jamón']

ingrediente_1 = 'Pollo'
ingrediente_2 = 'Salami'
ingrediente_3 = 'Jamón'

try:
    # Caso 1: no existe la variable.
    try:
        tipo
    except:
        raise NotImplementedError("No declaraste una variable llamada tipo.",)    

    # Caso 2: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
    
    # Caso 3: el código modifica los parametros del problema
    try:
        assert vegetarianos == ['Tomate', 'Champiñones', 'Pimenton']
        assert no_vegetarianos == ['Salami', 'Pollo', 'Jamón']
        assert ingrediente_1 == 'Pollo'
        assert ingrediente_2 == 'Salami'
        assert ingrediente_3 == 'Jamón'
    except:
        raise AssertionError("Tu código no debe modificar los datos del problema.")
        
    # Caso 4: no es de tipo str.
    assert type(tipo) == str, f"Tu variable tipo no es de tipo {str.__name__}."

    # Caso 5: el código no utiliza las variables ingrediente_1, ingrediente_2 e ingrediente_3
    assert _i.find("ingrediente_1") >= 0, "Tu código no utiliza la variable ingrediente_1."
    assert _i.find("ingrediente_2") >= 0, "Tu código no utiliza la variable ingrediente_2."
    assert _i.find("ingrediente_3") >= 0, "Tu código no utiliza la variable ingrediente_3."

    # Caso 6: la respuesta es correcta
    assert tipo == 'No vegetariana', "Tu implementación presenta errores cuando el tipo de una pizza es: No vegetariana."
        
except:
    # Restaurar variables base originales
    vegetarianos = ['Tomate', 'Champiñones', 'Cebolla']
    no_vegetarianos = ['Pepperoni', 'Pollo', 'Jamón']
    ingrediente_1 = 'Champiñones'
    ingrediente_2 = 'Pollo'
    ingrediente_3 = 'Cebolla'
    raise

finally:
    # Restaurar variables base originales
    vegetarianos = ['Tomate', 'Champiñones', 'Cebolla']
    no_vegetarianos = ['Pepperoni', 'Pollo', 'Jamón']
    ingrediente_1 = 'Champiñones'
    ingrediente_2 = 'Pollo'
    ingrediente_3 = 'Cebolla'

#--------------
# INSTANCIA 2
#--------------

# Base variables
vegetarianos = ['Tomate', 'Champiñones', 'Pimenton']
no_vegetarianos = ['Salami', 'Pollo', 'Jamón']

ingrediente_1 = 'Pimenton'
ingrediente_2 = 'Champiñones'
ingrediente_3 = 'Tomate'

try:
    # Caso 1: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
        
    # Caso 2: no es de tipo str.
    assert type(tipo) == str, f"Tu variable tipo no es de tipo {str.__name__}."

    # Caso 3: la respuesta es correcta
    assert tipo == 'Vegetariana', "Tu implementación presenta errores cuando el tipo de una pizza es: Vegetariana."
        
except:
    # Restaurar variables base originales
    vegetarianos = ['Tomate', 'Champiñones', 'Cebolla']
    no_vegetarianos = ['Pepperoni', 'Pollo', 'Jamón']
    ingrediente_1 = 'Champiñones'
    ingrediente_2 = 'Pollo'
    ingrediente_3 = 'Cebolla'
    raise

finally:
    # Restaurar variables base originales
    vegetarianos = ['Tomate', 'Champiñones', 'Cebolla']
    no_vegetarianos = ['Pepperoni', 'Pollo', 'Jamón']
    ingrediente_1 = 'Champiñones'
    ingrediente_2 = 'Pollo'
    ingrediente_3 = 'Cebolla'


#--------------
# INSTANCIA 3
#--------------

# Base variables
vegetarianos = ['Tomate', 'Champiñones', 'Pimenton']
no_vegetarianos = ['Salami', 'Pollo', 'Jamón']

ingrediente_1 = 'Pimenton'
ingrediente_2 = 'Salami'
ingrediente_3 = 'Tomate'

try:
    # Caso 1: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
        
    # Caso 2: no es de tipo str.
    assert type(tipo) == str, f"Tu variable tipo no es de tipo {str.__name__}."

    # Caso 3: la respuesta es correcta
    assert tipo == 'Semi vegetariana', "Tu implementación presenta errores cuando el tipo de una pizza es: Semi vegetariana."
        
except:
    # Restaurar variables base originales
    vegetarianos = ['Tomate', 'Champiñones', 'Cebolla']
    no_vegetarianos = ['Pepperoni', 'Pollo', 'Jamón']
    ingrediente_1 = 'Champiñones'
    ingrediente_2 = 'Pollo'
    ingrediente_3 = 'Cebolla'
    raise

finally:
    # Restaurar variables base originales
    vegetarianos = ['Tomate', 'Champiñones', 'Cebolla']
    no_vegetarianos = ['Pepperoni', 'Pollo', 'Jamón']
    ingrediente_1 = 'Champiñones'
    ingrediente_2 = 'Pollo'
    ingrediente_3 = 'Cebolla'

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ### Ejercicio 7
# 
# Utiliza un ciclo para almacenar los números pares del 1 al `n` (incluyéndolo) en una lista con nombre `pares`. La lista debe quedar ordenada ascendentemente. 

# In[145]:


# No modifiques esta celda

n = 100


# In[155]:


# YOUR CODE HERE
pares=[]
for i in range(1,n+1):
    if i%2 == 0:
        pares.append(i)

print(pares)

#raise NotImplementedError()


# In[156]:


## PRUEBAS

#--------------
# INSTANCIA 1
#--------------

# Base variables
n = 300

try:
    # Caso 1: no existe la variable.
    try:
        pares
    except:
        raise NotImplementedError("No declaraste una variable llamada pares.",)

    # Caso 2: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
    
    # Caso 3: el código modifica los parametros del problema
    try:
        assert n == 300
    except:
        raise AssertionError("Tu código no debe modificar los datos del problema.")

    # Caso 4: no es una lista.
    assert type(pares) == list, f"Tu variable pares no es de tipo {list.__name__}."
    
    # Caso 5: el código no utiliza ciclos
    assert _i.find("for") >= 0 or _i.find("while") >= 0, "Tu código no utiliza ciclos."

    # Caso 6: la lista contiene valores de tipo incorrecto
    for i in pares:
        assert type(i) == int, f"Tu lista contiene valores que no son de tipo {int.__name__}."

    # Caso 7: la lista tiene el tamaño incorrecto
    assert len(pares) == 150, "Tu lista no tiene el tamaño correcto."

    # Caso 8: la lista es correcta
    assert pares == list(range(2,301,2)), "Tu respuesta es incorrecta."

except:
    # Restaurar variables base originales
    n = 100
    raise

finally:
    # Restaurar variables base originales
    n = 100

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ### Ejercicio 8
# 
# En la siguiente celda encuentras declarada una variable que almacena un número entero.

# In[179]:


# No modifiques esta celda

inicio = 10


# Utiliza un ciclo para almacenar en una lista, con nombre `cuenta_regresiva`, los números desde el valor de la variable `inicio` hasta el 1. La lista debe estar ordenada descendemente y en caso de que el inicio sea menor a 1 debes devolver una lista vacía.

# In[181]:


# YOUR CODE HERE
cuenta_regresiva= []

contador= inicio

while contador >= 1:
    cuenta_regresiva.append(contador)
    contador += -1

print(cuenta_regresiva)
    


#raise NotImplementedError()


# In[182]:


## PRUEBAS

#--------------
# INSTANCIA 1
#--------------

# Base variables
inicio = 20

try:
    # Caso 1: no existe la variable.
    try:
        cuenta_regresiva
    except:
        raise NotImplementedError("No declaraste una variable llamada cuenta_regresiva.",)
    
    # Caso 2: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
    
    # Caso 3: el código modifica los parametros del problema
    try:
        assert inicio == 20
    except:
        raise AssertionError("Tu código no debe modificar los datos del problema.")

    # Caso 4: no es una lista.
    assert type(cuenta_regresiva) == list, f"Tu variable cuenta_regresiva no es de tipo {list.__name__}."
    
    # Caso 5: el código no utiliza la variable inicio o no utiliza ciclos
    assert _i.find("inicio") >= 0, "Tu código no utiliza la variable inicio."
    assert _i.find("for") >= 0 or _i.find("while") >= 0, "Tu código no utiliza ciclos."

    # Caso 6: la lista contiene valores de tipo incorrecto
    for i in cuenta_regresiva:
        assert type(i) == int, f"Tu lista contiene valores que no son de tipo {int.__name__}."

    # Caso 7: la lista tiene el tamaño incorrecto
    assert len(cuenta_regresiva) == 20, "Tu lista no tiene el tamaño correcto."

    # Caso 8: la lista es correcta
    assert cuenta_regresiva == list(range(20, 0, -1)), "Tu implementación presenta errores cuando el valor de la variable inicio es mayor o igual a 1."
    
except:
    # Restaurar variables base originales
    inicio = 10
    raise

finally:
    # Restaurar variables base originales
    inicio = 10
    
#--------------
# INSTANCIA 2
#--------------

# Base variables
inicio = 0

try:
    # Caso 1: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")

    # Caso 2: no es una lista.
    assert type(cuenta_regresiva) == list, f"Tu variable cuenta_regresiva no es de tipo {list.__name__}."

    # Caso 3: la lista tiene el tamaño incorrecto
    assert len(cuenta_regresiva) == 0, "Tu implementación presenta errores cuando el valor de la variable inicio es menor a 1."

except:
    # Restaurar variables base originales
    inicio = 10
    raise
    
finally:
    # Restaurar variables base originales
    inicio = 10

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ### Ejercicio 9
# 
# En la siguiente celda encuentras declarada una lista y un elemento.

# In[334]:


# No modifiques esta celda

numeros = [1,2,8,4,6,7,10,45,67,89,100,12,34,2,1,5,34,36,28,27,43,182,13,124,122,158,835,38,46,38,28,38,34,67,89,58]
a_buscar = 89


# Busca el número entero `a_buscar` en la lista `numeros` y guarda el índice en una variable con nombre `indice`. En caso de que el elemento se encuentre más de una vez en la lista `numeros`, debes almacenar el índice de la primera posición en la que lo encuentres. Por otro lado, si el elemento no se encuentra en la lista `numeros`, almacena -1 en la variable `indice`.

# In[335]:


# YOUR CODE HERE

for i in range(len(numeros)):
    if a_buscar == numeros [i]:
        indice= numeros.index(a_buscar)
        break
    else:
        indice = -1
        
print(indice)


#raise NotImplementedError()


# In[336]:


## PRUEBAS

#--------------
# INSTANCIA 1
#--------------

# Base variables
a_buscar = 28

try:
    # Caso 1: no existe la variable.
    try:
        indice
    except:
        raise NotImplementedError("No declaraste una variable llamada indice.",)
        
    # Caso 2: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
    
    # Caso 3: el código modifica los parametros del problema
    try:
        assert a_buscar == 28
    except:
        raise AssertionError("Tu código no debe modificar los datos del problema.")
    
    # Caso 4: no es de tipo int.
    assert type(indice) == int, f"Tu variable mas_rapido no es de tipo {int.__name__}."

    # Caso 5: el código no utiliza las variables a_buscar y numeros
    assert _i.find("a_buscar") >= 0, "Tu código no utiliza la variable a_buscar."
    assert _i.find("numeros") >= 0, "Tu código no utiliza la variable numeros."

    # Caso 6: la respuesta es correcta
    assert indice == 18, "Tu implementación presenta errores cuando el valor de la variable a_buscar se encuentra al menos una vez en la lista numeros. Es posible que no hayas almacenado el índice asociado a la primera vez que aparece el valor de la variable a_buscar."
    
except:
    # Restaurar variables base originales
    a_buscar = 89
    raise
    
finally:
    # Restaurar variables base originales
    a_buscar = 89

#--------------
# INSTANCIA 2
#--------------

# Base variables
a_buscar = 3

try:
    
    # Caso 1: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
    
    # Caso 2: no es de tipo int.
    assert type(indice) == int, f"Tu variable mas_rapido no es de tipo {int.__name__}."

    # Caso 3: la respuesta es correcta
    assert indice == -1, "Tu implementación presenta errores cuando el valor de la variable a_buscar no se encuentra en la lista numeros."
        
except:
    # Restaurar variables base originales
    a_buscar = 89
    raise
    
finally:
    # Restaurar variables base originales
    a_buscar = 89

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ### Ejercicio 10
# 
# En la siguiente celda encuentras declarada una variable que almacena una cadena de caracteres.

# In[44]:


# No modifiques esta celda

cadena = "Me encanta programar, Python es mi pasión."


# Almacena en un diccionario, con nombre `num_vocales`, la cantidad veces que aparece cada vocal en la cadena de caracteres `cadena`. Las llaves del diccionario deben ser las vocales, y los valores deben ser el número de veces que aparece cada vocal.
# 
# **Nota:** no tengas en cuenta vocales en mayúscula, ni con tíldes, ni con diéresis. Por ejemplo, el diccionario asociado a la cadena "El pingüino lingüístico." es: `{'a': 0, 'e': 0, 'i': 4, 'o': 2, 'u': 0}`.

# In[51]:


# YOUR CODE HERE

a = cadena.lower().count('a')
e = cadena.lower().count('e')
i = cadena.lower().count('i')
o = cadena.lower().count('o')
u = cadena.lower().count('u')

values= [a,e,i,o,u]
keys=['a','e','i','o','u']

num_vocales = dict(zip(keys,values))

print(num_vocales)
type(num_vocales)

#raise NotImplementedError()


# In[52]:


## PRUEBAS

#--------------
# INSTANCIA 1
#--------------

# Base variables
cadena = "The world's most valuable resource is no longer oil, but data."

try:
    # Caso 1: no existe el diccionario.
    try:
        num_vocales
    except:
        raise NotImplementedError("No existe una variable llamada num_vocales.",)

    # Caso 2: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
    
    # Caso 3: el código modifica los parametros del problema
    try:
        assert cadena == "The world's most valuable resource is no longer oil, but data."
    except:
        raise AssertionError("Tu código no debe modificar los datos del problema.")

    # Caso 4: no es un diccionario.
    assert type(num_vocales) == dict, f"Tu variable num_vocales no es de tipo {dict.__name__}."

    # Caso 5: el código no utiliza la variable candena
    assert _i.find("cadena") >= 0, "Tu código no utilizala variable cadena."

    # Caso 6: el diccionario contiene valores de tipo incorrecto
    for i in num_vocales.keys():
        assert type(i) == str, f"Tu diccionario contiene llaves que no son de tipo {str.__name__}."

    for j in num_vocales.values():
        assert type(j) == int, f"Tu diccionario contiene valores que no son de tipo {int.__name__}."

    # Caso 7: el diccionario tiene el tamaño incorrecto
    assert len(num_vocales) == 5, "Tu diccionario no tiene el tamaño correcto."

    # Caso 8: el diccionario no contiene los valores/llaves correctos/as
    assert set(num_vocales.keys()) == {'a', 'e', 'i', 'o', 'u'}, "Las llaves de tu diccionario no son correctas."
    assert set(num_vocales.values()) == {4, 2, 3, 5, 6}, "Los valores de tu diccionario no son correctos."

    # Caso 9: el diccionario es correcto 
    try:
        assert num_vocales['a'] == 4
        assert num_vocales['e'] == 5
        assert num_vocales['i'] == 2
        assert num_vocales['o'] == 6
        assert num_vocales['u'] == 3
    except AssertionError as e:
        e.args += ("Tu respuesta es incorrecta.",)
        raise e      
    
except:
    # Restaurar variables base originales
    cadena = "Me encanta programar, Python es mi pasión."
    raise

finally:
    # Restaurar variables base originales
    cadena = "Me encanta programar, Python es mi pasión."
            
# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ### Ejercicio 11
# 
# Jorge tiene un refugio de perros y realizará un evento de adopción en los próximos días. En estos eventos, las  personas están interesadas en perros con cierto rango de edad. Por lo tanto, es de interés presentar únicamente los perros que se encuentren en ese rango; en la siguiente celda se almacena el límite inferior del rango en la variable `lb` y el límite superior del rango en la variable `ub`. El diccionario `perros_refugio`, presentado en la siguiente celda, contiene los perros que pertenecen al refugio, donde las llaves son los nombres de los perros y los valores sus respectivas edades.

# In[228]:


# No modifiques esta celda

lb = 2
ub = 5

perros_refugio = {
                  "Bruno": 5,
                  "Alex": 2,
                  "Fiona": 3,
                  "Salvador": 7,
                  "Max": 1,
                  "Copito": 5,
                  "Joe": 1,
                  "Maya": 2
                  }


# A partir de las variables declaradas en la celda anterior, crea una lista, con nombre `perros_evento`, que contenga los nombres de los animales que se encuentren dentro del rango de edad. 
# 
# **Nota:** los perros que tienen la edad especificada por los límites también deben ser incluidos en la lista `perros_evento`.

# In[234]:


# YOUR CODE HERE
perros_evento=[]

for i in perros_refugio:
    if perros_refugio[i] >= lb and perros_refugio[i] <= ub:
        perros_evento.append(i)
        
print(perros_evento)

#raise NotImplementedError()


# In[235]:


## PRUEBAS

#--------------
# INSTANCIA 1
#--------------

# Base variables
lb = 1
ub = 2

try:
    # Caso 1: no existe la variable.
    try:
        perros_evento
    except:
        raise NotImplementedError("No declaraste una variable llamada perros_evento.",)
    
    # Caso 2: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
    
    # Caso 3: el código modifica los parametros del problema
    try:
        assert lb == 1
        assert ub == 2
    except:
        raise AssertionError("Tu código no debe modificar los datos del problema.")
    
    # Caso 4: no es una lista.
    assert type(perros_evento) == list, f"Tu variable perros_evento no es de tipo {list.__name__}."
    
    # Caso 5: la lista contiene valores de tipo incorrecto
    for i in perros_evento:
        assert type(i) == str, f"Tu lista contiene valores que no son de tipo {str.__name__}."
    
    # Caso 6: el código no utiliza las variables lb, ub y perros_refugio
    assert _i.find("lb") >= 0, "Tu código no utiliza la variable lb."
    assert _i.find("ub") >= 0, "Tu código no utiliza la variable ub."
    assert _i.find("perros_refugio") >= 0, "Tu código no utiliza la variable perros_refugio."
    
    # Caso 7: la lista tiene el tamaño incorrecto
    assert len(perros_evento) == 4, "Tu lista no tiene el tamaño correcto. Es posible que tengas problemas utilizando los límites del rango."
        
    # Caso 8: el diccionario es correcto 
    assert set(perros_evento) == {'Alex', 'Maya', 'Joe', 'Max'}, "Tu respuesta es incorrecta."

except:
    # Restaurar variables base originales
    lb = 2
    ub = 5
    raise

finally:
    # Restaurar variables base originales
    lb = 2
    ub = 5

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ### Ejercicio 12
# 
# Se dice que uno de los primeros ejemplos de cifrado en la historia fue inventado por Julio César, quien necesitaba enviar instrucciones escritas a sus generales, pero tenía que evitar que sus enemigos se enteraran de sus planes en caso de que los mensajes cayeran en sus manos. Para esto, desarrolló lo que ahora se conoce como el Cifrado César basándose en una idea muy simple: se define un corrimiento `corr` y luego, cada letra dentro del mensaje original se remplaza por la letra que esté `corr` posiciones más adelante en el alfabeto. Por ejemplo, con un `corr` igual a 3, la A se convierte en D, la B en E, y así sucesivamente. Las últimas tres letras en el alfabeto se vuelven las tres primeras: X se vuelve A, Y se vuelve B y Z se vuelve C. Para simplificar el ejercicio, el cifrado únicamente afectará caracteres que correspondan a letras minúsculas sin tíldes ni diéresis.
# 
# En la siguiente celda encuentras la cadena de caracteres `cifrada` que contiene una frase para descifrar y se especifica el valor de la variable `corr`. Adicionalmente, encuentras una tupla con el alfabeto.  

# In[2]:


# No modifiques esta celda

cifrada = "Aqxzxobjmp nmo bi kmoqb x ixp 5 ab ix qxoab"
corr = 3

alfabeto = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')


# Obtén el mensaje descifrado y almacénalo en una variable llamada `descifrada`.

# In[5]:


# YOUR CODE HERE
def cifrado(letra,corrimiento, alfabeto):
    if letra == ' ':
        letrafinal = ' '
        return letrafinal
    else:
        for i in alfabeto:
            if i == letra:
                posicioninicial= alfabeto.index(i)
                if posicioninicial + corrimiento <= len(alfabeto)-1:
                    letrafinal = alfabeto[posicioninicial + corrimiento]
                    
                    return letrafinal
                
                elif posicioninicial + corrimiento > len(alfabeto)-1:
                    movimiento= posicioninicial + corrimiento - len(alfabeto)
                    letrafinal = alfabeto[movimiento]
                    
                    return letrafinal
                
# Function to convert lists into strings
def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 

######------------------Corremos la funcion en un ciclo----------------------######

descifrada=[]           
for i in cifrada:
    if i not in alfabeto:
        descifrada.append(i)
    else:
        letra = cifrado(i,corr,alfabeto)
        descifrada.append(letra)
        

        
descifrada = listToString(descifrada)

print(descifrada)
        
#raise NotImplementedError()


# In[6]:


## PRUEBAS

#--------------
# INSTANCIA 1
#--------------

# Base variables
cifrada = "Eg ikhwnz yzg zñlív zñ Pvwgk"
corr = 5

try:
    # Caso 1: no existe la variable.
    try:
        descifrada
    except:
        raise NotImplementedError("No declaraste una variable llamada descifrada.",)
    
    # Caso 2: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
    
    # Caso 3: el código modifica los parametros del problema
    try:
        assert cifrada == "Eg ikhwnz yzg zñlív zñ Pvwgk"
        assert corr == 5
    except:
        raise AssertionError("Tu código no debe modificar los datos del problema.")
    
    # Caso 4: no es de tipo str.
    assert type(descifrada) == str, f"Tu variable descifrada no es de tipo {str.__name__}."

    # Caso 5: el código no utiliza las variables cifrada y corr
    assert _i.find("cifrada") >= 0, "Tu código no utiliza la variable cifrada."
    assert _i.find("corr") >= 0, "Tu código no utiliza la variable corr."

    # Caso 6: la respuesta es correcta
    assert descifrada == 'El nombre del espía es Pablo', "Tu respuesta es incorrecta."
    
except:
    # Restaurar variables base originales
    cifrada = "Aqxzxobjmp nmo bi kmoqb x ixp 5 ab ix qxoab"
    corr = 3
    raise
    
finally:
    # Restaurar variables base originales
    cifrada = "Aqxzxobjmp nmo bi kmoqb x ixp 5 ab ix qxoab"
    corr = 3

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ### Ejercicio 13
# 
# Santiago ha pedido un catálogo de artículos con el fin de escoger un regalo de cumpleaños para su amiga Mariana. A Santiago se le olvido guardar dinero para el regalo y por consiguiente necesita escoger el artículo más barato disponible. El diccionario `catalogo` presentado en la siguiente celda tiene varias llaves que corresponden al nombre de los artículos. El valor asociado a cada llave es el precio del artículo (en COP).

# In[9]:


# No modifiques esta celda

catalogo = {
            "Oso de peluche" : 50000,
            "Perfume" : 9800,
            "Aretes" : 5000,
            "Dulces" : 5000,
            "Blusa" : 15000,
            "Bono de peluqueria" : 10000,
            "Libros" : 60000
            }


# Almacena el nombre del artículo más barato en una variable llamada `regalo`. Si Santiago encuentra un empate entre dos o más artículos, escribirá sus nombres en orden alfabético y eligirá el primero. Asimismo, si el artículo más barato vale más de COP 10000, Santiago no comprará nada y le escribirá una carta a su amiga. Si este es el caso, deberás almacenar la cadena de caracteres `"Carta"` en la variable `regalo`.

# In[41]:


# YOUR CODE HERE
# list out keys and values separately

key_list = list(catalogo.keys())
val_list = list(catalogo.values())
regalomin=min(val_list)

listacomparable=[]
for i in key_list:
    if regalomin == catalogo[i]:
        listacomparable.append(i)

listacomparable= sorted(listacomparable)

if regalomin > 10000:
    regalo = 'Carta'
else:
    regalo = listacomparable[0]
    
print(regalo)
    
#raise NotImplementedError()


# In[42]:


## PRUEBAS

#--------------
# INSTANCIA 1
#--------------

# Base variables
catalogo = {"Peluche" : 5000, "Perfume" : 9800, "Cadena" : 20000, "Chocolates" : 5000, 
            "Zapatos" : 100000, "Flores" : 10000, "Libro" : 10000}

try:
    # Caso 1: no existe la variable.
    try:
        regalo
    except:
        raise NotImplementedError("No declaraste una variable llamada regalo.",)
        
    # Caso 2: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
    
    # Caso 3: el código modifica los parametros del problema
    try:
        assert catalogo == {"Peluche" : 5000, "Perfume" : 9800, "Cadena" : 20000, "Chocolates" : 5000, "Zapatos" : 100000, "Flores" : 10000, "Libro" : 10000}
    except:
        raise AssertionError("Tu código no debe modificar los datos del problema.")
    
    # Caso 4: no es de tipo str.
    assert type(regalo) == str, f"Tu variable regalo no es de tipo {str.__name__}."

    # Caso 5: el código no utiliza la variable catalogo 
    assert _i.find("catalogo") >= 0, "Tu código no utiliza la variable catalogo."

    # Caso 6: la respuesta es correcta
    assert regalo == 'Chocolates', "Tu implementación presenta errores cuando el artículo más barato tiene un valor menor o igual a COP 10000. Es posible que no hayas manejado correctamente la regla de desempate."
        
except:
    # Restaurar variables base originales
    catalogo = {"Oso de peluche" : 50000, "Perfume" : 9800,"Aretes" : 5000, "Dulces" : 5000,
                "Blusa" : 15000, "Bono de peluqueria" : 10000, "Libros" : 60000}
    raise

finally:
    # Restaurar variables base originales
    catalogo = {"Oso de peluche" : 50000, "Perfume" : 9800,"Aretes" : 5000, "Dulces" : 5000,
                "Blusa" : 15000, "Bono de peluqueria" : 10000, "Libros" : 60000}

#--------------
# INSTANCIA 2
#--------------

# Base variables
catalogo = {"Peluche" : 50000, "Perfume" : 98000, "Cadena" : 200000, "Chocolates" : 50000, 
            "Zapatos" : 1000000, "Flores" : 100000, "Libro" : 100000}
try:
    
    # Caso 1: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
    
    # Caso 2: no es de tipo str.
    assert type(regalo) == str, f"Tu variable regalo no es de tipo {str.__name__}."

    # Caso 3: la respuesta es correcta
    assert regalo == 'Carta', "Tu implementación presenta errores cuando el artículo más barato vale más de COP 10000."
        
except:
    # Restaurar variables base originales
    catalogo = {"Oso de peluche" : 50000, "Perfume" : 9800,"Aretes" : 5000, "Dulces" : 5000,
                "Blusa" : 15000, "Bono de peluqueria" : 10000, "Libros" : 60000}
    raise

finally:
    # Restaurar variables base originales
    catalogo = {"Oso de peluche" : 50000, "Perfume" : 9800,"Aretes" : 5000, "Dulces" : 5000,
                "Blusa" : 15000, "Bono de peluqueria" : 10000, "Libros" : 60000}

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ## Referencias
# 
# Senecode. (2019). Problemas. 25 Noviembre 2020, de Uniandes Sitio web: https://senecode.virtual.uniandes.edu.co/problemas/buscar
# 
# BootCamp Uniandes. (2016). Notas de clase. 25 Noviembre 2020, de GitHub Sitio web: https://github.com/PythonBootcampUniandes/notas-de-clase

# ## Créditos
# 
# __Autor(es)__: Camilo Falla Moreno, Juan Felipe Rengifo Méndez, Ariadna Sofía de Ávila Bula, Alejandro Mantilla Redondo, Diego Alejandro Cely Gómez
# 
# __Fecha última actualización:__ 06/08/2021
