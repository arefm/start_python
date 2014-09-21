from flask import Flask, render_template, request, url_for, redirect, session, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'the secret key goes here!'

def require_login(f):
	@wraps(f)
	def wrap(*arg, **kargs):
		if not 'loggedin' in session.keys():
			flash("not logged in")
			return redirect(url_for("Login"))
	return wrap

@app.route("/")
@require_login
def Home():
	# session['framework'] = "flask"
	# print redirect
	# for key in session:
	# 	print "Key: " + key
	# 	print "Value: " + session[key]

	return "Hello World!"

@app.route("/welcome/")
@require_login
def Welcome():
	message = None
	return render_template("welcome.html", message=message)

@app.route("/login/", methods=["GET", "POST"])
def Login():
	if 'loggedin' in session.keys():
		return redirect(url_for("Welcome"))

	message = None
	if request.method == "POST":
		message = "Logging in..."
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			message = "invalid credentials, please try again later"
		else:
			session['loggedin'] = True
			message = "welcome"
			return redirect(url_for('Welcome'))

	return render_template("login.html", message=message)

@app.route("/logout/")
@require_login
def Logout():
	session.pop("loggedin", None)
	return redirect(url_for("Login"));

if __name__ == '__main__':
	app.run(debug=True)