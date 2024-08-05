# Se tienen los siguientes diccionarios:
# PROGRAMA PRINCIPAL
Productos = {1:'Pantalones', 2:'Camisas', 3:'Corbatas', 4:'Casacas'}
Precios = {1:200.00, 2:120.00, 3:50.00, 4:350.00}
Stock = {1:50, 2:45, 3:30, 4:15}

# Elaborar un programa que muestre los diccionarios, y programar las siguientes acciones:
# [1] Agregar
# [2] Eliminar
# [3] Actualizar
# [4] Salir
def add_product():
    print('Agregar Producto')
    id = int(input('Ingrese ID: '))
    if id in Productos.keys():
        print('El ID ya existe')
        return
    name = input('Ingrese nombre del producto: ')
    try:
        price = float(input('Ingrese precio: '))
        if price <= 0 :
            print("Precio debe ser positivo")
    except ValueError as e:
        print("Precio debe ser entero o decimal")

    try:
        stock = int(input('Ingrese stock: '))
        if stock <= 0 :
            print("Stock debe ser positivo")
    except ValueError as e:
        print("Stock debe ser entero")
    Productos[id] = name
    Precios[id] = price
    Stock[id] = stock
    print('Producto agregado')


def delete_product ():
    print('Eliminar Producto')
    try:
        id = int(input('Ingrese ID: '))
    except ValueError as e:
        print("ID debe ser entero")
        return
    valueProduct = Productos.get(id)
    if  valueProduct is None :
        print('El ID no existe')
        return
    del Productos[id]
    del Precios[id]
    del Stock[id]

def update_product():
    print('Actualizar Producto')
    try:
        id = int(input('Ingrese ID: '))
    except ValueError as e:
        print("ID debe ser entero")
        return
    valueProduct = Productos.get(id)
    if  valueProduct is None :
        print("No se encuentra producto.")
        return
    name = input('Ingrese nuevo nombre del producto: ')
    try:
        price = float(input('Ingrese nuevo precio: '))
        if price <= 0 :
            print("Precio debe ser positivo")
    except ValueError as e:
        print("Precio debe ser entero o decimal")
        return

    try:
        stock = int(input('Ingrese nuevo stock: '))
        if stock < 0 :
            print("Stock debe ser mayor igual a cero")
    except ValueError as e:
        print("Stock debe ser entero")
        return
    Productos[id]  = name
    Precios[id]  = price
    Stock[id]  = stock

    print('Producto actualizado')

def show_products():
    print('Mostrando productos')
    line = '='*48
    print(f"{line}\nLista de Productos:\n{line}\n")
    for id, name in Productos.items():
        print('{:<5d} {:10s} {:20.2f} {:10d}'.format(id,name,Precios[id],Stock[id]))
    print(f"{line}")
    print("[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir \n Elija opción:")

def main():
    print('Bienvenido')
    option = 1
    while option!= '4':
        show_products()
        option = input()
        match option:
            case '1': add_product()
            case '2': delete_product()
            case '3': update_product()

main()