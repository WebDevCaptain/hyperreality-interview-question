from flask import make_response
from server_config import connexion_app, db

connexion_app.add_api("ApiSpec.yml")


@connexion_app.route("/")
def home():
    return make_response(
        "Welcome to Passenger API. Please visit the github repo to find out more on the usage of this API",
        200,
    )


@connexion_app.app.before_first_request
def create_tables():
    db.create_all()


if __name__ == "__main__":
    connexion_app.run(debug=True)
