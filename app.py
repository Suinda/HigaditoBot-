from flask import Flask
app = Flask(__name__)

@app.route("/")
def higadito():
    return "HigaditoBot dice: ¡Come vísceras y repite el placer!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
