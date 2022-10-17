# APIs with Python

# Install requests
# pip install requests - run this in terminal (Pycharm)

import requests

# Get
request_bbc_status_code = requests.get("https://www.bbc.co.uk/iplayer/live/bbcnews")
# Check the API call - 200 expected
print(request_bbc_status_code.status_code)


