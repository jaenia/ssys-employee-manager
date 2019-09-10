# SSYS Employee Manager

![Screenshot](./screenshot.png)
A simple app and API for employee management.

## Installation
Clone the repository and run commands below:

```
# Create a virtual environment to isolate our package dependencies locally
$ python3 -m venv env
$ source env/bin/activate

# Install project dependencies
$ pip install -r requirements.txt

# Sync the database for the first time
$ python manage.py migrate

# Populating the database with initial employee data
$ python manage.py loaddata initial_data.json

# Create an initial user named admin
$ python manage.py createsuperuser --email admin@example.com --username admin
```

## API

The API uses token authentication. To obtain a token, you must submit a POST to `/api/login/` by submitting a JSON with the username and password of an existing user. Doing so will receive a token, which should be inserted into the Authorization header of the requests in the following format "Token {number}".


```
/api/login/
Allow: POST
Content-Type: application/json
Vary: Accept
```

```
/api/employees
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```

```
/api/employees/{employeeId}/
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```

### Example

```
GET /api/employees/
```
```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "name": "employee2",
            "email": "employee2@example.com",
            "department": "department2"
        },
    ]
}
```