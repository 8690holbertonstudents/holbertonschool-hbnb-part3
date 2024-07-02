from flask import Blueprint, jsonify, request
from models.country import Country
from models.city import City
from persistence.datamanager import DataManager
from config import Config, db
from sqlalchemy.orm import sessionmaker
import pycountry

Session = sessionmaker(bind=Config.engine)
session = Session()

cities_api = Blueprint("cities_api", __name__)


@cities_api.route("/cities", methods=["POST"])
def create_cities():
    """
    Function used to create a new city, send it to the database datamanager
    """
    city_data = request.get_json()
    country_code = city_data.get('country_code')
    city_name = city_data.get('city_name')

    if not all([country_code, city_name]):
        return jsonify({"Error": "Missing required field."}), 400

    new_city = City(city_name=city_name, country_code=country_code)
    if not new_city:
        return jsonify({"Error": "setting up new user."}), 500

    is_city_uniq = \
        db.session.query(City.id).filter_by(city_name=city_name, \
                                            country_code=country_code).first()
    if is_city_uniq:
        return jsonify({"Error": "City already exists in this country."}), 409

    DataManager.create(new_city, db.session)
    db.session.refresh(new_city)
    return jsonify({"Success": "City added."}), 201



@cities_api.route("/cities", methods=["GET"])
def read_all_cities():
    all_cities = City.query.all()
    return jsonify([DataManager.read(city) for city in all_cities])


@cities_api.route("/cities/<country_code>", methods=["GET"])
def read_one_cities():
    one_city = City.query.filter_by(id=id)
    if not one_city:
        return jsonify({"Error": "City not found."}), 404
    return jsonify([DataManager.read(city) for city in one_city])


@cities_api.route("/cities/<country_code>", methods=["PUT"])
def update_city(id):
    city = City.query.get(id)
    if not city:
        return jsonify({'Error': 'City not found'}), 404

    updates = request.get_json()
    if not updates:
        return jsonify({'Error': 'No update provided'}), 409

    DataManager.update(city, updates, db.session)
    db.session.refresh(city)
    return jsonify({"Success": "City updated.", "City": DataManager.read(city)}), 201


@cities_api.route("/cities/<country_code>", methods=["DELETE"])
def delete_city(id):
    city = City.query.get(id)
    if not city:
        return jsonify({'Error': 'City not found'}), 404
    DataManager.delete(city, db.session)
    return jsonify({'Success': 'City deleted'}), 201
