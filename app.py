from flask import Flask, redirect, request, render_template
import requests
import subprocess
app = Flask(__name__)

client_id = "89a77af5-8151-4623-bc7e-0969a76ef37f"
client_secret = "BPk8Q~XGG6tN9s0lbyUh0ZXWZc72u5wIISnlgc~r"

@app.route("/onedrive")
def home():
    url = f"https://login.microsoftonline.com/common/oauth2/v2.0/authorize"
    
    query_params = {
        "client_id": client_id, 
        "scope": "Files.ReadWrite offline_access", 
        "response_type": "code",
        "redirect_uri":"http://localhost:8000/onedrive/callback"
    }
    response = requests.get(url, params=query_params)
    return redirect(response.url)

@app.route("/onedrive/callback")
def callbackHandler():
    code = request.args.get("code")
    token = subprocess.check_output(["python3", "getToken.py", client_id, client_secret, code]).decode("utf-8")
    return render_template("callback.html", code=code, token=token)
    
if __name__ == "__main__":
    app.run(debug=True, port=8000)
 