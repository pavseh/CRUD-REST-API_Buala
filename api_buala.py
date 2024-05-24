from flask import Flask, jsonify, request, make_response
from flask_mysqldb import MySQL
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import hmac

app = Flask(__name__)
app.config["SECRET_KEY"] = "super-secret"  # Secret key for JWT
api = Api(app)

# Main Config of Database
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "111004"  
app.config["MYSQL_DB"] = "ivernstudios"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

# Initialize JWT Manager
jwt = JWTManager(app)

# User class
class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        result = cur.fetchone()
        cur.close()
        if result:
            return cls(id=result['id'], username=result['username'], password=result['password'])
        return None

    @classmethod
    def find_by_id(cls, id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE id = %s", (id,))
        result = cur.fetchone()
        cur.close()
        if result:
            return cls(id=result['id'], username=result['username'], password=result['password'])
        return None

# Authentication endpoint
@app.route('/auth', methods=['POST'])
def auth():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    user = User.find_by_username(username)
    if user and hmac.compare_digest(user.password, password):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Bad username or password"}), 401

# All Functions

# Testing
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
    def get(self):
        data = data_fetch("""SELECT * FROM ivernstudios""")
        return make_response(jsonify(data), 200)

# Get Company ID Info
class CompanyByID(Resource):
    def get(self, id):
        data = data_fetch("""SELECT * FROM ivernstudios WHERE id = {}""".format(id))
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
class UpdateCompany(Resource):
    @jwt_required()
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("age", type=int)
        parser.add_argument("position")
        info = parser.parse_args()

        name = info["name"]
        age = info["age"]
        position = info["position"]
        
        cur = mysql.connection.cursor()
        cur.execute(
            """UPDATE ivernstudios SET name = %s, age = %s, position = %s WHERE id = %s""",
            (name, age, position, id),
        )
        mysql.connection.commit()
        cur.close()
        
        return make_response(
            jsonify({"message": "company updated successfully", "id": id, "name": name, "age": age, "position": position}),
            200,
        )

# Delete Company
class DeleteCompany(Resource):
    @jwt_required()
    def delete(self, id):
        cur = mysql.connection.cursor()
        cur.execute("""DELETE FROM ivernstudios WHERE id = %s""", (id,))
        mysql.connection.commit()
        cur.close()
        
        return make_response(
            jsonify({"message": "company deleted successfully", "id": id}),
            200,
        )

# Resource routing
api.add_resource(Index, "/")
api.add_resource(Company, "/company")
api.add_resource(CompanyByID, "/company/<int:id>")
api.add_resource(AddCompany, "/company")
api.add_resource(UpdateCompany, "/company/<int:id>")
api.add_resource(DeleteCompany, "/company/<int:id>")

# Flask App
if __name__ == "__main__":
    app.run(debug=True)
