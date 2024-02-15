from flask import Flask, render_template, request, redirect, url_for
import pyodbc

app = Flask(__name__)

# Database connection parameters
server = 'LAPTOP-5GSQ9Q8I\SQLEXPRESS'
database = 'PythonFlaskAngularTest'

# Function to establish database connection
def connect_to_database():
    return pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Extracting form data
    name = request.form['name']
    age = request.form['age']
    grade = request.form['grade']

    # Inserting data into the database
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    connection.commit()
    cursor.close()
    connection.close()

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
