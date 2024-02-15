# Auto Mailing Script

## Description
Auto Mailing is a Python script designed to simplify sending bulk emails to a wide audience. It automates the repetitive task of composing and sending individual emails by leveraging data from a CSV file and a customizable email template. Whether you're managing marketing campaigns, disseminating announcements, or distributing newsletters, this tool enhances efficiency, saving valuable time and resources.

## Requirements
- Python 3.x Installation
- Python Module Dependencies: Check and install the required Python modules specified in the `requirements.txt` file using the provided command.

## How to Run
### Configuration Setup:
Before executing the script, configure the parameters according to your requirements:
- Sender's Email Address (`from_addr`): Update this variable with the email address you intend to use as the sender.
- Email Credentials (`email` and `password`): Provide the necessary credentials for accessing the sender's email account.
- Email Template (`template_path`): Customize this variable to point to the location of your email template file. The script utilizes this template to compose the emails.
- Recipient Data (`data_path`): Specify the path to your CSV file containing recipient information, including email addresses and other relevant details.
- Column Names (`email_column` and `name_column`): Adjust these variables to match the column names in your CSV file corresponding to email addresses and recipient names.
- SMTP Server Settings (`smtp_server` and `smtp_port`): Customize these variables to align with the SMTP server details provided by your email service provider.
Upon execution, the script will read the CSV file, connect with the SMTP server, and dispatch personalized emails to the specified recipients using the configured email template.

### Monitoring:
The script maintains a log of its activities in a file named `email_sender.log`, residing in the same directory as the script. You can monitor this file to track successful email dispatches and any encountered errors.

## Author
This script was crafted by [Tirtho Roy](https://github.com/tirtho149). Don't hesitate to contact the author for inquiries, feedback, or contributions.

