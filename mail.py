import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
import json
from jinja2 import Template

# Configure logging
logging.basicConfig(filename='email_sender.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def send_emails(from_addr, email, password, subject, template_path, data_path, email_column, name_column, smtp_server='smtp.gmail.com', smtp_port=587):
    try:
        # Read email template from file
        with open(template_path, 'r') as template_file:
            template_content = template_file.read()
            email_template = Template(template_content)

        # Read recipient data from CSV
        data = pd.read_csv(data_path)
        to_addr = data[email_column].tolist()
        name = data[name_column].tolist()

        # Connect to SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as mail:
            mail.ehlo()
            mail.starttls()
            mail.login(email, password)

            # Iterate over recipients and send emails
            for i, recipient_email in enumerate(to_addr):
                msg = MIMEMultipart()
                msg['From'] = from_addr
                msg['To'] = recipient_email
                msg['Subject'] = subject

                # Render email content from template
                rendered_content = email_template.render(name=name[i])
                msg.attach(MIMEText(rendered_content, 'plain'))

                # Send email
                mail.sendmail(from_addr, recipient_email, msg.as_string())
                logging.info(f"Email sent to {recipient_email}")
                print(f"Email sent to {recipient_email}")

        print("All emails sent successfully.")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        print(f"An error occurred: {str(e)}")

# Load configuration from file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Example usage:
send_emails(
    config['from_addr'], 
    config['email'], 
    config['password'], 
    config['subject'], 
    'email_template.txt', 
    "recipient_data.csv", 
    config['email_column'], 
    config['name_column'], 
    config['smtp_server'], 
    config['smtp_port']
)
