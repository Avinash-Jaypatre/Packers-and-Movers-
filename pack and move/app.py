from flask import Flask, render_template, request, redirect

from routes.common.connection import DbManager


app = Flask(__name__,static_url_path='/static')

@app.route("/", methods=["GET","POST"])
def home_page():
    data ={}
    if request.method == "GET":
        return render_template("Home.html",data =data,message ="")
    elif request.method == "POST":
        db_Manager = DbManager()
        connection,cursor = db_Manager.getConnection()
        data['username'] = request.form.get('username')
        data['Email'] = request.form.get('Email')
        data['Mobilenumber'] = request.form.get('Mobilenumber')
        data['relocationdate'] = request.form.get('relocationdate')
        data['movetype'] = request.form.get('movetype')
        data['movesize'] = request.form.get('movesize')
        data['relocationfrom'] = request.form.get('relocationfrom')
        data['relocationto'] = request.form.get('relocationto')
        data['mentionitem'] = request.form.get('mentionitem')

        try:
            query ="insert into packersandmovers.home(username, Email, Mobilenumber, relocationdate, movetype, movesize, relocationfrom, relocationto, mentionitem) values('"+str(data['username'])+"','"+str(data['Email'])+"','"+str(data['Mobilenumber'])+"','"+str(data['relocationdate'])+"','"+str(data['movetype'])+"','"+str(data['movesize'])+"','"+str(data['relocationfrom'])+"','"+str(data['relocationto'])+"','"+str(data['mentionitem'])+"')"
            cursor.execute(query)
            connection.commit()

        except Exception as error:
            print(error)
            return render_template("Home.html",data=data,message="Database error")


        return render_template("Home.html",data=data,message="Registration successfull.")
    
@app.route("/Aboutus", methods=["GET","POST"])
def Aboutus_page():
    if request.method == "GET":
        return render_template("About-us.html")
    elif request.method == "POST":
        return redirect("/")
    
@app.route("/constactus", methods=["GET","POST"])
def constactus_page():
    if request.method == "GET":
        return render_template("constactus.html")
    elif request.method == "POST":
        return redirect("/")
    
@app.route("/constactin", methods=["GET","POST"])
def constactin_page():
    if request.method == "GET":
        return render_template("contact-in.html")
    elif request.method == "POST":
        return redirect("/")
    
@app.route("/login", methods=["GET","POST"])
def Login_page():
    if request.method == "GET":
        return render_template("Login.html")
    elif request.method == "POST":
        return redirect("/")
    
@app.route("/signup", methods=["GET","POST"])
def sign_page():
    if request.method == "GET":
        return render_template("Sign-up.html")
    elif request.method == "POST":
        return redirect("/")
    
@app.route("/Homeservice", methods=["GET","POST"])
def Homeservice_page():
    data={}
    if request.method == "GET":
        return render_template("Homeservice.html",data =data,message ="")
    elif request.method == "POST":
        db_Manager = DbManager()
        connection,cursor = db_Manager.getConnection()
        data['username'] = request.form.get('username')
        data['Email'] = request.form.get('Email')
        data['Mobilenumber'] = request.form.get('Mobilenumber')
        data['relocationdate'] = request.form.get('relocationdate')
        data['movetype'] = request.form.get('movetype')
        data['movesize'] = request.form.get('movesize')
        data['relocationfrom'] = request.form.get('relocationfrom')
        data['relocationto'] = request.form.get('relocationto')
        data['mentionitem'] = request.form.get('mentionitem')

        try:
            query ="insert into packersandmovers.homeservice(username, Email, Mobilenumber, relocationdate, movetype, movesize, relocationfrom, relocationto, mentionitem) values('"+str(data['username'])+"','"+str(data['Email'])+"','"+str(data['Mobilenumber'])+"','"+str(data['relocationdate'])+"','"+str(data['movetype'])+"','"+str(data['movesize'])+"','"+str(data['relocationfrom'])+"','"+str(data['relocationto'])+"','"+str(data['mentionitem'])+"')"
            cursor.execute(query)
            connection.commit()

        except Exception as error:
            print(error)
            return render_template("Homeservice.html",data=data,message="Database error")


        return render_template("Homeservice.html",data=data,message="Registration successfull.")
    
    
@app.route("/biketransport", methods=["GET","POST"])
def biketransport_page():
    data={}
    if request.method == "GET":
        return render_template("biketransport.html",data =data,message ="")
    elif request.method == "POST":
        db_Manager = DbManager()
        connection,cursor = db_Manager.getConnection()
        data['username'] = request.form.get('username')
        data['Email'] = request.form.get('Email')
        data['Mobilenumber'] = request.form.get('Mobilenumber')
        data['relocationdate'] = request.form.get('relocationdate')
        data['movetype'] = request.form.get('movetype')
        data['movesize'] = request.form.get('movesize')
        data['relocationfrom'] = request.form.get('relocationfrom')
        data['relocationto'] = request.form.get('relocationto')
        data['mentionitem'] = request.form.get('mentionitem')

        try:
            query ="insert into packersandmovers.bikeservice(username, Email, Mobilenumber, relocationdate, movetype, movesize, relocationfrom, relocationto, mentionitem) values('"+str(data['username'])+"','"+str(data['Email'])+"','"+str(data['Mobilenumber'])+"','"+str(data['relocationdate'])+"','"+str(data['movetype'])+"','"+str(data['movesize'])+"','"+str(data['relocationfrom'])+"','"+str(data['relocationto'])+"','"+str(data['mentionitem'])+"')"
            cursor.execute(query)
            connection.commit()

        except Exception as error:
            print(error)
            return render_template("biketransport.html",data=data,message="Database error")


        return render_template("biketransport.html",data=data,message="Registration successfull.")
    
    
@app.route("/Luggage", methods=["GET","POST"])
def Luggage_page():
    data={}
    if request.method == "GET":
        return render_template("Luggage.html",data =data,message ="")
    elif request.method == "POST":
        db_Manager = DbManager()
        connection,cursor = db_Manager.getConnection()
        data['username'] = request.form.get('username')
        data['Email'] = request.form.get('Email')
        data['Mobilenumber'] = request.form.get('Mobilenumber')
        data['relocationdate'] = request.form.get('relocationdate')
        data['movetype'] = request.form.get('movetype')
        data['movesize'] = request.form.get('movesize')
        data['relocationfrom'] = request.form.get('relocationfrom')
        data['relocationto'] = request.form.get('relocationto')
        data['mentionitem'] = request.form.get('mentionitem')

        try:
            query ="insert into  packersandmovers.luggage(username, Email, Mobilenumber, relocationdate, movetype, movesize, relocationfrom, relocationto, mentionitem) values('"+str(data['username'])+"','"+str(data['Email'])+"','"+str(data['Mobilenumber'])+"','"+str(data['relocationdate'])+"','"+str(data['movetype'])+"','"+str(data['movesize'])+"','"+str(data['relocationfrom'])+"','"+str(data['relocationto'])+"','"+str(data['mentionitem'])+"')"
            cursor.execute(query)
            connection.commit()

        except Exception as error:
            print(error)
            return render_template("Luggage.html",data=data,message="Database error")


        return render_template("Luggage.html",data=data,message="Registration successfull.")

@app.route("/Signup", methods=["GET","POST"])
def signup_page():
    data={}
    if request.method == "GET":
        return render_template("Signup.html",data =data,message ="")
    elif request.method == "POST":
        db_Manager = DbManager()
        connection,cursor = db_Manager.getConnection()
        data['name'] = request.form.get('name')
        data['email'] = request.form.get('email')
        data['password'] = request.form.get('password')
        data['confirmPassword'] = request.form.get('confirmPassword')

        try:
            query ="insert into  packersandmovers.signup(name, email, password, confirmPassword) values('"+str(data['name'])+"','"+str(data['email'])+"','"+str(data['password'])+"','"+str(data['confirmPassword'])+"')"
            cursor.execute(query)
            connection.commit()

        except Exception as error:
            print(error)
            return render_template("Signup.html",data=data,message="Database error")
        
        return render_template("Signup.html",data=data,message="Registration successfull.")

   
app.run(port=8000)
    