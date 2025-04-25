from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    
   
    return "<h3>Hello, welcome to my cloud space!</h3>"

@app.route('/reg')
def reg():
    return "<h1>This is our registration page</h1>"

@app.route('/aboutus')
def aboutsu():
    name="Mrs Akinfolaju"
    email="peju@yahoo.com"
    return render_template('aboutus.html', name=name,email=email)

@app.route('/services')
def services(): 
    service1="Web Design"
    service2="Cloud Computing"
    service3="Software Development"
    service4="Data Science"
    return render_template('service.html',service1=service1,service2=service2,service3=service3,service4=service4)
   
@app.route("/contact")
def contact ():
    email="feyithonia@gmail.com"
    phone="080966753"
    return "Our Contact details are " + email + " , " + phone






if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)