import discord
from discord.ext import commands
import peliculas as lista_peliculas
import series as lista_series
import juegos as lista_juegos
import records as lista_records
import random
from datos import datos_peliculas, datos_series, datos_juegos, datos_records, normalizar
from pathlib import Path

intents = discord.Intents.default()
intents.message_content = True

# Ubicación de las imágenes de las películas
Pelicula_Imagenes = Path(__file__).parent / "imagenes de peliculas"

# Ubicacion de las imagenes de las series 
Series_Imagenes = Path(__file__).parent / "imagenes de series"

# Ubicacioón de las imagenes de los juegos
Juegos_Imagenes = Path(__file__).parent/ "imagenes de juegos"

# Ubicacion de las imagenes de los records
Records_Imagenes = Path(__file__).parent/ "imagenes de record guinness"


bot = commands.Bot(command_prefix='&', intents=intents)

# Guardar el catálogo seleccionado por cada usuario
catalogos = {}

#confirmacion de los records
Confirmar_Records = set()

@bot.command()
async def hola(ctx):
    await ctx.send("Hola, soy un bot que se algunas cosas. Si quieres ver unos de esos escribe &catalogo te enseñare lo que tengo en mi catalogo 😺.")

@bot.command()
async def catalogo(ctx):
    await ctx.send("😺🧾 a ver tengo peliculas, series, juegos y records. si quieres ver unas de esas escribe &peliculas para ver mis peliculas 📹, &series para ver mis series 📺, &juegos para ver mis juegos 🎮 y &records para ver mis records 🏆.")

@bot.command()
async def peliculas(ctx):
    catalogos[(ctx.guild.id if ctx.guild else None, ctx.author.id)] = "peliculas"
    await ctx.send("!Genial! tengo peliculas de drama 🎭 , terror 👻 , comedia 😹, animacion 🎨 , anime 🇯🇵 y documentales 🎤. Si quieres ver unas de esas peliculas escribe 1 para drama, 2 para terror, 3 para comedia, 4 para animacion, 5 para anime o 6 para documental. Yo te enseño mi lista que tengo.")

@bot.command()
async def series(ctx):
    catalogos[(ctx.guild.id if ctx.guild else None, ctx.author.id)] = "series"
    await ctx.send("!Genial! tengo series de drama 🎭 , terror 👻 , comedia 😹 y documentales 🎤 . Si quieres ver unas de esas series escribe 1 para drama, 2 para terror, 3 para comedia o 4 para documental")

@bot.command()
async def juegos(ctx):
    catalogos[(ctx.guild.id if ctx.guild else None, ctx.author.id)] = "juegos"
    await ctx.send("!Genial! tengo juegos de aventuras 🗺️ , terror 👻 y infantiles 🧸 o tal vez no 😶 . Si quieres ver unas de esas peliculas escribe 1 para aventuras, 2 para terror y 3 para infantilis . Yo te enseño mi lista que tengo.")

@bot.command()
async def records(ctx):
    usuario = (ctx.guild.id if ctx.guild else None, ctx.author.id)

    Confirmar_Records.add(usuario)

    await ctx.send("!Genial! tengo gatos que ganaron records 🏆🐈. No te voy a mostrarte las lista porque sera aleotorio para no arriunar los sorprendentes gatos que ganaron records. Para aceptar escribe “acepto” ✅ sino escribe “no acepto” ❌ ")


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    usuario = (message.guild.id if message.guild else None, message.author.id)

    if usuario in Confirmar_Records:
        Respuesta = normalizar(message.content.strip())

        if Respuesta == "acepto":
            Confirmar_Records.discard(usuario)
            await message.channel.send("Exelente. aqui tienes un gato que gano un record")

            nombre, datos = random.choice(list(datos_records.items()))

            gato, imagen = datos

            embed = discord.Embed(
                title=f"🏆 {nombre}",
                description=gato["record"],
                color=discord.Color.gold()
            )

            embed.add_field(name="🌎 País", value=gato["Pais"])
            embed.add_field(name="🐾 Raza", value=gato["Raza"])
            embed.add_field(name="👤 Dueño", value=gato["Dueño"])
            embed.add_field(name="🏅 Logro", value=gato["logro"])
            embed.add_field(name="📅 Registro", value=gato["Registro"])
            embed.add_field(
                name="💡😼 Dato curioso",
                value=gato["Dato curioso"],
                inline=False)

            ruta = Records_Imagenes / imagen

            if ruta.is_file():
                archivo = discord.File(ruta, filename=ruta.name)

                embed.set_image(url=f"attachment://{ruta.name}")

                await message.channel.send(
                    embed=embed,
                    file = archivo
                )

            else:
                await message.channel.send(embed = embed)
                print(f"no se encontro ninguna imagen: {ruta}")
                

            return

        elif Respuesta == "no acepto":
            Confirmar_Records.discard(usuario)
            await message.channel.send("oki entiendo. puedes usar nuevamente &catalogo para ver otra cosa")
            return
    
    
    catalogo_actual = catalogos.get(usuario)

    if message.content.strip() == "1" and catalogo_actual == "peliculas":
        texto = "🎭 ¡Estas son mis películas de Drama!\n\n"
        lista = lista_peliculas.Drama

    elif message.content.strip() == "1" and catalogo_actual == "series":
        texto = "Estos son mis series de Drama \n\n"
        lista = lista_series.Drama

    elif message.content.strip() == "1" and catalogo_actual == "juegos":
        texto = " ¡Estos son mis juegos de Aventuras!\n\n"
        lista = lista_juegos.Aventuras

    elif message.content.strip() == "2" and catalogo_actual == "peliculas":
        texto = " Estas son mis películas de Terror \n\n"
        lista = lista_peliculas.Terror

    elif message.content.strip() == "2" and catalogo_actual == "series":
        texto = "Estas son mis series de Terror \n\n"
        lista = lista_series.Terror

    elif message.content.strip() == "2" and catalogo_actual == "juegos":
        texto = " ¡Estos son mis juegos de Terror!\n\n"
        lista = lista_juegos.Terror

    elif message.content.strip() == "3" and catalogo_actual == "peliculas":
        texto = "¡Estas son mis películas de Comedia!\n\n"
        lista = lista_peliculas.Comedia

    elif message.content.strip() == "3" and catalogo_actual == "series":
        texto = "Estas son mis series de Comedia \n\n"
        lista = lista_series.Comedia

    elif message.content.strip() == "3" and catalogo_actual == "juegos":
        texto = " ¡Estos son mis juegos Infantiles!\n\n"
        lista = lista_juegos.Infantil

    elif message.content.strip() == "4" and catalogo_actual == "peliculas":
        texto = "¡Estas son mis películas de Animación!\n\n"
        lista = lista_peliculas.Animacion

    elif message.content.strip() == "5" and catalogo_actual == "peliculas":
        texto = "¡Estas son mis películas de Anime!\n\n"
        lista = lista_peliculas.Anime

    elif message.content.strip() == "6" and catalogo_actual == "peliculas":
        texto = "¡Estos son mis documentales!\n\n"
        lista = lista_peliculas.Documental

    elif message.content.strip() == "4" and catalogo_actual == "series":
        texto = "Estos son mis documentales \n\n"
        lista = lista_series.Documental


    
    else:
        if catalogo_actual == "peliculas":
            datos_actuales = datos_peliculas
            carpeta_actual = Pelicula_Imagenes

        elif catalogo_actual == "series":
            datos_actuales = datos_series
            carpeta_actual = Series_Imagenes

        else:
            datos_actuales = datos_juegos
            carpeta_actual = Juegos_Imagenes
        for nombre, datos in datos_actuales.items():
            if normalizar(message.content) == normalizar(nombre):

                descripcion, imagen = datos

                if catalogo_actual == "juegos":
                    emoji = "🎮"
                    colores = discord.Color(0x8C51B5)
                    
                elif catalogo_actual == "series":
                    emoji = "📺"
                    colores = discord.Color(0xFF4F4F)

                else:
                    emoji = "🎬"
                    colores = discord.Color(0xD1D1D1)

                embed = discord.Embed(
                    title=f"{emoji} {nombre}",
                    description=descripcion,
                    color=colores
                )

                ruta = carpeta_actual / imagen

                if ruta.is_file():
                    archivo = discord.File(ruta, filename=ruta.name)

                    embed.set_image(url=f"attachment://{ruta.name}")

                    await message.channel.send(
                        embed=embed,
                        file=archivo
                    )

                else:
                    await message.channel.send(embed=embed)
                    print(f"No encontré la imagen: {ruta}")

                return

        await bot.process_commands(message)
        return

    if catalogo_actual == "peliculas":
        emoji = "🎬"

    elif catalogo_actual == "series":
        emoji = "📺"

    else:
        emoji = "🎮"

    for Tema in lista:
        texto += f"{emoji} {Tema}\n"

    await message.channel.send(texto)


























bot.run("TOKEN")