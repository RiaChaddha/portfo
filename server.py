from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("./index.html")

def storedata(name, email, subject, message):
    try:
        with open("data.csv", "r"):
            pass
    except FileNotFoundError:
        with open("data.csv", "w", newline ="") as Fw:
            wobj = csv.writer(Fw)
            wobj.writerow(["name", "email", "subject", "message"])

    with open("data.csv", "a", newline ="") as Fw:
        wobj = csv.writer(Fw)
        wobj.writerow([name, email, subject, message])

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        newsub = "***" + str(subject) + "***"
        message = request.form.get("message")

        storedata(name, email, newsub, message)

    else:
        return "Form not submitted"

    return render_template("./thankyou.html")