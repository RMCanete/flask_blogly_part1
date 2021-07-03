"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE = "https://www.freeiconspng.com/uploads/-mario-baseball-superstar-super-bros-png-26.png"
                    # July 2, 2021 - https://www.freeiconspng.com/img/49311 title="Image from freeiconspng.com"  img src="https://www.freeiconspng.com/uploads/-mario-baseball-superstar-super-bros-png-26.png"

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=True, default=DEFAULT_IMAGE)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

def connect_db(app):
    db.app = app
    db.init_app(app)

