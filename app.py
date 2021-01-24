from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    data = {
        "name": "thongchai",
        "age": 30,
        "salary": 5000
    }
    return render_template("index.html", mydata=data)
    # return "<h1>Hello Flask Framework</h1>"


@app.route("/about")
def about():
    product = ["เสื้อผ้า", "เตารีด", "ผ้าห่ม","ยาสระผม"]
    return render_template("about.html",myproduct=product)


@app.route("/admin")
def admin():
    # ชื่อ
    name = "Thongchai"
    age = 28
    username = "thongchai"
    return render_template("admin.html", myname=name, age=age, username=username)


@app.route("/user/<name>/<age>")
def member(name, age):
    return "<h1>สวัสดีสมาชิก : {} , อายุ : {} ปี</h1>".format(name, age)


if __name__ == "__main__":
    # app.run()
    app.run(debug=True)  # open debug mode
