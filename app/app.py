import os
from flask import Flask
from flask_cors import CORS
from api.user_api import user_api
from api.country_api import country_api
from api.place_api import place_api
from api.amenities_api import amenities_api
from api.review_api import review_api
from api.cities_api import cities_api
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost"}})

port = os.getenv("PORT", 5000)

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Test application"
    },
)

app.register_blueprint(swaggerui_blueprint)
app.register_blueprint(user_api)
app.register_blueprint(country_api)
app.register_blueprint(place_api)
app.register_blueprint(amenities_api)
app.register_blueprint(review_api)
app.register_blueprint(cities_api)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=port)
