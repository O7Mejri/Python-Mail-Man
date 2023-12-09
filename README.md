# Python Mail Man

## Prerequisites

1. **Gmail Account Setup:**
   - Enable "Less secure app access" for your Gmail account.
   - Create an [App Password](https://support.google.com/accounts/answer/185833?hl=en) for your Python application.

2. **Security Measures:**
   - Use SSL (Secure Sockets Layer) or TLS (Transport Layer Security) for secure email communication.
   - All the code files use SSL by default but can be changed to TLS depending on the case.

## Usage

   ```bash
   git clone https://github.com/O7Mejri/Python-Mail-Man.git
   cd Python-Mail-Man
   pip install -r requirements.txt
   ```

## Note:
Create a .env file in the project root and add the following lines:

   ```bash
   EMAIL=<your-email@gmail.com>
   PW=<your-app-password>
   ```

Add .env to your .gitignore file to avoid committing sensitive information.

## Update Code:

- Open send_email.py.
- Update the to_address, subject, and body variables with your desired values.
- Run the Script:

   ```bash 
   python send_email.py

