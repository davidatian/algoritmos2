from flask import Flask
from config import db, DATABASE_URI
from routes.user_routes import  user_bp
from routes.product_routes import store_ph


app = Flask(__name__)

#Configurar la URI de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Inicializar la base de datos
db.init_app(app)

#Registrar los Blueprints de las rutas
app.register_blueprint(user_bp)
app.register_blueprint(store_ph)

#Crear las tablas si no existen
with app.app_context():


if __name__ == '__main__':
    app.run(debug=True)