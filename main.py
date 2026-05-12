import os
os.system("cls")
flag = True
#contadores
contador_ahorro = 0
contador_deposito = 0
contador_cantidad_depositos = 0


try:
    while flag:
        print("====Banco Financiero====")
        print("1.Mostrar cuotas ahorro")
        print("2.Sumular depósito acumulado")
        print("3.Tabla de crédito")
        print("4.Contar clientes atendidos")
        print("5.Salir")
        menu = int(input("Ingrese opcion:\n"))
        while menu >= 6 or menu <= 0:
            print("La opcion ingresada no es valida.")
            print("====Banco Financiero====")
            print("1.Mostrar cuotas ahorro")
            print("2.Sumular depósito acumulado")
            print("3.Tabla de crédito")
            print("4.Contar clientes atendidos")
            print("5.Salir")
            menu = int(input("Ingrese opcion:\n"))
        if menu == 1:
            mes = int(input("Ingrese cantidad de meses:\n"))
            ahorro = int(input("Ingrese cuanto va a ahorrar:\n"))
            for x in range(1,mes+1):
                contador_ahorro = contador_ahorro + ahorro
                print(f"Mes {x}: {contador_ahorro}")
                
        elif menu == 2:
            flag2 = True
            while flag2:
                deposito = int(input("Ingrese deposito:\n"))
                if deposito > 0:
                    contador_deposito = contador_deposito + deposito
                    contador_cantidad_depositos = contador_cantidad_depositos + 1
                    print(f"Cantidad depositada:${contador_deposito}")
                    print(f"Cantidad de depósitos: {contador_cantidad_depositos}")
                else:
                    print("Depositado.")
                    flag2 = False
            
        elif menu == 3:
            multi = int(input("Ingrese un monto de credito:\n"))
            while multi <= 0:
                multi = int(input("El valor ingresado no es valido.\nIngrese un monto de credito:\n"))
            for x in range(1,13):
                multiplicacion = multi * x
                print(f"{multi} x {x} = {multiplicacion}")
            
        elif menu == 4:
            clientes = int(input("Ingrese cantidad de clientes:\n"))
            while clientes <= 0:
                clientes = int(input("La cantidad ingresada no es valida.\nIngrese cantidad de clientes:\n"))
            for x in range(1,clientes +1):
                print(f"Clientes atendido N°{x}")
            
        elif menu == 5:
            print("Gracias por utilizar el sistema financiero.")
            flag = False
except:
    print("No es valido")





