from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    contactNumber = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self) -> str:
        return f"{self.firstName} {self.lastName} - {self.email} - {self.contactNumber} - {self.message}"


# This function creates the database tables
def create_tables():
    with app.app_context():
        db.create_all()

# Uncomment this line to create the tables
# create_tables()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        contactNumber= request.form['tel']
        message = request.form['message']
        new_contact = Contact(firstName=firstName, lastName=lastName, email=email, contactNumber=contactNumber, message=message)

        db.session.add(new_contact)
        db.session.commit()

        return render_template('success.html')

    return render_template('contact.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/feestructure')
def feestructure():
    return render_template('feestructure.html')


@app.route('/show')
def show():
    
    contact = Contact.query.all()
    return render_template('show.html', contact = contact)    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

