import re

def guardar_csv(path:str, lista_peliculas:list[dict]) -> None:

    linea =""
    for i in range(len(lista_peliculas)):
        linea += f"{lista_peliculas[i]['id']},{lista_peliculas[i]['titulo']},{lista_peliculas[i]['genero']},{lista_peliculas[i]['anio_lanzamiento']},{lista_peliculas[i]['duracion']},{lista_peliculas[i]['apto_para_todo_publico']},{lista_peliculas[i]['plataformas']}\n"

    with open(path, "w", encoding="utf8") as archivo:
        archivo.write(linea)

def importar_peliculas_csv(path: str) -> list[dict]:
    lista_peliculas = []

    with open(path, "r", encoding='utf8') as archivo:
        for linea in archivo:
            datos = re.split(",|\n", linea)

            diccionario = {}
            diccionario["id"] = datos[0]
            diccionario["titulo"] = datos[1]
            diccionario["genero"] = datos[2]
            diccionario["anio_lanzamiento"] = datos[3]
            diccionario["duracion"] = datos[4]
            diccionario["apto_para_todo_publico"] = datos[5]
            diccionario["plataformas"] = datos[6]
            lista_peliculas.append(diccionario)
            if len(lista_peliculas) > 1:
                for pelicula in range(len(lista_peliculas) - 1):
                        if diccionario["titulo"] == lista_peliculas[pelicula]["titulo"]:
                            lista_peliculas.pop()
                            break
                        

    return lista_peliculas