import random

# Definición de elementos para la generación de historias
personajes = [
    "un valiente caballero", "una princesa astuta", "un dragón temible", "un mago sabio", "un astuto ladrón",
    "una bruja malvada", "un rey justo", "un guerrero legendario", "un elfo místico", "una sirena encantadora"
]
lugares = [
    "en un reino lejano", "en un misterioso bosque", "en un castillo encantado", "en una pequeña aldea", "en una isla desierta",
    "en una montaña nevada", "en un desierto abrasador", "en una ciudad mágica", "en una cueva oscura", "en una torre abandonada"
]
acciones = [
    "buscar un tesoro perdido", "rescatar a un ser querido", "enfrentar sus miedos", "descubrir un antiguo secreto", "vencer a un enemigo poderoso",
    "explorar tierras desconocidas", "romper una maldición", "encontrar un artefacto mágico", "proteger su reino", "buscar la verdad"
]
objetivos = [
    "probar su valentía", "salvar su hogar", "cumplir una profecía", "encontrar la paz", "obtener un gran poder",
    "restaurar el equilibrio", "ganar una guerra", "reunir a su familia", "demostrar su inocencia", "descubrir su destino"
]
objetos = [
    "una espada mágica", "un escudo indestructible", "una poción de invisibilidad", "un amuleto antiguo", "un mapa del tesoro",
    "un libro de hechizos", "una capa de invisibilidad", "una llave mágica", "una varita poderosa", "un anillo encantado"
]
eventos = [
    "una tormenta feroz", "un monstruo aterrador", "una puerta mágica", "una sombra misteriosa", "un sonido extraño",
    "un terremoto", "un eclipse", "una batalla épica", "un hechizo fallido", "una visión profética"
]
resultados = [
    "encontró la felicidad", "salvó el día", "resolvió el problema", "conquistó el reino", "descubrió un secreto",
    "ganó el respeto de todos", "restauró la paz", "destruyó el mal", "se convirtió en leyenda", "aprendió una valiosa lección"
]

# Plantillas de historias
plantillas = [
    "Había una vez {personaje} que vivía {lugar}. Un día, decidió {accion} para {objetivo}. Con la ayuda de {objeto}, se enfrentó a {evento} y finalmente {resultado}.",
    "En {lugar}, {personaje} se embarcó en una aventura para {accion}. Armado con {objeto}, su objetivo era {objetivo}. Durante su viaje, encontró {evento} y al final {resultado}.",
    "{personaje} estaba {accion} {lugar} cuando de repente {evento}. Usando {objeto}, logró {objetivo} y así {resultado}.",
    "Un día, {personaje} decidió que era tiempo de {accion}. Con {objeto} en mano, viajó {lugar} con el objetivo de {objetivo}. Durante su viaje, {evento} ocurrió, pero al final {resultado}.",
    "En el corazón de {lugar}, {personaje} se encontraba {accion}. Con la ayuda de {objeto}, su misión era {objetivo}. Pero {evento} cambió su camino, y finalmente {resultado}.",
    "Hace mucho tiempo, {personaje} vivía tranquilamente {lugar}. Sin embargo, un día decidió {accion} para {objetivo}. Equipado con {objeto}, enfrentó {evento} y {resultado}.",
    "{personaje} siempre había querido {accion}, así que partió {lugar} con {objeto}. Su objetivo era {objetivo}, pero durante su aventura, {evento}. Al final, {resultado}.",
    "En una tierra lejana, {personaje} emprendió un viaje para {accion}. Con {objeto} como su aliado, buscaba {objetivo}. Se encontró con {evento} y {resultado}.",
    "Una vez, {personaje} decidió que debía {accion}. Viajó {lugar} con {objeto}, determinado a {objetivo}. En su camino, {evento}, y al final {resultado}.",
    "En un antiguo {lugar}, {personaje} estaba {accion}. Con {objeto} en mano, tenía la misión de {objetivo}. Pero cuando {evento} sucedió, supo que {resultado}."
]

def es_coherente(personaje, accion, objetivo):
    # Reglas de coherencia básicas
    if personaje == "un valiente caballero" and "proteger" not in accion and "valentía" not in objetivo:
        return False
    if personaje == "una princesa astuta" and "astucia" not in objetivo:
        return False
    if personaje == "un dragón temible" and "destruir" not in accion and "temible" not in objetivo:
        return False
    if personaje == "un mago sabio" and "magia" not in accion and "sabiduría" not in objetivo:
        return False
    if personaje == "un astuto ladrón" and "robar" not in accion and "astucia" not in objetivo:
        return False
    return True

def generar_historia():
    # Selección aleatoria de una plantilla y sus elementos
    plantilla = random.choice(plantillas)
    intentos = 0
    max_intentos = 10
    
    while intentos < max_intentos:
        personaje = random.choice(personajes)
        lugar = random.choice(lugares)
        accion = random.choice(acciones)
        objetivo = random.choice(objetivos)
        objeto = random.choice(objetos)
        evento = random.choice(eventos)
        resultado = random.choice(resultados)

        # Validar coherencia
        if es_coherente(personaje, accion, objetivo):
            historia = plantilla.format(
                personaje=personaje,
                lugar=lugar,
                accion=accion,
                objetivo=objetivo,
                objeto=objeto,
                evento=evento,
                resultado=resultado
            )
            return historia
        
        intentos += 1
    
    # Si no se encuentra una combinación coherente
    return "No se pudo generar una historia coherente."

# Generar y mostrar una historia
print(generar_historia())

# Generar múltiples historias
def generar_varias_historias(n):
    historias = []
    for _ in range(n):
        historias.append(generar_historia())
    return historias

# Ejemplo de uso para generar 5 historias
for historia in generar_varias_historias(5):
    print("\n" + historia)
