from app import app
from utils.db import db

db.init_app(app) #sin esta linea no puede iniciar la app y no crea la base de datos

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)