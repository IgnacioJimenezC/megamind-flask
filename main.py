import random
from urllib import request

from flask import *

app = Flask(__name__)
COLOR = ["#daf7a6","#ff5733","#581845","#f1948a"]
secreto = list(COLOR)
random.shuffle(secreto)
intentos = []

intento_adversario= list(COLOR)
random.shuffle(intento_adversario)

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

@app.route('/',methods=["GET", "POST"])
def index():
  if request.method == "POST":
     intento_actual = [
            request.form["color1"],
            request.form["color2"],
            request.form["color3"],
            request.form["color4"]
        ]

     resultado = comprobador_aciertos(intento_actual,secreto)
     if len(intentos) == 4:
         intentos.pop(0)
         intentos.append(resultado)
     else:
        intentos.append(resultado)
  return render_template("index.html", intentos= intentos, COLOR = COLOR, intento_adversario = intento_adversario)
if __name__ == "__main__":
    app.run()