from flask import Flask
app = Flask(__name__)

@app.route("/")
def higadito():
    return "HigaditoBot dice: ¡Come vísceras y repite el placer!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "HigaditoBot dice: ¡Come vísceras y repite el placer!"

@app.route("/ayuno")
def ayuno():
    return "El ayuno es como limpiar los pasillos del estómago. 16:8 o no existe."

@app.route("/sopa")
def sopa():
    return "Sopa de mollejas: lo que no te mata, te hace más fuerte."

@app.route("/rinones")
def rinones():
    return "Riñones al vino: cuidado, el vino se te sube antes que la proteína."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
