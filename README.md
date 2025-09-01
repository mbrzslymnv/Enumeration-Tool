# Enumeration Tool 

## Introduction
This project is a tool to enumerate subdomains and directories of a website.

## Installation 
git clone https://github.com/mbrzslymnv/Enumeration-Tool.git

### Usage

pip install -r requirements.txt

python enumeration.py -h

For linux/macOS use python3 

Usage for directory enumeration:

python enumeration.py -m dir -d domain_name -w "/path/to/wordlist"

Usage for subdomain enumeration:

python enumeration.py -m sub -d domain_name -w "/path/to/wordlist"

Adding time delay(seconds):

Default time delay is 3 seconds.

python enumeration.py -m dir -d domain_name -w "/path/to/wordlist" -t 2

Adding status code filter:

The default displayed status codes are 200, 301, and 302.

python enumeration.py -m dir -d domain_name -w "/path/to/wordlist" -s 200,404
