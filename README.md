# AppProfes


## Requisitos
Python 3.10
Django 4.1.3
HTML
CSS

### Instalacion git clone
Para clonar el proyecto se debe ejecutar:
git clone https://github.com/maramoyano/Entrega1-Moyano-Mara.git

### Instalación y ejecución del proyecto
Se debe crear el entorno virtual de python:

virtualenv venv
Luego activamos el entorno con el siguiente comando:

venv\Scripts\activate
Procedemos a instalar Django para correr el entorno:

pip install Django

Para correr el proyecto deben iniciar nuestro proyecto en la carpeta "Proyecto1" de la siguiente manera:

cd Proyecto1
Luego realizamos una migracion de nuestros Models para asegurarnos que corra todo bien:
python manage.py makemigrations
python manage.py migrate  
Por ultimo ejecutamos el proyecto de la siguiente manera:

python manage.py runserver
Esto iniciara un servidor web.
