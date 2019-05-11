cd /bee_dictionary/git/bee-dictionary-backend
source venv/bin/activation
python init_server

# Import oxford
python dictionary_crawler/transform/transform_oxford_to_redis.py

# Install and run web
## start docker-compose
## create database postgres

psql -U postgres
create database bee_dictionary;

cd /bee_dictionary/git/bee-dictionary-backend
python bee_dictionary_api/manage.py makemigrations
python bee_dictionary_api/manage.py migrate
python bee_dictionary_api/manage.py runserver 0.0.0.0:8000