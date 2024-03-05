from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# MySQL connection parameters
MYSQL_HOST = '172.17.0.2'
MYSQL_USER = 'shivam'
MYSQL_PASSWORD = 'redhat'
MYSQL_DATABASE = 'user'  # Replace with your database name

@app.route('/api/user', methods=['POST'])
def add_user():
    username = request.json.get('username')

    if not username:
        return jsonify({'error': 'Username is required'}), 400

    # Establish MySQL connection
    connection = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )

    cursor = connection.cursor()

    # Insert username into the database
    insert_query = "INSERT INTO users (username) VALUES (%s)"
    cursor.execute(insert_query, (username,))
    connection.commit()

    # Close cursor and connection
    cursor.close()
    connection.close()

    return jsonify({'message': f'Hello, {username}! Your username has been added to the database.'})

@app.route('/api/users', methods=['GET'])
def get_users():
    # Establish MySQL connection
    connection = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )

    cursor = connection.cursor(dictionary=True)

    # Fetch all users from the database
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    # Close cursor and connection
    cursor.close()
    connection.close()

    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=83)
