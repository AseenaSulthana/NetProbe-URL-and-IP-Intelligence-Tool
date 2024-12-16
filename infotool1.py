import sys
import requests
import socket
import json

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <url>")
    sys.exit(1)

# Get the URL from the command line arguments
url = sys.argv[1]

# Make an HTTP GET request to the provided URL
req = requests.get('https://' + url)
print("\nHTTP Headers:")
print(req.headers)

# Get the IP address of the provided URL using socket
gethostby = socket.gethostbyname(url)
print("\nThe IP address of " + url + " is: " + gethostby + "\n")

# Make a request to ipinfo.io to get location information of the IP address
req_two = requests.get(f'https://ipinfo.io/{gethostby}/json')
resp_ = json.loads(req_two.text)

# Print location information
print("Location:", resp_.get("loc"))
print("Region:", resp_.get("region"))
print("City:", resp_.get("city"))
print("Country:", resp_.get("country"))
print("Org: " + resp_["org"])
