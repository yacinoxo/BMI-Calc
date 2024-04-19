from flask import Flask, request, render_template


app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def Home():
    #cheke do we have a POST request
    if request.method == "POST" and "userheight" in request.form and "userweight" in request.form:
        
        #define the weight and height varibles
        weight = int(request.form.get("userweight"))
        height = int(request.form.get("userheight"))

        #cheke do we have the value of weight and height
        if height and weight :
            bmi = round(weight / ((height / 100)**2), 2)
            return render_template('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><link rel="stylesheet" href="/static/styel.css"><title>BMI calculator</title></head><body><h1>BMI calculator</h1><br><p>Hi how is it going, I hope you are right.</p><form action="/" method="post"><label for="userheight">Height:</label><input type="text" name="userheight" placeholder="plz entre your Height in CM" required><br><br><label for="userweight">Weight:</label><input type="text" name="userweight" placeholder="plz entre your Weight in KG" required*><br><br><br><button type="submit">Calculate</button></form><br><div>{% if bmi %}<p>Your BMI is <i style="color: goldenrod">{{ bmi }}</i> <b style="color: red">kg/m²</b></p>{% endif %}</div></body></html>', bmi = bmi)
    return render_template("index.html")
    



app.run()
