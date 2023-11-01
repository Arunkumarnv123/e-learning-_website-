from flask import Flask, request,url_for,render_template,flash, redirect,session
from flask_sqlalchemy import SQLAlchemy
import bcrypt
import time as t
from random import randint
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stutech.db'
db = SQLAlchemy(app)
app.secret_key = 'secret_key'
mail = Mail (app)

app.config ['MAIL_SERVER']='smtp.gmail.com'
app.config ['MAIL_PORT'] = 465
app.config ['MAIL_USERNAME'] = 'arunkumarnv2002@gmail.com'
app.config ['MAIL_PASSWORD'] = 'bgxx ogic axfp ezfx'
app.config ['MAIL_USE_TLS'] = False
app.config ['MAIL_USE_SSL'] = True

mail = Mail (app)
#c_otp = randint(1000, 9999)
c_otp=4343
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)

    phone = db.Column(db.String(100))
    address = db.Column(db.String(100))
    role = db.Column(db.String())
    password = db.Column(db.String(200))

    def __init__(self,email,password, phone, address,name,role):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.password=password
        self.role=role

    def check_role(self):
        return self.role
    def check_password(self,pas):
        return pas==self.password


class Data(db.Model):
    __tablename__= "Data"
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), unique=True)
    content = db.Column(db.String(2000))
    instructor = db.Column(db.String(100))



    def __init__(self, name, instructor, content ):
        self.name = name
        self.instructor = instructor
        self.content = content

with app.app_context():
    db.create_all()


@app.route('/')
def index():

    return render_template('index.html')



@app.route('/validate',methods=['GET','POST'])
def validate():
    user_otp = request.form['otp']
    print(user_otp)
    if c_otp == int(user_otp):
        return redirect('/login')
    return render_template('register.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':

        name = request.form['name']
        gemail = request.form['email']


        phone =  request.form['phone']
        address =  request.form['address']
        password = request.form['password']
        role=request.form['role']

        new_user = User(name=name,email=gemail, phone=phone, address=address,password=password,role=role)

        msg = Message(' verification mail by Arun', sender='arunkumarnv2002@gmail.com', recipients=[gemail])
        msg.body = 'Hello this message has been sent to verifying your email ' + gemail + ' please enter the otp in webpage : ' + str(c_otp)
        mail.send(msg)
        print(c_otp)
        db.session.add(new_user)
        db.session.commit()
        print(c_otp)
        flash("OTP varied successfully ")
        return render_template('validate.html')



    return render_template('register.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        flash("OTP varied successfully ")

        user = User.query.filter_by(email=email).first()


        if user and user.check_password(password) and user.role=='student':
            session['email'] = user.email
            return render_template('main.html')
        elif user and user.check_password(password) and user.role=='teacher':
            session['email'] = user.email
            all_data = Data.query.all()
            print(all_data)
            return render_template('addc.html',course=all_data)
        else:

            flash("Wrong password or mailid" , 'warning')

            return render_template('login.html',error='Invalid user')

    return render_template('login.html')


@app.route('/main')
def base():
    return render_template('main.html')

@app.route('/addc')
def addcourse():
    all_data = Data.query.all()
    print(all_data)

    return render_template("addc.html", course=all_data)


@app.route('/dashboard')
def dashboard():

    user = User.query.filter_by(email=session['email']).first()
    return render_template('dashboard.html',user=user)

    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('email',None)
    return redirect('/login')

@app.route('/update', methods=['GET','POST'])
def update():

    if request.method == 'POST':
        my_data=User.query.get(request.form.get('id'))


        my_data.name=request.form['name']
        my_data.address=request.form['address']
        my_data.email=request.form['email']
        my_data.phone=request.form['phone']
        my_data.role=User.query.get(request.form.get('role'))
        my_data.password =User.query.get(request.form.get('password'))


        db.session.commit()

        flash(" updated Successfully")
    return render_template('main.html')
@app.route('/insert', methods=['POST'])
def insert():  # put application's code here

    if request.method == 'POST':

        name=request.form['name']

        content=request.form['email']
        instructor= request.form['phone']

        my_data=Data(name,content,instructor)

        db.session.add(my_data)

        db.session.commit()
        flash("Course inserted successfully ")
    return render_template('addc.html')


@app.route('/updatec', methods=['GET','POST'])
def updatec():

    if request.method == 'POST':
        my_data=Data.query.get(request.form.get('id'))


        my_data.name=request.form['name']

        my_data.instructor=request.form['instructor']
        my_data.content=request.form['phone']
        db.session.commit()

        flash("cousrse updated Successfully")
        return redirect(url_for('addcourse'))

@app.route('/delete/<id>', methods=['GET', "POST"])
def delete ( id ) :
    my_data=Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Course Deleted Successfully" )
    return redirect('/addc')




if __name__ == '__main__':
    app.run(debug=True)