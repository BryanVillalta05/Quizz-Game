import time

print("Bienveniido a una sesion de preguntas al azar de distintos temas")
print("Instrucciones: \n -Seran 10 preguntas en total \n -Si respondes bien una pregunta se te sumara un punto \n -Si fallas una se te restara 1 punto")
print("¡Empecemos!")
score=10
time.sleep(1)

print("Preguna 1: \n ¿Qué palabra usarías para describir a una persona que no tiene todos los dedos en una mano?")
respuesta = input("Ingrese su respuesta: ")
if respuesta == "persona normal":
    print("¡Acertaste!")
    score+=1
    print(score)
else:
    print("Fallaste :(")
    score-=1
    print(score)

time.sleep(1)

print("Preguna 2: \n Es completamente tuyo, sin embargo, todos lo usan... ¿qué es?")
respuesta = input("Ingrese su respuesta: ")
if respuesta == "el nombre":
    print("¡Acertaste!")
    score+=1
    print(score)
else:
    print("Fallaste :(")
    score-=1
    print(score)

time.sleep(1)

print("Preguna 3: \n ¿Qué puedes sostener en tu mano derecha, pero nunca en tu mano izquierda?")
respuesta = input("Ingrese su respuesta: ")
if respuesta == "la mano izquierda":
    print("¡Acertaste!")
    score+=1
    print(score)
else:
    print("Fallaste :(")
    score-=1
    print(score)

time.sleep(1)

print("Preguna 4: \n ¿Cuál es el principal motivo por el cual la gente se divorcia")
respuesta = input("Ingrese su respuesta: ")
if respuesta == "el matrimonio":
    print("¡Acertaste!")
    score+=1
    print(score)
else:
    print("Fallaste :(")
    score-=1
    print(score)

time.sleep(1)

print("Preguna 5: \n ¿Qué es lo más importante para que no caiga un rayo en casa?")
respuesta = input("Ingrese su respuesta: ")
if respuesta == "que no llueva":
    print("¡Acertaste!")
    score+=1
    print(score)
else:
    print("Fallaste :(")
    score-=1
    print(score)

time.sleep(1)

print("Preguna 6: \n Quien lo fabrica no lo necesita, a quien lo compra no le sirve y quien lo usa no puede ni verlo ni sentirlo, ¿qué es?")
respuesta = input("Ingrese su respuesta: ")
if respuesta == "un ataud":
    print("¡Acertaste!")
    score+=1
    print(score)
else:
    print("Fallaste :(")
    score-=1
    print(score)

time.sleep(1)

print("Preguna 7: \n Solo hay una pregunta que nadie podrá responder afirmativamente y diciendo la verdad, ¿cuál es?")
respuesta = input("Ingrese su respuesta: ")
if respuesta == "¿Estas dormido?":
    print("¡Acertaste!")
    score+=1
    print(score)
else:
    print("Fallaste :(")
    score-=1
    print(score)

time.sleep(1)

print("Preguna 8: \n ¿Qué sube, pero nunca baja?")
respuesta = input("Ingrese su respuesta: ")
if respuesta == "la edad":
    print("¡Acertaste!")
    score+=1
    print(score)
else:
    print("Fallaste :(")
    score-=1
    print(score)

time.sleep(1)

print("Preguna 9: \n Imagina que te encuentras en una habitación oscura... ¿cómo sales de ahí?")
respuesta = input("Ingrese su respuesta: ")
if respuesta == "dejando de imaginar":
    print("¡Acertaste!")
    score+=1
    print(score)
else:
    print("Fallaste :(")
    score-=1
    print(score)

time.sleep(1)

print("Preguna 10: \n ¿Cuántas manzanas crecen en los árbol?")
respuesta = input("Ingrese su respuesta: ")
if respuesta == "todas":
    print("¡Acertaste!")
    score+=1
    print(score)
else:
    print("Fallaste :(")
    score-=1
    print(score)

time.sleep(1)

print("Quizz terminado, has llegado al final, felicidades\nAhora revisemos tú puntaje")
print("Tú puntaje es: ", score)
if score < 5:
    print("Buena suerte la proxima")
elif score == 5:
    print("5/10 lo hiciste bien, pero puedes mejorar")
elif score >= 8:
    print("Felicidades")
