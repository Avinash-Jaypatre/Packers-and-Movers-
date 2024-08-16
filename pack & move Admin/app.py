from flask import Flask, render_template, request, redirect
from routes.common.connection import DbManager


app = Flask(__name__,static_url_path='/static')

@app.route("/", methods=["GET","POST"])
def Index_page():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        return redirect("/")

@app.route("/Homeservice", methods=["GET","POST"])
def Registred_users_page():
    data = []
    if request.method == "GET":
        db_manager = DbManager()
        connection,cursor = db_manager.getConnection()
        query = "select * from packersandmovers.homeservice"
        cursor.execute(query)
        records = cursor.fetchall()
        print(records)
        return render_template("Homeservice.html",data=records)
    
@app.route("/Homeservice", methods=["GET","POST"])
def Homeservice_page():
    if request.method == "GET":
        return render_template("Homeservice.html")
    elif request.method == "POST":
        return redirect("/")

@app.route("/Bikeservice", methods=["GET","POST"])
def Bikeservice():
    data = []
    if request.method == "GET":
        db_manager = DbManager()
        connection,cursor = db_manager.getConnection()
        query = "select * from packersandmovers.bikeservice"
        cursor.execute(query)
        records = cursor.fetchall()
        print(records)
        return render_template("Bikeservice.html",data=records)
     
@app.route("/Bikeservice", methods=["GET","POST"])
def Bikeservice_page():
    if request.method == "GET":
        return render_template("Bikeservice.html")
    elif request.method == "POST":
        return redirect("/")
    
@app.route("/Laggage", methods=["GET","POST"])
def Laggage():
    data = []
    if request.method == "GET":
        db_manager = DbManager()
        connection,cursor = db_manager.getConnection()
        query = "select * from packersandmovers.luggage"
        cursor.execute(query)
        records = cursor.fetchall()
        print(records)
        return render_template("Laggage.html",data=records)
     

    
@app.route("/Laggage", methods=["GET","POST"])
def Laggage_page():
    if request.method == "GET":
        return render_template("Laggage.html")
    elif request.method == "POST":
        return redirect("/")


@app.route("/signup", methods=["GET","POST"])
def signup():
    data = []
    if request.method == "GET":
        db_manager = DbManager()
        connection,cursor = db_manager.getConnection()
        query = "select * from packersandmovers.signup"
        cursor.execute(query)
        records = cursor.fetchall()
        print(records)
        return render_template("signup.html",data=records)
     
@app.route("/signup", methods=["GET","POST"])
def signup_page():
    if request.method == "GET":
        return render_template("signup.html")
    elif request.method == "POST":
        return redirect("/")

app.run(port=8000)