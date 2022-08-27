observador=100

print("**MENU**")
print("0.SALIR")
print("1.Saludar")
print("2.Despedir")
while(observador != 0):

    observador=int(input("Digite una opcion: "))

    if(observador==0):
        break
    elif(observador==1):
        print("hola")
    elif(observador==2):
        print("chao")
    else:
        print("Digite una opción valida")
    
