from sub_menu_mostrar_peliculas import *
from sub_menu_calcular_promedio import *
from sub_menu_calcular_porcentaje import *
from sub_menu_dar_de_alta import *
from sub_menu_eliminar_pelicula import *
from sub_menu_buscar_pelicula import *
from sub_menu_ordenar_peliculas import *
from funcion_guardar_csv import *
from mostrar_por_genero import *
from sub_menu_modificar_pelicula import *

lista_peliculas_importadas = importar_peliculas_csv("Parcial/peliculas.csv")

while True:
    print("""
        1_ Dar de alta.
        2_ Modificar película.
        3_ Eliminar película.
        4_ Mostrar películas.
        5_ Ordenar películas.
        6_ Buscar película (título).
        7_ Calcular promedio (año o duración).
        8_Calcular porcentaje (género o ATP).
        9_ Salir. 
        10_ Mostrar cantidad por genero. """)
    
    eleccion = input("Ingrese opción a elegir: ")
    
    
    match eleccion:
        case "1":
            menu_dar_de_alta(lista_peliculas_importadas)
        case "2":
            titulo = input("Ingrese titulo a modificar: ")
            menu_modificar_pelicula(buscar_pelicula(lista_peliculas_importadas, titulo))
        case "3":
            titulo = input("Ingrese pelicula que desee eliminar: ")
            eliminar_pelicula(lista_peliculas_importadas, titulo)
        case "4":
            menu_mostrar_peliculas(lista_peliculas_importadas)          
        case "5":
            menu_ordenar_pelicula(lista_peliculas_importadas)
        case "6":
            titulo = input("Ingrese pelicula que desea buscar: ")
            buscar_pelicula_por_titulo(lista_peliculas_importadas, titulo)
        case "7":
            menu_calcular_promedio(lista_peliculas_importadas)
        case "8":
            menu_calcular_porcentaje(lista_peliculas_importadas)
        case "9":
            guardar_csv("Parcial/peliculas.csv", lista_peliculas_importadas)
            print("¡Gracias por usar nuestro programa!")
            break
        case "10":
            mostrar_peliculas_por_genero(lista_peliculas_importadas)
        case _:
            print("Eleccion incorreta. (1-8) sino 9 para salir.")

