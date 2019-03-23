from flask import Flask,render_template,request
import model

app = Flask(__name__)
model.init_db()

@app.route('/')
def home():
    todos=model.get_all_data()
    return render_template('home.html',todos=todos)

@app.route('/enternew')
def enternew():
   return render_template('form.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         Name = request.form['Name']
         Email = request.form['Email']
         Password = request.form['Password']
         Address = request.form['Address']
         City= request.form['City']
         State = request.form['State']
         Zip = request.form['Zip']
         formlist =[Name,Email,Password,Address,City,State,Zip]
         model.add_newform(formlist)
      except:
         pass
   return "database updated <a href='/'> Return to Homepage</a>"


if __name__=='__main__':
    app.run(debug = True)
