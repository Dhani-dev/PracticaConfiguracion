from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Práctica configuración - Mi aplicación"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)  # Escuchar en el puerto 80
