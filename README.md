# Analytics engine instructions

Texto

# Prediction cron (smart feature) instructions

Run the following commands to install the required libraries:

```
pip install schedule
pip install SQLAlchemy
pip install databases
```

You will also need postgres running on the background for the app to work. If you want to adjust the code to run on other database you can edit the database.py file.

The postgres database name for default is sportpal_db, the username is postgres and the password 1234. To create the database you can do this:

```
psql -U postgres
postgres# CREATE DATABASE sportpal_db OWNER postgres;
postgres# ALTER USER postgres WITH PASSWORD '1234';
```

To launch the app go to the root folder and use:

```
python main.py
```
# How to run the analytics dashboard?

Run the app
```
uvicorn main:app --reload
```
Then, you should download the dashboard wich is inside the back's repository. After this, you have to input the server's details in order to connect with the postgre server. Once you have done this, the dashboard should run.
