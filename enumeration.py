import requests 
import argparse
import time 
from termcolor import colored


parser = argparse.ArgumentParser()

# Add arguments for terminal
parser.add_argument("-m", help="enumeration mode", choices=["sub","dir"] )
parser.add_argument("-w",  help="wordlist (full path)" )
parser.add_argument("-d", help="domain name")
parser.add_argument("-t", type=int, help="time delay (seconds, default=3)", default=3)
parser.add_argument("-s", "--status", help="status code(default = 200,301,302)", default="200,301,302")
args = parser.parse_args()  

# Convert status codes to list 
codes = [int(code.strip()) for code in args.status.split(",")]

# Define header
headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.198 Safari/537.36"}

def dir_enum():
    
    # Open given wordlist and read 
    with open(args.w, "r") as file:
        directories = file.readlines()

    # Loop through each directory from the wordlist
    for directory in directories:
        directory = directory.strip()

        # Build the full URL from the given domain name and directory wordlist
        url = f"https://{args.d}/{directory}"

        # Send an HTTP get request to targeted url with custom header
        response = requests.get(url, headers=headers)

        # Check if the response status code is one of the codes we are interested in
        if response.status_code in codes:

            # If the response status code is 200 -> directory found
            if response.status_code == 200:
                print(f"[{colored('+', 'cyan')}] {colored(url, 'green')} [{response.status_code}]")
            # If the response status code is 301 or 302 -> redirecting
            elif response.status_code in [301,302]:
                print(f"[{colored('+', 'cyan')}] {colored(url, 'yellow')} [{response.status_code}]")
            # If the response status code is not 200,301,302 -> directory not found or server error
            else:
                print(f"[{colored('+', 'cyan')}] {colored(url, 'red')} [{response.status_code}]")
        else: 
            pass
        # Add time delay between each request
        time.sleep(args.t)

def sub_enum():
    
    # Open given wordlist and read
    with open(args.w, "r") as file:
        subdomains = file.readlines()

    # Loop through each directory from the wordlist
    for subdomain in subdomains:
        subdomain = subdomain.strip()

        # Build the full URL from the given domain name and directory wordlist
        url = f"https://{subdomain}.{args.d}"

        try:
            # Send an HTTP get request to targeted url with custom header
            response = requests.get(url, headers=headers)

            # Check if the response status code is one of the codes we are interested in
            if response.status_code in codes:
                # If the response status code is 200 -> directory found
                if response.status_code == 200:
                    print(f"[{colored('+', 'cyan')}] {colored(url, 'green')} [{response.status_code}]")
                # If the response status code is 301 or 302 -> redirecting
                elif response.status_code in [301,302]:
                    print(f"[{colored('+', 'cyan')}] {colored(url, 'yellow')} [{response.status_code}]")
                # If the response status code is not 200,301,302 -> directory not found or server error
                else:
                    print(f"[{colored('+', 'cyan')}] {colored(url, 'red')} [{response.status_code}]")
            # Add time delay between each request
            time.sleep(args.t)
        except requests.ConnectionError:
            pass 
        
        

# Call functions
if args.m == "dir":
    dir_enum()
elif args.m == "sub":
    sub_enum()
