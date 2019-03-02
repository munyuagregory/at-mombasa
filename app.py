from flask import Flask
app = Flask(__name__)

@app . route('/')
def index():
	return '<h1>Hello Mombasa!!</h1>'

@app.route('/bamburi')
def bamburi():
	return '<h1>We are now in Bamburi!!</h1>'

@app.route('/town/<name>')
def town(name):
	return'<h1>I am in {town} </h1>'
"""
latiname =''
if latiname[-1]== 'y':
	latiname = latin_name[:-1]+'iful'
else:
	latiname = latin_name +'y'
 return f'My latin name is {latiname}</h1>'"""
if __name__=='__main__':
	app.run()

