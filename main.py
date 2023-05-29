import random
from urllib import request
from flask import *

app = Flask(__name__)
COLOR = ["#daf7a6","#ff5733","#581845","#f1948a"]

intentos = []
intentos_adversario = []

def generador_secretos(listaColores:list):
    secreto = []
    for posible_secretito in random.choice(listaColores):
        secreto.append(posible_secretito)
    return secreto

def intento_maquina() -> list:
    intento_advesario = []
    for posible_color in random.choice(COLOR):
        intento_advesario.append(posible_color)
    return intento_advesario
def comprobador_aciertos(intento:list,secreto:list):
    resultado = []
    for color in intento:
        if color == secreto[intento.index(color)]:
            resultado.append("#00ff61")  # Acierto: color verde
        elif color != secreto[intento.index(color)] and color in secreto:
             resultado.append("#ffff00") # no coincide pero está en el secreto
        else:
            resultado.append("#ff4500")  # No coincide: color naranja
    return resultado

def fucking_partida():
     return

secreto = generador_secretos(COLOR)
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        intento_actual = [
            request.form["color1"],
            request.form["color2"],
            request.form["color3"],
            request.form["color4"]
        ]
        intento_sin_comprobar = intento_maquina()
        intento_adversario = comprobador_aciertos(intento_sin_comprobar, secreto)
        comprobar_intento = comprobador_aciertos(intento_actual, secreto)
        if len(intentos_adversario) == 4:
            intentos_adversario.pop(0)
            intentos_adversario.append(intento_adversario)
        else:
            intentos_adversario.append(intento_adversario)
        if len(intentos) == 4:
            intentos.pop(0)
            intentos.append(comprobar_intento)
        else:
            intentos.append(comprobar_intento)
    return render_template("index.html", intentos=intentos, intentos_adversario=intentos_adversario)
if __name__ == "__main__":
    app.run()