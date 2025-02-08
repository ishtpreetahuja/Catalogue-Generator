import imaplib
import email
from email.header import decode_header
from dotenv import load_dotenv
import os
from src.pdf_gen import generator
from src.sync_local import syncing

# Load environment variables from .env file
load_dotenv(dotenv_path="utils/.env")

# Email account credentials
EMAIL = os.getenv("RECEIVER-EMAIL")
PASSWORD = os.getenv("RECEIVER-PASSWORD")
IMAP_SERVER = "imap.gmail.com"
IMAP_PORT = 993

def check_email():
    print("Checking for new emails...")  # Added print statement
    # Connect to the email server
    mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    try:
        mail.login(EMAIL, PASSWORD)
        print("Login successful")
    except imaplib.IMAP4.error as e:
        print(f"Login failed: {e}")
        return

    mail.select("inbox")

    # Search for unread emails with subject "Send catalogue" (case insensitive)
    result, data = mail.search(None, '(UNSEEN SUBJECT "Send catalogue" SUBJECT "send catalogue" SUBJECT "SEND CATALOGUE")')
    if result == "OK":
        mail_ids = data[0].split()
        print(f"Found {len(mail_ids)} new emails with subject 'Send catalogue'")

        for num in mail_ids:
            # Fetch the email
            result, msg_data = mail.fetch(num, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    # Parse email content
                    msg = email.message_from_bytes(response_part[1])
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding or "utf-8")
                    print(f"Email subject: {subject}")

                    # Extract email body
                    if msg.is_multipart():
                        for part in msg.walk():
                            if part.get_content_type() == "text/plain":
                                body = part.get_payload(decode=True).decode()
                                break
                    else:
                        body = msg.get_payload(decode=True).decode()

                    # Generate PDF and get the path
                    pdf_path = generator(body, msg["From"], f"REPLY TO {body}")

                    # Mark the email as read
                    mail.store(num, '+FLAGS', '\\Seen')

    # Search for unread emails with subject "sync" (case insensitive)
    result, data = mail.search(None, '(UNSEEN SUBJECT "sync" SUBJECT "Sync" SUBJECT "SYNC")')
    if result == "OK":
        mail_ids = data[0].split()
        print(f"Found {len(mail_ids)} new emails with subject 'sync'")

        for num in mail_ids:
            # Fetch the email
            result, msg_data = mail.fetch(num, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    # Parse email content
                    msg = email.message_from_bytes(response_part[1])
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding or "utf-8")
                    print(f"Email subject: {subject}")

                    # Trigger syncing function
                    syncing()

                    # Mark the email as read
                    mail.store(num, '+FLAGS', '\\Seen')

    mail.logout()