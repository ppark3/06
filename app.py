from flask import Flask, render_template, request

my_app = Flask(__name__)

@my_app.route('/')
def root():
	return render_template("base.html")
	
@my_app.route('/echo', methods=["POST","GET"])
def echo():
	print request
	print request.method
	print request.headers
	print request.form["user"]
	username = request.form["user"]
	methodd = request.method
	return render_template("echo.html", user=username, method=methodd)
	
if __name__ == '__main__':
	my_app.debug == True
	my_app.run()