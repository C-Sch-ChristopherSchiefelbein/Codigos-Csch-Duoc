print("\n******************************\nBienvenido a la app!!\n-Toma de pedidos(Rolls)\n")
print("Se desplegaran las opciones\nUna vez las selecciones, puedes seleccionar mas, como un carrito!\n")
total_pedido = 0#total precio pedidos
Cant_articulos = 0#cuenta la cantidad de articulos total
verificar = 0#da el estado del descuento a la funcion
rolls=[0,0,0,0]#lista para verificar cant de rolls

def boleta(verificar): #boleta a imprimir 
    print(f"\n******************************\nTOTAL PRODUCTOS: {Cant_articulos}\n******************************\n")
    print(f"Pikachu Roll: {rolls[0]}\nOtaku Roll: {rolls[1]}\nPulpo Venenoso Roll: {rolls[2]}\nAnguila Eléctrica Roll: {rolls[3]}\n******************************\n")
    print(f"Subtotal por pagar: {total_pedido}\n")
    if verificar == 1:
        descuento = total_pedido* 10 / 100
        print(f"Descuento por código: {descuento}\n")
        print(f"TOTAL a pagar: {total_pedido-descuento}")
    else:
        print(f"TOTAL a pagar: {total_pedido}")
def llevas():#va indicando que lleva
    print(f"******************************\nLlevas:\n1-Pikachu Roll: {rolls[0]}\n2-Otaku Roll: {rolls[1]}\nPulpo Venenoso Roll: {rolls[2]}\nAnguila Eléctrica Roll: {rolls[3]}\n******************************\n")

while True:#menu, bucle hasta break
    print("******************************\nOpciones:\n\n1-Pikachu Roll $4500\n2-Otaku Roll $5000\n3-Pulpo Venenoso Roll $5200\n4-Anguila Eléctrica Roll $4800")
    print("5-Terminar pedido/salir")
    eleccion = int(input("\nSelecciona un pedido\nSe añadirá al carrito (1-5): "))#ELECCION MENU
    #opciones segun eleccion ingresada
    if eleccion == 5:
        print("Tienes un código de descuento? (si/no)")
        desc_tiene = input("si / no: ").lower()
        if desc_tiene == "no":
            boleta(verificar=0)
            break
        elif desc_tiene == "si":
            codigo = input("Ingresa el codigo: ")
            if codigo == "soyotaku":
                boleta(verificar=1)
                print("\nHasta Pronto!")
                break
            else:
                print("Codigo erroneo")
                boleta(verificar=0)
                print("\nHasta Pronto!")
                break
    elif eleccion == 1:
        total_pedido += 4500
        Cant_articulos += 1
        rolls[0]+=1#suma 1 a la cantidad, en la lista
        print("\n******************************\nSe añadio la opcion 1 al carrito\n")
        llevas()
    elif eleccion == 2:
        total_pedido += 5000
        Cant_articulos += 1
        rolls[1]+=1
        print("\n******************************\nSe añadio la opcion 2 al carrito\n")
        llevas()
    elif eleccion == 3:
        total_pedido += 5200
        Cant_articulos += 1
        rolls[2]+=1
        print("\n******************************\nSe añadio la opcion 3 al carrito\n")
        llevas()
    elif eleccion == 4:
        total_pedido += 4800
        Cant_articulos += 1
        rolls[3]+=1
        print("\n******************************\nSe añadio la opcion 4 al carrito\n")
        llevas()
    else:
        print("Opción incorrecta")
        llevas()
    
    




