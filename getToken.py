import requests

def getToken(client_id, client_secret, code):
    url = f"https://login.microsoftonline.com/common/oauth2/v2.0/token"

    data = {
        "client_id":        client_id,
        "client_secret":    client_secret,
        "redirect_uri":     "http://localhost:8730/tokentools/azure/callback",
        "code":             code,
        "grant_type":       "authorization_code"
    }

    response = requests.post(url, data=data)
    if response.status_code != 200:
        return response.json() + "$$split$$" + response.json()
    elif response.json()["token_type"] == "Bearer":
        return response.json()["access_token"] + "$$split$$" + response.json()["refresh_token"]
    return "Error" + "$$split$$" + "Error"