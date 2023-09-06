import smtplib
from flask import Flask, render_template, request, redirect, flash
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app_code import pass_code, sec_key

app = Flask(__name__)
app.secret_key = sec_key  # Set a secret key for flash messages


@app.route("/")
def index():
    return render_template("email_form.html")


@app.route("/send_email", methods=["POST"])
def send_email():
    if request.method == "POST":
        email_sender = request.form["sender"]
        email_password = pass_code  # Replace with your password or input logic
        email_recipient = request.form["recipient"]
        subject = request.form["subject"]
        body = request.form["body"]

        # Create the email message
        message = MIMEMultipart()
        message["From"] = email_sender
        message["To"] = email_recipient
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        try:
            # Set up SMTP server and send message
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(email_sender, email_password)
                server.sendmail(email_sender, email_recipient, message.as_string())

            flash("Email sent successfully!", "success")
        except Exception as e:
            flash(f"An error occurred: {str(e)}", "error")

        return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
