from flask import Flask, request, render_template_string

app = Flask(_name_)

@app.route("/")
def home():
    return "site çalışıyor"

@app.route("/admin", methods=["GET","POST"])
def admin():
    if request.method=="POST":
        if request.form.get("username")=="admin" and request.form.get("password")=="1234":
            return "LOGIN OK"

    return render_template_string("""
    <form method="post">
    <input name="username">
    <input name="password" type="password">
    <button>login</button>
    </form>
    """)

app.run()