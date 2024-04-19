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
            render_template("index.html", bmi = bmi)    
    return render_template("index.html")
    



app.run()
