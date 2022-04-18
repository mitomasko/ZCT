import random
import pyodbc
import json
import ast

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from custom_function import getClass, render_html

app = Flask(__name__)

######## Database config vars ############
usr_name = "allpain@zct-mysercver"
pwd = "Nogain20"
srv = "zct-mysercver.postgres.database.azure.com"
db_name = "postgres"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://{}:{}@{}/{}".format(usr_name, pwd, srv, db_name)

db = SQLAlchemy(app)

class datasets(db.Model):
    temperature = db.Column(db.String(50), primary_key=True)
    luminosity = db.Column(db.String(50))
    radius = db.Column(db.String(50))
    absolute_magnitude = db.Column(db.String(5))
    star_color = db.Column(db.String(50))
    spectral_class = db.Column(db.String(50))
    star_type = db.Column(db.String(50))


######## Rest API Config vars ############
url = 'https://ussouthcentral.services.azureml.net/workspaces/c5dc545e40b0400a990968fdc1a99944/services/4c26352fbfbb4a08b9e46e79f2fc6fe3/execute?api-version=2.0&format=swagger'
api_key = 'nkzI00LQ0Xd6heWf9A+N+z3YfWb2yTPJRDUCd/pshQvr6Ld969+2M5yW55ZtXHoW2e2G0rcenRKV1f6YpR0peQ==' 
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}


@app.route('/')
def main():
    return render_template("main.html", pred_history=datasets.query.all())


@app.route('/get_data', methods=['POST', 'GET'])
def get_prediction():

    if (request.method == 'POST'):
        data = {
            "Inputs": {
                "input1":
                [
                    {
                    'Temperature (K)': request.form['temperature'],   
                    'Luminosity(L/Lo)': request.form['luminosity'],   
                    'Radius(R/Ro)': request.form['radius'],   
                    'Absolute magnitude(Mv)': request.form['absolute-magnitude'],   
                    'Star type': request.form['star-type'],   
                    'Star color': request.form['color'],   
                    }
                ],
            },
            "GlobalParameters":  {}
        }

        body = str.encode(json.dumps(data))

        req = urllib2.Request(url, body, headers)
        
        try:
            response = urllib2.urlopen(req)
            spec_class, acc = getClass(response.read())

            print("Predicted class: {} with {} accurency".format(spec_class, acc))

            # sending data to database
            temperature = request.form['temperature']
            luminosity =request.form['luminosity']
            radius = request.form['radius']
            absolute_magnitude =request.form['absolute-magnitude']
            star_color = request.form['color']
            spectral_class = spec_class
            star_type = request.form['star-type']

            ds = datasets(temperature=temperature, luminosity=luminosity, radius=radius, absolute_magnitude=absolute_magnitude, star_color=star_color, spectral_class=spectral_class, star_type=star_type)

            db.session.add(ds)
            db.session.commit()

            return render_template(render_html(spec_class), acc=(acc*100))
        except:
            return render_template("bad_response.html")


if __name__ == "__main__":
    app.run()