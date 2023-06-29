import requests

def obtener_distancia(ciudad_chile, ciudad_latinoamerica):
    url = "http://www.mapquestapi.com/directions/v2/route"
    params = {
        "key": "HAZukgjyYJStYwqTV6NvpU7qqUPj5JAv",
        "from": ciudad_chile,
        "to": ciudad_latinoamerica,
        "unit": "k",
        "locale": "es_ES"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200 and data["info"]["statuscode"] == 0:
        distancia = round(data["route"]["distance"], 3)
        return distancia
    else:
        return None

def calcular_duracion(distancia):
    velocidad_promedio = 60  # km/h
    tiempo_horas = distancia / velocidad_promedio
    tiempo_minutos = tiempo_horas * 60
    tiempo_segundos = tiempo_minutos * 60
    return tiempo_horas, tiempo_minutos, tiempo_segundos

def calcular_combustible(distancia):
    consumo_litros_por_km = 0.12
    combustible_requerido = round(distancia * consumo_litros_por_km, 3)
    return combustible_requerido

while True:
    # Solicitar ciudades de origen y destino en español
    ciudad_chile = input("Ingrese la ciudad de Inicio y si desea salir presione la tecla q: ")
    if ciudad_chile.lower() == "q":
        print("Programa finalizado.")
        break

    ciudad_latinoamerica = input("Ingrese la ciudad de Destino: ")

    # Obtener distancia utilizando la API de MapQuest
    distancia = obtener_distancia(ciudad_chile, ciudad_latinoamerica)

    # Calcular duración del viaje
    tiempo_horas, tiempo_minutos, tiempo_segundos = calcular_duracion(distancia)

    # Calcular combustible requerido
    combustible_requerido = calcular_combustible(distancia)

    # Imprimir resultados
    if distancia is None:
        print("No se pudo obtener la distancia. Asegúrate de ingresar ciudades válidas.")
    else:
        print("1.-La distancia entre", ciudad_chile, "y", ciudad_latinoamerica, "es de", distancia, "kilómetros.")
        print("2.- La duración del viaje es de", round(tiempo_horas, 3), "horas,", round(tiempo_minutos, 3), "minutos,", round(tiempo_segundos, 3), "segundos.")
        print("3.- Se requieren", combustible_requerido, "litros de combustible para el viaje.")
        print("4.- Saldrás de", ciudad_chile, "y llegarás a", ciudad_latinoamerica, "recorriendo una distancia de", distancia, "kilómetros.")
        print("5.- El viaje tomará aproximadamente", round(tiempo_horas, 3), "horas,", round(tiempo_minutos, 3), "minutos, y", round(tiempo_segundos, 3), "segundos.")
        print("6.- Se recomienda cargar", combustible_requerido, "litros de combustible antes de partir.")
