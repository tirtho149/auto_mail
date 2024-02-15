# auto_mail
# Automated Mailing

## 🛠️ Description
Automated Mailing is a Python script designed to streamline the process of sending bulk emails to a large audience. It automates the tedious task of individually composing and sending emails by leveraging data from a CSV file and a customizable email template. Whether you're sending marketing campaigns, announcements, or newsletters, this tool simplifies the process, saving time and effort.

## ⚙️ Requirements
To run the Automated Mailing script, ensure you have the following prerequisites:
- Python 3.x installed on your system.
- Required Python modules listed in `requirements.txt`. You can install them using the following command:

## 🌟 How to Run
### 1. Setup Configuration:
Before running the script, you need to set up the configuration parameters:
- **Sender's Email Address (`from_addr`)**: Update this variable with the email address from which you want to send the emails.
- **Email Credentials (`email` and `password`)**: Assign values to these variables with your email credentials.
- **Email Template (`template_path`)**: Customize this variable to point to your email template file. The script will use this template to compose the emails.
- **Recipient Data (`data_path`)**: Modify the `data_path` variable to specify the path to your CSV file containing recipient data, including email addresses and any other relevant information.
- **Column Names (`email_column` and `name_column`)**: Adjust these variables to match the column names in your CSV file corresponding to email addresses and recipient names.
- **SMTP Server Settings (`smtp_server` and `smtp_port`)**: Customize these variables to match your email provider's SMTP server address and port.

### 2. Running the Script:
Execute the script by running the following command in your terminal:
Upon execution, the script will read the CSV file, connect to the SMTP server, and send personalized emails to the specified recipients using the provided email template.

### 3. Monitoring:
The script logs its activity to a file named `email_sender.log`, located in the same directory as the script. You can monitor this file for information on successful email sends and any encountered errors.

## 🤖 Author
This script was authored by [Tirtho Roy](https://github.com/tirtho149). For any questions, feedback, or contributions, feel free to reach out to the author.

