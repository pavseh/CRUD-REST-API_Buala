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

# Get Company Data
@app.route("/company", methods=["GET"])
def get_company():
    data = data_fetch("""SELECT * FROM company""")
    # JSON response return value
    return make_response(jsonify(data), 200)

# Get Company ID
@app.route("/company/<int:id>", methods=["GET"])
def get_company_by_id(id):
    data = data_fetch("""SELECT * FROM company WHERE id = {}""".format(id))
    # JSON response return
    return make_response(jsonify(data), 200)
