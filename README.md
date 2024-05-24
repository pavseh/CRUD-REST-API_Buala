# (CRUD REST API) Ivern Studios API Documentation

## Introduction
Welcome to the Ivern Studios API documentation! This API provides functionality to manage the studio company information with user authentication, built with Flask and MySQL.


## Installation

1. Create or Clone the Repository:
    ```bash
    git clone https://github.com/pavseh/CRUD-REST-API_Buala
    ```

2. Navigate to the project directory:
    ```bash
    cd BUALA-FINALS-NEW
    ```


3. Install all the required dependencies or libraries:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the MySQL database by executing the SQL Database I made for the program: `ivernstudios.sql`.

5. Make sure that all the configurations of the SQL Database is already set up.

```python
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "password"  # I used 111004
app.config["MYSQL_DB"] = "name" # I used ivernstudios
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
```

6. Setting up your MySQL database:
   
   - Open a MySQL database named `ivernstudios`.
   - Update the database connection settings in `api_buala.py` with your MySQL username, password, host, and name of the database.

7. Lastly, run the Flask App: (do not run the tester.py)
    ```bash
   python api_buala.py
   ```
   
8. The application should now be running locally. Access it in your browser or Postman at http://localhost:5000.


## Usage
1. Run the Flask App:
    ```bash
    python or py api_buala.py
    ```

2. The API will be accessible at `http://localhost:5000`.



### Other Usage
Once you have the app running, you can now do the following actions:

- Add an employee 
- View all employees
- Update/Remove existing employee/s
- Can view the employee in JSON/XML format (I used JSON for this one.)


## API Usage
I used **Postman** for the **CRUD or Create *(Post)*, Read *(Get)*, Update *(Put)*, Delete *(DELETE)*.**

- `POST /add_employee`: Create a new employee.
- `GET /employees`: View all employees.
- `PUT /update_employee`: Update an existing employee.
- `DELETE /delete_employee`: Delete an employee.



## Other Information

To authenticate, send a POST request to `/auth` with JSON containing `username` and `password`:

**With Postman**, you can go to the ***Auth Type > Bearer Token***, then paste the token for authorization (This applies to PUT/UPDATE and DELETE) of the program.

### Token
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNjUzNDA4NCwianRpIjoiZmMwZmNkZmUtY2U2OC00N2U4LWEwMzgtNWQ1MGU3MzM2ZTMyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNzE2NTM0MDg0LCJjc3JmIjoiNzVmYThhOWUtNTJlMi00M2YxLWJjYWMtZTJiZGNjZDk4NTRmIiwiZXhwIjoxNzE2NTM0OTg0fQ.oCFPq67v6dnOMLE2vDZgqKQSVldQsQeSp6OCnb4FIq8
```

### Security Information
```bash
Username: admin
Password: buala
```