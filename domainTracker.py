import whois
import time
import os
import sys

def check_domain_availability(domain):
    try:
        w = whois.whois(domain)
        if w.status == None:
            return True
        else:
            return False
    except whois.parser.PywhoisError:
        return True

def monitor_domain_availability(domain):
    while True:
        if check_domain_availability(domain):
            message = f"The domain {domain} is now available for purchase!"
            print(message)
            # add logic for notifiaction mechanism (twilio ++)
            break
        else:
            print("Domain is still unavailable. Checking again in 1 hour...")
            time.sleep(3600)  # Check every hour

# Usage example
monitor_domain_availability("qxtaiba.com")
