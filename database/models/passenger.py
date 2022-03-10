from datetime import datetime
from server_config import db, mm


class Passenger(db.Model):
    __tablename__ = "passenger"

    id = db.Column(db.Integer, primary_key=True)
    checked = db.Column(db.Boolean)
    name = db.Column(db.String(50))
    aadhar_no = db.Column(db.String(16), index=True)
    type = db.Column(db.String(12))
    age = db.Column(db.Integer)
    description = db.Column(db.String(128))
    date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


class PassengerSchema(mm.SQLAlchemyAutoSchema):
    class Meta:
        model = Passenger
        load_instance = True
