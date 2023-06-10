# Scope, alcance o ambito

# Ambito local: Si una variable se define dentro de una funcion
def funcion():
    variable_local = "Soy una variable local"
    print(variable_local)
funcion()

# Ambito de cierre: se usa cuando tenemos una funcion dentro de otra funcion
def funcion_externa():
    variable_cierre = "Soy una variable de cierre"
    def funcion_interna():
        print(variable_cierre)
    
    funcion_interna()
funcion_externa()

# Ambito global: es usada por todo el archivo de python
variable_global = "Soy una variable global"
def funcion1():
    print(variable_global)
funcion1()
print(variable_global)

# Ambito incorporado: no es necesario declarar nada, son funciones que ya estan dentro de python
print(len([1, 2, 3, 4, 0]))