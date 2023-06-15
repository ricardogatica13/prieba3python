from funciones import *

menu = True
while menu: 
    print('1 agregar afiliado')
    print('2 buscar afiliado')
    print('3 listar afiliad@s solter@s ')
    print('4 salir')
    opcion = int(input('ingrese una opción\n'))
    if opcion > 0 and opcion < 5:
        if opcion == 1:
            print("Agregar Afiliado")
            agregarAfiliado()            
        elif opcion == 2:
            print("Buscar Afiliado")
            buscarAfiliado()
        elif opcion == 3:
            print("Listar")
            listarSolteros()
        elif opcion == 4:
            op = int(input("esta seguro que desea salir?\n 1. SI\n 2.NO\n"))
            if op == 1:
                menu = False
                
