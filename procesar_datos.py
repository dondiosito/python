def calcular_puntos(kills, asistencias, muertes):
    """Calcula los puntos de un jugador en base a kills, asistencias y muertes."""
    return (kills * 3) + (asistencias * 1) - (muertes * 2)


def determinar_mvp(ranking):
    """Determina el MVP de la ronda, es decir, el jugador con más puntos."""
    if not ranking:
        return None
    return max(ranking, key=lambda jugador: jugador['puntos'])


def generar_ranking(jugadores):
    """Genera el ranking de jugadores con sus respectivos puntos."""
    ranking = []
    for jugador in jugadores:
        puntos = calcular_puntos(jugador['kills'], jugador['asistencias'], jugador['muertes'])
        ranking.append({
            'nombre': jugador['nombre'],
            'kills': jugador['kills'],
            'asistencias': jugador['asistencias'],
            'muertes': jugador['muertes'],
            'puntos': puntos
        })
    return ranking


def procesar_datos(rondas):
    """Procesa los datos de varias rondas y genera el ranking final con MVPs."""
    ranking_final = {}
    mvp_contador = {}
    
    for ronda in rondas:
        ranking_ronda = generar_ranking(ronda)
        mvp = determinar_mvp(ranking_ronda)
        
        if mvp:
            mvp_contador[mvp['nombre']] = mvp_contador.get(mvp['nombre'], 0) + 1
        
        for jugador in ranking_ronda:
            nombre = jugador['nombre']
            if nombre not in ranking_final:
                ranking_final[nombre] = {
                    'kills': 0, 'asistencias': 0, 'muertes': 0, 'puntos': 0, 'MVPs': 0
                }
            ranking_final[nombre]['kills'] += jugador['kills']
            ranking_final[nombre]['asistencias'] += jugador['asistencias']
            ranking_final[nombre]['muertes'] += jugador['muertes']
            ranking_final[nombre]['puntos'] += jugador['puntos']
    
    for nombre in mvp_contador:
        if nombre in ranking_final:
            ranking_final[nombre]['MVPs'] = mvp_contador[nombre]
    
    ranking_ordenado = sorted(ranking_final.items(), key=lambda x: x[1]['puntos'], reverse=True)
    
    return ranking_ordenado
