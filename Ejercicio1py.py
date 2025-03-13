
usuario = {"Nombre": "Juan", "Edad": 22,
           "Ciudad": "Bogotá"}  # Información básica

amigos = [{"Nombre": "Manuel", "Tiempo de amistad": "4 años"},
          {"Nombre": "Pedro", "Tiempo de amistad": "5 años"},
          {"Nombre": "Luis", "Tiempo de amistad": "2 años"},
          {"Nombre": "Daniela", "Tiempo de amistad": "1 año"}]

posts = {"Publicación 1":
         {"Contenido": "Foto en la playa", "Likes": 100, "Comentarios": [
             {"Aleja": "Exelente vista", "David": "Me encanta esa playa"}]},
         "Publicación 2":
         {"Contenido": "Foto en la montaña", "Likes": 4,
             "Comentarios": [{"Juan": "No me gusto la foto"}]}
         }

# Mostrar datos actuales
print("Usuario:", usuario)
print("\nAmigos:", amigos)
print("\nPosts:", posts)
print()

# Se agg un nuevo post al perfil
posts["Publicación 3"] = {
    "Contenido": "Foto familiar", "Likes": 39, "Comentarios": [{"Tatiana": "❤️"}]}

# Se modifica la ciudad
usuario["Ciudad"] = "Madrid"

# Se elimina el segundo amigo de la lista
amigos.pop(1)

print("Usuario actualizado:", usuario)

print("\nAmigos actualizados")
for amigo in amigos:
    print(
        f"Nombre: {amigo['Nombre']} \nTiempo de amistad: {amigo['Tiempo de amistad']}")

print("\nPosts actualizados:")
for post, detalles in posts.items():
    print(f"{post}: \nDetalles: {detalles['Contenido']}")
    print(f"Likes: {detalles['Likes']}")
    print("Comentarios:")
    for comentario in detalles['Comentarios']:
        for usuario, comentario_texto in comentario.items():
            print(f"{usuario}: {comentario_texto}")
    print()
