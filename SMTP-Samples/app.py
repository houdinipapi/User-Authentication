import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template, request
from app_code import pass_code

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('email_form.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        email = request.form['email']
        message = request.form['message']

        # Email server configuration (using Gmail as an example)
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = 'olivertim.ot@gmail.com'  # Replace with your email
        smtp_password = pass_code  # Replace with your email password

        # Create an email message
        msg = MIMEMultipart()
        msg['From'] = smtp_username
        msg['To'] = smtp_username  # Send the email to yourself
        msg['Subject'] = 'User Message'
        msg.attach(MIMEText(f'User Email: {email}\n\nUser Message:\n{message}', 'plain'))

        try:
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.sendmail(smtp_username, smtp_username, msg.as_string())

            return "Email sent successfully."
        except Exception as e:
            return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)

