from FtoB import database, app
from FtoB.models import Usuario, Foto

with app.app_context():
    database.create_all()