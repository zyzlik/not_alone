echo "Hello, "$USER".  This script will set up your developers environment"
echo -n "Creating virtual environment..."
virtualenv -p python3 env

echo -n "Enter desired DB name and press [ENTER]: "
read db_name

echo -n "Creating user for database..."
createuser -P -s -e $USER

echo -n "Creating DB $db_name..."
createdb $db_name -O $USER

echo -n "Enter your password again and press [ENTER]: "
stty -echo
read password
stty echo

secret="$(openssl rand -base64 50)"


touch core/local_settings.py
echo "SECRET_KEY = '$secret'
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': '$db_name',
        'USER': '$USER',
        'PASSWORD': '$password',
    }
}" > core/local_settings.py

source env/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate