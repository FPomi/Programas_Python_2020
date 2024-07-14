import math

# Se calcula la distancia entre latitudes y longitudes, a partir de eso se pasa a km y se redondea

def calculo_distancia(ubicacion, ubicacion_usuario_prueba):
  
  latitud_usuario_principal, longitud_usuario_principal = ubicacion
  latitud_usuario_prueba, longitud_usuario_prueba = ubicacion_usuario_prueba
  
  radio_tierra = 6367
  distancia_latitud = latitud_usuario_prueba - latitud_usuario_principal
  distancia_longitud = longitud_usuario_prueba - longitud_usuario_principal

  a = math.sin(math.radians(distancia_latitud/2))**2 + math.cos(math.radians(latitud_usuario_principal)) * math.cos(math.radians(latitud_usuario_prueba)) * math.sin(math.radians(distancia_longitud/2))**2
  c = 2 * math.atan2(math.sqrt(a),  math.sqrt(1-a))
  distancia_en_km = radio_tierra * c

  if distancia_en_km < 1:
    distancia_en_km = round(distancia_en_km, 3)

  elif 1 < distancia_en_km < 10:
    distancia_en_km = round(distancia_en_km, 2)

  elif 10 < distancia_en_km < 100:
    distancia_en_km = round(distancia_en_km, 1)
  
  else:
    distancia_en_km = round(distancia_en_km)
        
  return distancia_en_km