from flask import Flask
from connection import db
from models import Student
from flask import render_template
from flask import request, redirect, url_for
import os
from dotenv import load_dotenv
load_dotenv()

from sqlalchemy.engine import URL
from sqlalchemy import create_engine
import MySQLdb

app = Flask(__name__)

# url_object = URL.create(
#     "mysql+mysqldb",
#     host=os.getenv("DATABASE_HOST"),
#     user=os.getenv("DATABASE_USERNAME"),
#     password=os.getenv("DATABASE_PASSWORD"),
#     database=os.getenv("DATABASE"),
#     # autocommit=True,
#     # ssl_mode="VERIFY_IDENTITY",
# )

# # PyMySQL
# engine = create_engine(
#     url_object,
#     connect_args={
#         "ssl": {
#             "ssl_ca": "/etc/ssl/cert.pem"
#         }
#     }
# )

# engine = create_engine(
#     # "mysql+mysqldb://scott:tiger@192.168.0.134/test",
#     # url_object,
#     connect_args={
#         "ssl": {
#             "ssl_ca": "/home/gord/client-ssl/ca.pem",
#             "cert": "/home/gord/client-ssl/client-cert.pem",
#             "key": "/home/gord/client-ssl/client-key.pem"
#         }
#     }
# )

# connection_uri = (
#     "mysql+pymysql://scott:tiger@192.168.0.134/test"
#     "?ssl_ca=/home/gord/client-ssl/ca.pem"
#     "&ssl_cert=/home/gord/client-ssl/client-cert.pem"
#     "&ssl_key=/home/gord/client-ssl/client-key.pem"
#     "&ssl_check_hostname=false"
# )

# app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://username:password@host:port/database_name'
# SQLALCHEMY_DATABASE_URI_KEY = os.environ.get("SQLALCHEMY_DATABASE_URI_KEY")
# app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI_KEY 
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URI,
#     autocommit = True,
#     ssl_mode = "VERIFY_IDENTITY",
#     ssl = {
#         "ssl_ca": "/etc/ssl/cert.pem"
#     }
    
# )

# import ssl
# context = ssl.SSLContext()
# context.load_cert_chain(r"C:\Users\Shera\Documents\cert.pem", r"C:\Users\Shera\Documents\key.pem")

# connection = MySQLdb.connect(
#   host= os.getenv("DATABASE_HOST"),
#   user=os.getenv("DATABASE_USERNAME"),
#   passwd= os.getenv("DATABASE_PASSWORD"),
#   db= os.getenv("DATABASE"),
#   autocommit = True,
#   ssl_mode = "VERIFY_IDENTITY",
#   ssl      = {
#     "ca": "/etc/ssl/cert.pem"
#   }
# )

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///records.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# resp = request.get('https://student-records-396909.ew.r.appspot.com', verify=True, cert=['C:\Users\Shera\Downloads\cacert-2023-08-22.pem'])

# Home Page
@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)   

# Create new Student Record
@app.route('/new/', methods=('GET', 'POST'))
def newStudent():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        age = int(request.form['age'])
        bio = request.form['bio']
        student = Student(firstname=firstname,
                          lastname=lastname,
                          email=email,
                          age=age,
                          bio=bio)
        db.session.add(student)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('newStudent.html')

# ID Route
@app.route('/<int:student_id>/')
def student(student_id):
    student = Student.query.get_or_404(student_id)
    return render_template('student.html', student=student)

# Update Record
@app.route('/<int:student_id>/update/', methods=('GET', 'POST'))
def updateStudent(student_id):
    student = Student.query.get_or_404(student_id)

    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        age = int(request.form['age'])
        bio = request.form['bio']

        student.firstname = firstname
        student.lastname = lastname
        student.email = email
        student.age = age
        student.bio = bio

        db.session.add(student)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('updateStudent.html', student=student)

# Delete Record
@app.post('/<int:student_id>/delete/')
def delete(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True
    #ssl_context=(R'C:\Users\Shera\Documents\cert.pem', R'C:\Users\Shera\Documents\key.pem'),
    )
    # context = ('local.crt', 'local.key')#certificate and key files
    # app.run(debug=True)