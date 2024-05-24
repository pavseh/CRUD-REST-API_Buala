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

# Get Company Data Info
@app.route("/company", methods=["GET"])
def get_company():
    data = data_fetch("""SELECT * FROM company""")
    # JSON response return value
    return make_response(jsonify(data), 200)

# Get Company ID Info
@app.route("/company/<int:id>", methods=["GET"])
def get_company_by_id(id):
    data = data_fetch("""SELECT * FROM company WHERE id = {}""".format(id))
    # JSON response return
    return make_response(jsonify(data), 200)

# Add Company Info
@app.route("/company", methods=["POST"])
def add_company():

    # Extract Company Data
    info = request.get_json()
    name = info.get("name")
    age = info.get("age")
    position = info.get("position")
    
    # Insert New Company Data
    cur = mysql.connection.cursor()
    cur.execute(
        """INSERT INTO company (name, age, position) VALUES (%s, %s, %s)""",
        (name, age, position),
    )
    mysql.connection.commit()
    cur.close()
    
    # Return Value if company added
    return make_response(
        jsonify({"message": "company added successfully", "name": name, "age": age, "position": position}),
        201,
    )


# Update Company Info
@app.route("/company/<int:id>", methods=["PUT"])
def update_company(id):

    # Extract Updated Company Data
    info = request.get_json()
    name = info.get("name")
    age = info.get("age")
    position = info.get("position")
    
    # Update Company Data
    cur = mysql.connection.cursor()
    cur.execute(
        """UPDATE company SET name = %s, age = %s, position = %s WHERE id = %s""",
        (name, age, position, id),
    )
    mysql.connection.commit()
    cur.close()
    
    # Return Value if company updated
    return make_response(
        jsonify({"message": "company updated successfully", "id": id, "name": name, "age": age, "position": position}),
        200,
    )


# Delete Company
@app.route("/company/<int:id>", methods=["DELETE"])
def delete_company(id):

    # Delete Company Data
    cur = mysql.connection.cursor()
    cur.execute("""DELETE FROM company WHERE id = %s""", (id,))
    mysql.connection.commit()
    cur.close()
    
    # Return value if company data deleted
    return make_response(
        jsonify({"message": "company deleted successfully", "id": id}),
        200,
    )

# Flask App
if __name__ == "__main__":
    app.run(debug=True)