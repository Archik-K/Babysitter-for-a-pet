import enum
from core import db


class AnimalsEnum(enum.Enum):
    cat = "cat"
    dog = "dog"
    parrot = "parrot"
    guinea_pig = "guinea pig"


class Nanny(db.Model):
    id = db.Column(db.Integer,  primary_key=True)
    name = db.Column(db.VARCHAR(64), nullable=False)
    animal = db.Column(db.Enum(AnimalsEnum), nullable=False)
    photo = db.Column(db.VARCHAR(256))
    birthday = db.Column(db.Date, nullable=False)
    place = db.Column(db.VARCHAR(64), nullable=False)
    rate = db.Column(db.Integer, nullable=False)
    practice = db.Column(db.Integer, nullable=False)
    contact = db.Column(db.VARCHAR(256), nullable=False)
    about = db.Column(db.VARCHAR(512))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "animal": self.animal.value,
            "photo": self.photo,
            "birthday": self.birthday.strftime("%Y-%m-%d"),
            "place": self.place,
            "rate": self.rate,
            "practice": self.practice,
            "contact": self.contact,
            "about": self.about
        }