from flask import Flask , render_template,request
import sqlite3
app=Flask(__name__)
def database():
	ket_noi=sqlite3.connect("dangky.db")
	ghi=ket_noi.cursor()
	ghi.execute("""CREATE TABLE IF NOT EXISTS dang_ky (
	id INTEGER PRIMARY KEY AUTOINCREMENT , username TEXT UNIQUE ,password TEXT)""")
	ket_noi.commit()
	ket_noi.close()
database()
@app.route("/",methods=["GET","POST"])
def trang_chu():
	return render_template("trangchu.html")
@app.route("/dang_ky",methods=["GET","POST"])
def trang_chu_dang_ky():
	if request.method=="POST":
		username=request.form.get("ten")
		password=request.form.get("mk")
		confirm_password=request.form.get("xac_nhan_mat_khau")
		if confirm_password != password:
			loi_xac_nhan="Mật khẩu xác nhận không giống với mật khẩu bạn đã nhập trước đó"
			return render_template("dangky.html",loi_xac_nhan=loi_xac_nhan)
		try:
			ket_noi=sqlite3.connect("dangky.db",timeout=15)
			ghi=ket_noi.cursor()
			ghi.execute("INSERT INTO dang_ky (username,password) VALUES (?,?)",(username,password))
			ket_noi.commit()
			thanh_cong="Bạn đã đăng ký thành công , bạn có thể đăng nhập ở phía dưới để truy cập trang web"
			return render_template("dangnhap.html",thanh_cong=thanh_cong)
		except sqlite3.IntegrityError:
			that_bai="Tên tài khoản bạn nhập đã có người khác sử dụng "
			return render_template("dangky.html",that_bai=that_bai)
		finally :
			ket_noi.close()
	return render_template("dangky.html")
@app.route("/dang_nhap",methods=["GET","POST"])
def dang_nhap():
	return render_template("dangnhap.html")
if __name__==("__main__"):
	app.run()