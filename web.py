from flask import Flask , render_template,request
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def trang_chu():
	return render_template("trangchu.html")
@app.route("/dang_nhap")
def trang_chu_dang_nhap():
	return render_template("dangnhap.html")
if __name__==("__main__"):
	app.run()