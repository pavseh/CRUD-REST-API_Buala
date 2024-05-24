from flask import Flask, make_response, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Main Config of Database
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "studio123456"  
app.config["MYSQL_DB"] = "ivernstudios"

app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

# All Functions

# Fetching Data from Database
def data_fetch(query):
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    return data