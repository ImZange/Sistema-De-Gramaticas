import re
from Menu import menuPrincipal
#global archivo
#global no_terminales
#global terminales
#global producciones
reglas = {}

def selArchivo():
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()
    archivo = filedialog.askopenfilename(title="Selecciona un archivo")
    return archivo

def iniciarPrograma():
    menuPrincipal()
    elect = input(f"Ingresa la opción a realizar: ")
    match elect:
        case "1":
            menuGramatica()
        case "2":
            return
        case "3":
            return
        case "4":
            return
        case _:
            print("Opción incorrecta")

def leerArchivo():
    archivo = selArchivo()
    with open(archivo, 'r') as f:
        contenido = f.read()
    
    no_terminales = re.search(r'N\{(.*?)\}', contenido)
    terminales = re.search(r'T\{(.*?)\}', contenido)
    producciones = re.search(r'P\{(.*?)\}', contenido, re.DOTALL)
    if no_terminales:
        no_terminales = no_terminales.group(1).split(',')
    else:
        print("No hay elementos no_terminales en el archiv")
    if terminales:
        terminales = terminales.group(1).split(',')
    else:
        print("No hay terminales en el archivo")

    reglas = {}

    if producciones:
        for linea in producciones.group(1).split(','):
            linea = linea.strip()
            if linea:
                lado_izq, lado_der = linea.split('>')
                lado_izq = lado_izq.strip()
                lado_der = [p.strip() for p in lado_der.split('|')]
                if lado_izq in reglas:
                    reglas[lado_izq].extend(lado_der)  
                else:
                    reglas[lado_izq] = lado_der
    return no_terminales, terminales, reglas

def mostrarGramatica():
    no_terminales, terminales, reglas = leerArchivo()
    print("No terminales:", no_terminales)
    print("Terminales:", terminales)
    print("Producciones:")

    for L, P in reglas.items():
        print(f"  {L} -> {' | '.join(P) }")

def menuGramatica():
    print(""" Submenú Gramáticas 
        - 1.- Cargar Gramatica 
        - 2.- Conteo de Reglas Recursivas 
        - 3.- Generar cadena 
        - 4.- Salir 
    """)
    opcion = input("¿Qué operación realizarás?  ")
    match opcion:
        case "1":
            leerArchivo()
            mostrarGramatica()
            print("\nGramatica cargada con exito /ᐠ - ˕ -マ")
        case "2":
            leerArchivo()
            conteoReglasR()
        case _:
            return

def conteoReglasR():
    cont_Recursiones = 0
    no_terminales, terminales, reglas = leerArchivo()  # Obtener las reglas
    
    for L, P in reglas.items(): 
        print(L)
        print(P)
        if any(L in produccion for produccion in P):
            cont_Recursiones += 1
    print(f"El total de reglas recursivas es: {cont_Recursiones}")
    return cont_Recursiones
iniciarPrograma()

#recurrencia: cuantas reglas recursivas
#generación de cadenas: aleartoria cargando la gramatica y sus reglas


