from flask import Flask, make_response, jsonify, request
from flask_mysqldb import MySQL
from flask_restful import Api, Resource, reqparse
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

app = Flask(__name__)
app.config["SECRET_KEY"] = "super-secret" # Secret Key for JWT
api = Api(app)

# Main Config of Database
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "111004"  
app.config["MYSQL_DB"] = "ivernstudios"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

# All Functions

class User(object):
    def __init__(self, id):
        self.id = id
    
    @classmethod
    def find_by_username(cls, username):
        if username == "admin":
            return cls(id=1)

def authentication(username, password):
    user = User.find_by_username(username)
    if user and safe_str_cmp(password.encode("utf-8"), "password".encode("utf-8")):
        return user

def identity(payload):
    user_id = payload["identity"]
    return User.find_by_id(user_id)



# MAIN
class Index(Resource):
    def get(self):
        return {
            "message": "Welcome to the Ivern Studios API!",
            "endpoints": {
                "View all companies": "/company",
                "View company by ID": "/company/<int:id>",
                "Add a new company": "/company",
                "Update company by ID": "/company/<int:id>",
                "Delete company by ID": "/company/<int:id>"
            }
        }



# Fetching Data from Database
def data_fetch(query):
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    return data

# Get Company Data Info
class Company(Resource):
    def get_company():
        data = data_fetch("""SELECT * FROM ivernstudios""")
        # JSON response return value
        return make_response(jsonify(data), 200)

# Get Company ID Info
class CompanyByID(Resource):
    def get(self, id):
        data = data_fetch("""SELECT * FROM ivernstudios WHERE id = {}""".format(id))
        # JSON response return value
        return make_response(jsonify(data), 200)


# Add Company Info
class AddCompany(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", required=True)
        parser.add_argument("age", type=int, required=True)
        parser.add_argument("position", required=True)
        info = parser.parse_args()

        name = info["name"]
        age = info["age"]
        position = info["position"]
        
        cur = mysql.connection.cursor()
        cur.execute(
            """INSERT INTO ivernstudios (name, age, position) VALUES (%s, %s, %s)""",
            (name, age, position),
        )
        mysql.connection.commit()
        cur.close()
        
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
        """UPDATE ivernstudios SET name = %s, age = %s, position = %s WHERE id = %s""",
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
    cur.execute("""DELETE FROM ivernstudios WHERE id = %s""", (id,))
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