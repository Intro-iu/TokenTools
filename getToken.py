# POST https://login.microsoftonline.com/common/oauth2/v2.0/token
# Content-Type: application/x-www-form-urlencoded

# client_id={client_id}&redirect_uri={redirect_uri}&client_secret={client_secret}
# &code={code}&grant_type=authorization_code

import requests
import sys

client_id = sys.argv[1]
client_secret = sys.argv[2]
code = sys.argv[3]

url = f"https://login.microsoftonline.com/common/oauth2/v2.0/token"

data = {
    "client_id":        client_id,
    "client_secret":    client_secret,
    "redirect_uri":     "http://localhost:8730/tokentools/onedrive/callback",
    "code":             code,
    "grant_type":       "authorization_code"
}

if __name__ == "__main__":
    response = requests.post(url, data=data)
    print(response.json()["access_token"], end=" ")
    print(response.json()["refresh_token"])