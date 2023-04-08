from flask import Flask, render_template, request, redirect, url_for, session
import blockchain
import transaction
import user

app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.route("/")
def index():
    if "username" in session:
        return render_template("index.html", username=session["username"])
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user_id = user.login(username, password)
        if user_id is not None:
            session["user_id"] = user_id
            session["username"] = username
            return redirect(url_for("index"))
        else:
            error = "Invalid username or password"
    return render_template("login.html", error=error)

@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if user.register(username, password):
            return redirect(url_for("login"))
        else:
            error = "Username already taken"
    return render_template("register.html", error=error)

@app.route("/logout")
def logout():
    session.pop("user_id", None)
    session.pop("username", None)
    return redirect(url_for("login"))

@app.route("/send", methods=["GET", "POST"])
def send():
    error = None
    if request.method == "POST":
        sender = session["username"]
        recipient = request.form["recipient"]
        amount = int(request.form["amount"])
        if amount <= 0:
            error = "Invalid amount"
        elif amount > blockchain.get_balance(sender):
            error = "Insufficient balance"
        else:
            transaction.create(sender, recipient, amount)
            return redirect(url_for("index"))
    return render_template("send.html", error=error)

if __name__ == "__main__":
    app.run(debug=True)
