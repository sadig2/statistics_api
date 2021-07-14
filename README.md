# create environment

    python3 -m venv env
# activate environment
    source env/bin/activate
    source .env
# install dependencies
    pip install -r requirements.txt

# run application
    ./manage.py runserver

# create dummy data 

    python3 populate -n {numer_of_users} -m {number of posts per user}

# run test
    ./manage.py test api.tests

