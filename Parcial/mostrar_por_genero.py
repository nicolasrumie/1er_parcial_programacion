import json
generos = []
lista_generos = ["Acción", "Aventura", "Animación", "Biográfico", "Comedia", "Comedia romántica",
        "Comedia dramática", "Crimen", "Documental", "Drama", "Fantasía", "Histórico",
        "Infantil", "Musical", "Misterio", "Policíaco", "Romance", "Ciencia ficción",
        "Suspenso", "Terror", "Western", "Bélico", "Deportivo", "Noir", "Experimental",
        "Familiar", "Superhéroes", "Espionaje", "Artes marciales", "Fantástico", "Catástrofe",
        "Melodrama", "Erótico", "Cine independiente", "Zombies", "Vampiros", "Cyberpunk",
        "Steampunk", "Distopía", "Utopía", "Road Movie", "Docuficción", "Mockumentary",
        "Gótico", "Slasher", "Adolescente", "Culto", "Maravilloso"]

def mostrar_peliculas_por_genero(lista_peliculas_importadas:list[dict]) -> None:
    global generos
    lista_peliculas_mismo_genero = []
    lista_peliculas_mismo_genero_aux = []
    generos = []
    count = 0

    for genero in lista_generos:
        lista_peliculas_mismo_genero_aux = []
        for pelicula in lista_peliculas_importadas:
            if pelicula['genero'] == genero:
                lista_peliculas_mismo_genero_aux.append(pelicula['titulo'])
                count += 1
            if count == 1:
                count += 1
                generos.append(genero)
        count = 0
        if len(lista_peliculas_mismo_genero_aux) > 0:
            lista_peliculas_mismo_genero.append(lista_peliculas_mismo_genero_aux)
    
    crear_json("Parcial/json_peliculas.json", genero, generos, lista_peliculas_mismo_genero)


def crear_json(path:str, genero:str, generos:list[str] , lista_peliculas_mismo_genero:list[str]) -> None:
    formato = dict()
    contador = 0
    for genero in generos:
        for i in range(len(lista_peliculas_mismo_genero)):
            i = contador
            formato[genero] = lista_peliculas_mismo_genero[i]
            contador += 1
            break

    archivo = open(path, 'w')
    json.dump(formato, archivo, indent=8, ensure_ascii=False)
    archivo.close()

