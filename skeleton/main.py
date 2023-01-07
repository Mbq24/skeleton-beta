import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for

TOKEN = "figd_ASdlJUjKD8bjctapoAekHKm8MbucdvOTKNhx7Xbu"

load_dotenv()

app = Flask(__name__)
url = os.getenv("DATABASE_URL")
conn = psycopg2.connect(url)
# Create a cursor
# cursor = conn.cursor()
#
# # Execute a query
# cursor.execute("SELECT * FROM users")
#
# # Fetch the results
# results = cursor.fetchall()
#
# # Loop through the results
# for result in results:
#     print(result)

CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS user (id SERIAL PRIMARY KEY, first TEXT, last TEXT , phone INTEGER, email TEXT, capital REAL) """

INSERT_NEW_USER = "INSERT INTO user (first, last, phone, email, capital) VALUES (%s,%s,%s,%s,%s) RETURNING id"

@app.route('/', methods=['GET', 'POST'])
def landing():
    return render_template("opt-in.html")

    data = request.get_json()
    first = data['first']
    print(first)
@app.route('/create-acct', methods=['GET', 'POST'])
def create_acct():
    return render_template("create-account.html")


@app.route('/verify-acct', methods=['GET', 'POST'])
def verify_acct():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
