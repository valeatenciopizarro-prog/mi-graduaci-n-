import peliculas as info1
import series as info2
import juegos as info3
import records as info4
import unicodedata

# Normalizar texto para comparaciones
def normalizar(texto):
    return unicodedata.normalize("NFKD", texto.lower()).encode("ascii", "ignore").decode("ascii")

datos_peliculas = {
    # Drama
    "Simón, el gato testarudo": (info1.Simón, "Simón.png"),
    "Un gato callejero llamado Bob": (info1.Bob, "Bob.png"),
    "Las crónicas del gato viajero": (info1.Viajero, "Viajero.png"),
    "Mi Navidad con Bob": (info1.Bob2, "Bob2.png"),
    "La Vida Electrizante de Louis Wain": (info1.Electrizante, "Electrizante.png"),
    "La casa de Neko Atsume": (info1.Neko, "Neko.png"),

    # Terror
    "Los ojos del gato": (info1.Ojos, "Ojos.png"),
    "El gato": (info1.El, "El.png"),
    "Sonámbulos": (info1.Sonámbulos, "Sonambulos.png"),
    "Cementerio de Animales": (info1.Cementerio, "Cementerio.png"),
    "El gato negro": (info1.Gato, "Gato.png"),
    "Hausu": (info1.Hausu, "Hausu.png"),

    # Comedia
    "Rent a Cat": (info1.Rent, "Rent.png"),
    "El gato que vino del espacio": (info1.Espacio, "Espacio.png"),
    "Un gato del FBI": (info1.FBI, "FBI.png"),
    "Como perros y gatos": (info1.PG, "PG.png"),
    "Keanu": (info1.Keanu, "Keanu.png"),
    "Mi papá es un gato": (info1.Papá, "Papa.png"),

    # Animación
    "Flow": (info1.Flow, "Flow.png"),
    "Los aristogatos": (info1.Aristogatos, "Aristogatos.png"),
    "El gato con botas: El último deseo": (info1.Deseo, "Deseo.png"),
    "Las aventuras de Maurice": (info1.Maurice, "Maurice.png"),
    "Oliver y su pandilla": (info1.Oliver, "Oliver.png"),

    # Anime
    "Haru en el reino de los gatos": (info1.Reino, "Reino.png"),
    "Amor de gata": (info1.Amor, "Amor.png"),
    "Anzu, gato fantasma": (info1.Anzu, "Anzu.png"),
    "Rudolf, el gato negro": (info1.Rudolf, "Rudolf.png"),
    "La noche del ferrocarril galáctico": (info1.Ferrocarril, "Ferrocarril.png"),
    "Sopa de gato": (info1.Sopa, "Sopa.png"),

    # Documentales
    "En la mente de un gato": (info1.Mente, "Mente.png"),
    "Kedi: Gatos de Estambul": (info1.Kedi, "Kedi.png"),
    "Gatos: Una oda al amor gatuno": (info1.Gatos, "Gatos.png")
}

datos_juegos = {
    #Aventuras
    "Stray": (info3.Stray, "Stray.png"),
    "Little Kitty, Big City": (info3.City, "City.png"),
    "Gato Roboto": (info3.Roboto, "Roboto.png"),
    "Cat Quest": (info3.Quest, "Quest.png"),
    "Cat Quest II": (info3.Quest2, "Quest2.png"),
    "Cat Quest III": (info3.Quest3, "Quest3.png"),
    "Stars in the Trash": (info3.Stars, "Stars.png"),

    # Terror
    "Still It Runs": (info3.Runs, "Runs.png"),
    "The Cat in Yellow": (info3.Yellow, "Yellow.png"),
    "Cat Fred Evil Pet": (info3.Evil, "Evil.png"),
    "Cartoon Cat Horror Game": (info3.Cartoon, "Cartoon.png"),

    #Infantil
    "Super Cat Tales": (info3.Super, "Super.png"),
    "Super Cat Tales 2": (info3.Super2, "Super2.png"),
    "Cat Goes Fishing": (info3.Fishing, "Fishing.png"),
    "KleptoCats": (info3.KleptoCats, "KleptoCats.png"),

}

datos_series = {
    # Drama
    "Neko Zamurai": (info2.Zamurai, "Zamurai.png"),
    "Mi compañero de cuarto es un gato": (info2.Cuarto, "Cuarto.png"),
    "Ella y su gato: Todo fluye": (info2.Fluye, "Fluye.png"),

    # Terror
    "La noche de los gatos vivientes": (info2.Noche, "Noche.png"),
    "El mundo oculto de Sabrina": (info2.Oculto, "Oculto.png"),

    # Comedia
    "Sabrina, la bruja adolescente": (info2.Adolescente, "Adolescente.png"),
    "Gatitos explosivos": (info2.Explosivos, "Explosivos.png"),
    "Gatos callejeros": (info2.Callejeros, "Callejeros.png"),
    "El dulce hogar de Chi": (info2.Hogar, "Hogar.png"),
    "Bananya": (info2.Bananya, "Bananya.png"),

    # Documentales
    "Gente de gatos": (info2.Gente, "Gente.png"),
    "Mi gato endemoniado": (info2.Endemoniado, "Endemoniado.png"),
    "A los gatos, ni tocarlos: Un asesino en Internet": (info2.Asesino, "Asesino.png")
}

datos_records = {
    "Crème Puff": (info4.Viejo, "Viejo.png"),
    "Stewie":(info4.Largo, "Largo.png"),
    "Barivel": (info4.Largo2, "Largo2.png"),
    "Fenrir": (info4.Alto, "Alto.png"),
    "Arcturus": (info4.Alto2, "Alto2.png"),
    "Missi": (info4.Bigotes, "Bigotes.png"),
    "Merlin": (info4.Ronroneo, "Ronroneo.png"),
    "Smokey": (info4.Ronroneo2, "Ronroneo2.png"),
    "Bella": (info4.Ronroneo3, "Ronroneo3.png"),
    "Lilieput": (info4.Corto, "Corto.png"),
    "Didga": (info4.Trucos, "Trucos.png"),
    "Maru": (info4.YouTube, "YouTube.png"),
    "Cygnus": (info4.Cola, "Cola.png")
}