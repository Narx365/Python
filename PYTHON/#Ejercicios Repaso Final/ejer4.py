class Producto:
    def __init__(self, id, nombre, precio, stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

inventario= []
opcion= ""


while opcion != 0:
    print ("1) Añadir producto")
    print ("2) Eliminar productor por id")
    print ("3) Actualizar stock")
    print ("4) Mostrar inventario")
    print ("5) Calcular valor total del inventario")
    print ("6) Salir")

    opcion= input ("Diganos que acción quiere realizar: ")
    if opcion == "1":
        id= input("Digame el ID del producto: ")
        repetido= False

        for i in inventario:
            if i.id == id:
                repetido= True
        
        if repetido:
            print("ID repetido, no se introducirá nada")
        else:
            nombre= input("mete tu nombre: ")
            precio = float(input("Precio: "))
            stock = int(input("Stock: "))
            inventario.append(Producto(id, nombre, precio, stock))

    elif opcion == "2":
        id= input("dígame el ID que quiere eliminar: ")
        encontrado= False
        
        for i in inventario:
            if i.id == id:
                inventario.remove(i)
                encontrado= True
        
        if encontrado:
            print ("producto eliminado, hemos encontrado su ID")
        else:
            print ("producto no eliminado, no hemos encontrado su ID")

    elif opcion == "3":
        id= input("dígame el ID que quiere actualizar: ")
        encontrado= False
        
        for i in inventario:
            if i.id == id:
                n_stock= int(input("Mete el nuevo id: "))
                i.stock= n_stock
                encontrado= True
        
        if encontrado:
            print ("Hemos cambiado el ID del producto elegido")
        else:
            print ("No hemos podido cambiadr el ID, no hemos encontrado ese ID")

    elif opcion == "4":
        if len(inventario)== 0:
            print ("Inventario VACIO")
        else:
            for i in inventario:
                print ("Nombre:" , nombre , "id:" , id , "stock" , stock , "precio" , precio)
    
    elif opcion == 0:
        print ("Saliendo del programa")
    
    else:
        print ("Opción inválida")