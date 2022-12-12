
#TODO ******************** IMPORTANTE************

# Archivo creado con el fin de guardar en variables los datos capturados desde el archivo .env, de esta forma a la hora de subir el proyecto a un repositorio, no subimos con nuestros usuarios y contraseñas utilizadas en el mismo. Es decir, los demas solo veran las variables, no los datos que contienen esas variables, de esa forma protegemos nuestros datos.

#Para que esto funcione se hace esto:
# 1 - se instala el paquete python-dotenv con pip install
# 2 - se crea un archivo llamado .env en el directorio principal
# 3 - dentro de este archivo se crean las variables con los valores que queremos proteger (usuarios, pass,  etc).
# 4 - se crea un archivo config.py en el cual importamos "load_dotenv" desde dotenv, tambien importamos "os"
# 5 - llamamos la funcion load_dotenv()
# 6 - nombramos nuevamente las variables que queremos que aparezcan y a ellas les damos el valor de "os.environ['nombre_de_la_variable_en_.env']", dentro de los corchetes va el nombre que les dimos anteriormente dentro el archivo .env
# 7 - Por ultimo, creamos el archivo .gitignore y dentro de el agregamos el archivo .env, de esta forma no se subiria al repositorio y solo quedarian las variables declaradas en config.py haciendo referencia a los valores sin mostrarlos.
# 8 - usando el comando pip freeze > requirements.txt creamos el archivo con las dependencias utilizadas en el proyecto, asi el que quiera probarlo, puede ver que necesita descargar e instalar
# 9 - pip install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy pymysql  -U flask-cors

from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ['MYSQL_USER']
password = os.environ['MYSQL_PASSWORD']
host = os.environ['MYSQL_HOST']
port = os.environ['MYSQL_PORT']
database = os.environ['MYSQL_DB']

DATABASE_CONNECTION_URI = f'mysql://{user}:{password}@{host}:{port}/{database}'