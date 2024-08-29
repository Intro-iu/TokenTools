# TokenTools
TokenTools is a tool that helps developers obtain tokens (e.g., access_token, refresh_token) from Microsoft (Azure).

# Usage
Modify the configuration file `config.toml`. 

It should be in the following format:

```toml
[client]
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
scope = "YOUR_SCOPE"
```

Add the redirect URI `http://localhost:8730/tokentools/azure/callback` for your apps in [Azure](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade).
> Click: `Your App -> Redirect URIs` and then add the above URI.

![61ff98b9554543c57f7606ddd0ca868](https://github.com/user-attachments/assets/a23c2edb-8e4a-4f1e-b578-3100d0270bd3)

Then, run the program:
```bash
python app.py
```

And visit the [website](http://localhost:8730/tokentools/azure).

After logging in, the website will return the tokens you need.

![5b33ff425267dc60593fbbc9fb90cd9](https://github.com/user-attachments/assets/c5a8096e-81e2-47fd-af41-0f1d49da30d2)
