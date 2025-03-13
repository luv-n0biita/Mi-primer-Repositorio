from entities import Item,Usuario
from utils import pretty_print
import os.path

def cargar_items() ->list:
    lista_productos = []
    ruta = os.path.dirname(__file__) + "/utils/items.dcc"
    with open(ruta , "r") as data:
        for linea in data:
            item = linea.strip().split(",")
            instancia = Item(item[0],int(item[1]),int(item[2]))

            lista_productos.append(instancia)
            
    return lista_productos



def crear_usuario(tiene_suscripcion: bool) -> Usuario:
    
    instancia = Usuario(tiene_suscripcion) #instancia Creadd
        
    pretty_print.print_usuario(instancia)
    
    return instancia


if __name__ == "__main__":
    
    usuario = crear_usuario(False) #instancia
    items = cargar_items()
    pretty_print.print_items(items)
    
    for item in items:
        usuario.agregar_item(item)
        
    pretty_print.print_canasta(usuario)
    usuario.comprar()
    pretty_print.print_usuario(usuario)
    
        
    
        
    
    