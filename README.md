# flask-jewelry-app
## How to run flask

Virtual Envs

This command installs the module to allow you to create virtual environemts (needs to be done once on your computer) pip3 install virtualenv
Starting a project


setup your virtual env
virtualenv .env -p python3
source .env/bin/activate
a. virtualenv .env -p python3 - this sents up the environment with python3 b. source .env/bin/activate - this activates the environement So this is all that needs to be done if you already set up an environment


Start Python on the shell script
python3 app.py
set this up seperately from your postgres shell

c. Install module - pip3 install -r requirments.txt (requirments.txt is like package.json)

Starting from scratch?

mkdir flask-app
cd flask-app
virtualenv .env -p python3
source .env/bin/activate
Install your depenedencies
pip3 install flask-restful peewee flask psycopg2 flask_login flask_cors
Add them to requirements.txt - pip3 freeze > requirements.txt
Leaving a Virtual Env


Entering a file that has a virtual environment
# Setting up database-
source .env/bin/activate

# Type deactivate in the terminal window
source .env/bin/deactivate

## Setup your Sqlite3 in the terminal-
sqlite3 (data.db < c291.sql)

peewee - is our Norm (comparable to mongoose) gives us the power to talk to a sql database - LOOK AT THE DOCS!!!




