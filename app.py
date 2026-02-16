from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "site calisiyor"

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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port
