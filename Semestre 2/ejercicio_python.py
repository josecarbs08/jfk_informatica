import random

print("="*60)
print("BIENVENIDO AL TORNEO DEL MULTIVERSO TANGIBLE")
print("="*60)
print("El Creador ha fusionado 6 mundos. Para ganar $2 billones de dólares")
print("necesitas 5 llaves elementales y la contraseña de la habitación FIFA 21.")
print("¡Comienza la prueba!\n")

hab_minecraft = {"¿Minecraft fue desarrollado en Java?": "si",
"¿Quién es el mejor mod?": "creeper",
"¿Quién es el enemigo de Steve?": "herobrine",
"¿Quién fue el creador de  minecraft?": "notch",
"¿Qué versión de minecraft está en consola?": "bedrock"

}


hab_valorant = {"¿Qué agente de Valorant tiene la habilidad de revivir aliados?": "sage",
"¿Qué agente no necesita mucha skill?": "harbor".,
"¿Qué arma es la favorita de valorant?": "phantom",
"¿Qué es mejor una pistola o el cuchillo?": "cuchillo",
"¿Qué agente de Valorant tiene la habilidad de teletransportarse?": "yoru"


}


hab_aoe2 = {"¿Qué recurso principal se necesita para crear un aldeano en AoE II?": "comida",
"¿Qué recurso principal no se necesita para crear un aldeano en AoE II?": "paja",
"¿Está perfecta la app de móvil?": "no"
}
hab_lol = {"¿Qué monstruo neutral otorga el buffo morado a los súbditos?": "baron"
"¿Urgor q rol es?": "top",
"¿Ezrael q tiene  q hacer ?": "apuntar"

}
hab_zelda = {"¿Cómo se llama el protagonista de Zelda BotW?": "link",
"¿A qué princesa debes salvar?": "zelda",
"¿Qué le pasó a link?": "se le borró la memoria"
}

llaves = 0
habitaciones_completadas = []
letras_obtenidas = []

while llaves < 5:
    habitacion_actual = random.randint(1, 5)
    
    if habitacion_actual in habitaciones_completadas:
        continue
        
    print("-" * 40)
    if habitacion_actual == 1:
        print(">> Entraste a la habitación: MINECRAFT")
        pregunta = random.choice(list(hab_minecraft.keys()))      
        respuesta_correcta = hab_minecraft[pregunta]
        
        respuesta_usuario = input(pregunta + " ").strip().lower()
        
        if respuesta_usuario == respuesta_correcta:
            print("¡Correcto! Obtienes 1 llave elemental y la letra: M")
            llaves += 1
            habitaciones_completadas.append(1)
            letras_obtenidas.append("M")
        else:
            print("Respuesta incorrecta. Un portal te succiona hacia otra habitación...")
            
    elif habitacion_actual == 2:
        print(">> Entraste a la habitación: VALORANT")
        pregunta = random.choice(list(hab_valorant.keys())) 
        respuesta_correcta = hab_valorant[pregunta]
        
        respuesta_usuario = input(pregunta + " ").strip().lower()
        
        if respuesta_usuario == respuesta_correcta:
            print("¡Correcto! Obtienes 1 llave elemental y la letra: E")
            llaves += 1
            habitaciones_completadas.append(2)
            letras_obtenidas.append("E")
        else:
            print("Respuesta incorrecta. Un portal te succiona hacia otra habitación...")
            
    elif habitacion_actual == 3:
        print(">> Entraste a la habitación: AGE OF EMPIRES II")
        pregunta = random.choice(list(hab_aoe2.keys())) 
        respuesta_correcta = hab_aoe2[pregunta]
        
        respuesta_usuario = input(pregunta + " ").strip().lower()
        
        if respuesta_usuario == respuesta_correcta:
            print("¡Correcto! Obtienes 1 llave elemental y la letra: S")
            llaves += 1
            habitaciones_completadas.append(3)
            letras_obtenidas.append("S")
        else:
            print("Respuesta incorrecta. Un portal te succiona hacia otra habitación...")
            
    elif habitacion_actual == 4:
        print(">> Entraste a la habitación: LEAGUE OF LEGENDS")
        pregunta = random.choice(list(hab_lol.keys())) 
        respuesta_correcta = hab_lol[pregunta]
        
        respuesta_usuario = input(pregunta + " ").strip().lower()
        
        if respuesta_usuario == respuesta_correcta:
            print("¡Correcto! Obtienes 1 llave elemental y la letra: S")
            llaves += 1
            habitaciones_completadas.append(4)
            letras_obtenidas.append("S")
        else:
            print("Respuesta incorrecta. Un portal te succiona hacia otra habitación...")
            
    elif habitacion_actual == 5:
        print(">> Entraste a la habitación: ZELDA BOTW")
        pregunta = list(hab_zelda.keys())[0]
        respuesta_correcta = hab_zelda[pregunta]
        
        respuesta_usuario = input(pregunta + " ").strip().lower()
        
        if respuesta_usuario == respuesta_correcta:
            print("¡Correcto! Obtienes 1 llave elemental y la letra: I")
            llaves += 1
            habitaciones_completadas.append(5)
            letras_obtenidas.append("I")
        else:
            print("Respuesta incorrecta. Un portal te succiona hacia otra habitación...")

print("\n" + "="*60)
print("¡Felicidades! Tienes las 5 llaves elementales.")
print("Las letras que conseguiste en tu aventura son:", letras_obtenidas)
print("Ahora estás frente a la gran puerta del estadio de FIFA 21.")
print("El panel de seguridad requiere una contraseña para abrir la bóveda.")

password_final = input("Ingresa la contraseña final: ").strip().upper()

if password_final == "MESSI":
    print("\n¡ACCESO CONCEDIDO! La puerta de FIFA 21 se abre.")
    print("El Creador aparece frente a ti con el maletín. ¡Ganaste los $2 billones de dólares!")
else:
    print("\n¡ACCESO DENEGADO! Las alarmas suenan. La puerta se sella para siempre.")
    print("Has perdido el torneo. Fin del juego.")
