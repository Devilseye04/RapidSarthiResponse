from flask import Flask, render_template,request,redirect,url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact_infomation.sqlite3'
app.config['SECRET_KEY'] = "pleasebesafe"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class contact_info(db.Model):
    id = db.Column('contact_id', db.Integer, primary_key = True)
    city = db.Column(db.String(50),nullable=False)
    name = db.Column(db.String(200),nullable=False)
    ph_number = db.Column(db.String(20),nullable=False,unique=True)
    facility = db.Column(db.String(500),nullable=False)
    date = db.Column(db.DateTime,default=datetime.utcnow())
    report = db.Column(db.Integer,default=1)
    fraud = db.Column(db.Integer,default=1)

    def __repr__(self) -> str:
        return f"{self.city} - {self.date}"

@app.route('/',methods=['GET','POST'])
def home_page():
    if request.method=='POST':
       pass
    
    allContacts = contact_info.query.all()
    print(allContacts) 
    return render_template('index.html', allContacts=allContacts)

       



@app.route('/report/<int:sno>')
def report_number(sno):
    contact = contact_info.query.filter_by(id=sno).first()
    print(contact.city,contact.ph_number,contact.report)
    if contact.report == 5:
        db.session.delete(contact)
        db.session.commit()
    else:
        contact.report = contact.report+1
        db.session.add(contact)
        db.session.commit()
    return redirect("/")

@app.route('/fraud/<int:sno>')
def fraud_number(sno):
    contact = contact_info.query.filter_by(id=sno).first()
    print(contact.city,contact.ph_number,contact.report)
    if contact.report == 1  :
        db.session.delete(contact)
        db.session.commit()
    else:
        contact.fruad = contact.fraud+1
        db.session.add(contact)
        db.session.commit()
    return redirect("/")

@app.route('/addPhoneNumber',methods=['GET','POST'])
def filter():
    if request.method == 'POST':
        try:
            city = request.form['city']
            name = request.form['nameofperson']
            ph_number = str(int(request.form['ph_number']))
            facility = request.form['facility']
            contact = contact_info(city=city,name=name, ph_number=ph_number,facility=facility)
            db.session.add(contact)
            db.session.commit()
            c = request.json
        except Exception as e:
            print(e)
            return redirect('/')
    
    return redirect('/')
    
if __name__ == '__main__':
   app.run(debug=True)