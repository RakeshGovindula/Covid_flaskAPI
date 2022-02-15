from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, extract

database_name = 'Covid_database.db'# database created by Cleaning_and_creating_db.py file

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

mydb = SQLAlchemy(app)


class first(mydb.Model):#For storing the database data into the class for querying.
    __tablename__ = 'Covid_database'
    SNo = mydb.Column(mydb.Integer, primary_key=True)
    ObservationDate = mydb.Column(mydb.Date)
    State = mydb.Column(mydb.String)
    Country = mydb.Column(mydb.String)
    LastUpdate = mydb.Column(mydb.String)
    Confirmed = mydb.Column(mydb.Integer)
    Deaths = mydb.Column(mydb.Integer)
    Recovered = mydb.Column(mydb.Integer)


@app.route('/')
def welcome_page():# The Welcome Page that is appeared when opening it.
    return "Welcome to HomePage. Query Results based on Country name and MMYYYY after entering as /covid/"


@app.route('/covid/<country>/<ym>', methods=["GET"])
def ok(country, ym):
    try:
        res = first.query.filter(func.lower(first.Country) == str.lower(country), #works for different entries of country names
                                   extract('year', first.ObservationDate) == int( #Extracting and querying the year and month
                                       ym[-4:]),# The last 4 digits are the year.
                                   extract('month', first.ObservationDate) == int(
                                       ym[0:2])# The first 2 digits are the month for that year.
                                   ).all()
        if res:
            return render_template('index.html', res=res)# Passing the resultant queried data to the html.
        else:
            return "Please Search with only the available data"

    except Exception as e: # Exceptiom if something wrong happens
        error_info = "<p>There is an error:<br>" + str(e) + "</p>"
        info = '<h1>Sorry,Something is wrong</h1>'
        return info + error_info


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
