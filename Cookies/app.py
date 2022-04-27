from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route('/set', methods = ['POST'])
def setcookie():
   if request.method == 'POST':
       user = request.form['name']
       resp = make_response('The Cookie has been Set')
       resp.set_cookie('UserID', user)
       return resp

@app.route('/get')
def getcookie():
    name = request.cookies.get('UserID')
    return f'<h1>Welcome {name}</h1>'

@app.route('/delete')
def deletecookie():
    resp = make_response('Cookie deleted!')
    resp.set_cookie('UserID', expires=0)
    return resp

if __name__ == '__main__':
    app.run(debug=True)
