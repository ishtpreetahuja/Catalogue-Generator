from src.email_trigger import check_email
import time

if __name__ == "__main__":
    while True:
        check_email()
        time.sleep(5)