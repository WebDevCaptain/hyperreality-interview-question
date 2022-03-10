from flask import make_response, abort
from database.models.passenger import Passenger, PassengerSchema
from server_config import db


def read_all():
    passengers = Passenger.query.all()

    passenger_schema = PassengerSchema(many=True)
    data = passenger_schema.dump(passengers)
    return data


def create(passenger):
    aadhar_no = passenger.get("aadhar_no")

    existing_passenger = Passenger.query.filter(
        Passenger.aadhar_no == aadhar_no
    ).one_or_none()

    if existing_passenger is None:
        schema = PassengerSchema()
        new_passenger = schema.load(passenger, session=db.session)

        new_passenger.save_to_db()

        data = schema.dump(new_passenger)
        return data, 201
    else:
        abort(409, f"Passenger with Aadhar No. {aadhar_no} already exists")


def read_one(passenger_id):
    passenger = Passenger.query.filter(Passenger.id == passenger_id).one_or_none()

    if passenger is not None:
        passenger_schema = PassengerSchema()
        data = passenger_schema.dump(passenger)
        return data
    else:
        abort(404, f"Passenger with ID {passenger_id} not found")


def delete(passenger_id):
    passenger = Passenger.query.filter(Passenger.id == passenger_id).one_or_none()

    if passenger is not None:
        passenger.delete_from_db()
        return make_response(f"Passenger {passenger_id} deleted")
    else:
        abort(404, f"Passenger with ID {passenger_id} not found")


def update(passenger_id, passenger):
    update_passenger = Passenger.query.filter(
        Passenger.id == passenger_id
    ).one_or_none()

    aadhar_no = passenger.get("aadhar_no")

    existing_passenger = Passenger.query.filter(
        Passenger.aadhar_no == aadhar_no
    ).one_or_none()

    if update_passenger is None:
        abort(404, f"Passenger not found for Id: {passenger_id}")

    elif existing_passenger is None:
        abort(404, f"Passenger not found for aadhar_no {aadhar_no}")

    elif existing_passenger is not None and existing_passenger.id != passenger_id:
        abort(409, f"Passenger with aadhar_no {aadhar_no} exists already")

    else:
        schema = PassengerSchema()
        update = schema.load(passenger, session=db.session)

        update.id = update_passenger.id

        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update_passenger)

        return data, 200
