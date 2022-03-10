import os
from database.models.passenger import Passenger
from server_config import db


def seed():
    # Example Passengers
    PASSENGERS = [
        {
            "checked": True,
            "name": "Arvind",
            "type": "AC",
            "age": 22,
            "description": "Regular from PAT to DEL",
            "aadhar_no": "1234567891011121",
        },
        {
            "checked": True,
            "name": "Manish",
            "type": "Non-AC",
            "age": 21,
            "description": "Regular from DEL to RNC",
            "aadhar_no": "1234567891011122",
        },
        {
            "checked": False,
            "name": "Prithvi",
            "type": "Non-AC",
            "age": 20,
            "description": "Occasionally from BLR to DEL",
            "aadhar_no": "1234567891011123",
        },
    ]

    if os.path.exists("data.db"):
        os.remove("data.db")

    db.create_all()

    for passenger in PASSENGERS:
        p = Passenger(
            checked=passenger["checked"],
            name=passenger["name"],
            type=passenger["type"],
            age=passenger["age"],
            description=passenger["description"],
            aadhar_no=passenger["aadhar_no"],
        )
        db.session.add(p)

    db.session.commit()


if __name__ == "__main__":
    seed()
