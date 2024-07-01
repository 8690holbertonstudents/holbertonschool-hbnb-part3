import os
from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import *


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)

    # Setup the Flask-JWT-Extended extension
    app.config["JWT_SECRET_KEY"] = "iknownothingbuticanexplain"  # Change this!
    jwt = JWTManager(app)

    from api.amenities_api import amenities_api
    app.register_blueprint(amenities_api)

    from api.cities_api import cities_api
    app.register_blueprint(cities_api)

    from api.country_api import country_api
    app.register_blueprint(country_api)

    from api.place_api import place_api
    app.register_blueprint(place_api)

    from api.review_api import review_api
    app.register_blueprint(review_api)

    from api.user_api import user_api
    app.register_blueprint(user_api)

    return app


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=port)
