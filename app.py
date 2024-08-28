from flask import Flask, redirect, request, render_template, url_for
import requests
import subprocess
import toml

app = Flask(__name__)

config = toml.load("config.toml")
client_id = config["client"]["client_id"]
client_secret = config["client"]["client_secret"]
scope = config["client"]["scope"]

@app.route("/tokentools/azure")
def home():
    url = f"https://login.microsoftonline.com/common/oauth2/v2.0/authorize"
    
    query_params = {
        "client_id":        client_id, 
        "scope":            scope, 
        "response_type":    "code",
        "redirect_uri":     "http://localhost:8730/tokentools/azure/callback"
    }
    response = requests.get(url, params=query_params)
    return redirect(response.url)

@app.route("/tokentools/azure/callback")
def callbackHandler():
    code = request.args.get("code")
    token = subprocess.check_output(["python3", "getToken.py", client_id, client_secret, code]).decode("utf-8").split(" ")
    return render_template("callback.html", code=code, access_token=token[0], refresh_token=token[1])
    
if __name__ == "__main__":
    app.run(debug=True, port=8730)
