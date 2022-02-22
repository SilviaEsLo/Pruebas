from flask import Flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
# la ruta home
def home():
    return "ESEN"
    
if __name__ == "__main__":
    app.run(debug=True)
