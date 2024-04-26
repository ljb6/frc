from flask import Flask
from routes import home, teamSearch, errorPage

app = Flask(__name__)

# routes
app.register_blueprint(home)
app.register_blueprint(teamSearch)
app.register_blueprint(errorPage)

if __name__ == "__main__":
    app.run(debug=True)
