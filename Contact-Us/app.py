from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("contact.html")


@app.route("/contact", methods=["POST"])
def contact():
    if request.method == "POST":
        # Process the contact form data here
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        # Redirect to a thank-you page or display a confirmation message
        return render_template("thankyou.html")


if __name__ == "__main__":
    app.run(debug=True)
