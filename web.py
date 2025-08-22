from flask import Flask , render_template,request
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def trang_chu():
	return render_template("trangchu.html")
if __name__==("__main__"):
	app.run()