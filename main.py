from flask import Flask
from routes import home, errorPage, eventSearch

app = Flask(__name__)

# routes
app.register_blueprint(home)
app.register_blueprint(errorPage)
app.register_blueprint(eventSearch)

if __name__ == "__main__":
    app.run(debug=True)
