from flask import make_response
from server_config import connexion_app

connexion_app.add_api("ApiSpec.yml")


@connexion_app.route("/")
def home():
    return make_response("Welcome to Passenger API", 200)


if __name__ == "__main__":
    connexion_app.run(debug=True)
