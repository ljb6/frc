from flask import Flask
from routes import home

app = Flask(__name__)

# routes
app.register_blueprint(home)

if __name__ == "__main__":
    app.run(debug=True)
