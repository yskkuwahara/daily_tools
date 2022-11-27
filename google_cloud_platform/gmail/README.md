# Gmail

## Dependencies:

- Python 3.8.12
- python-dotenv
- oauthlib

```bash
$ pip install python-dotenv oauthlib
```

## Environments

copy `.env-sample` to `.env`.
Update your own environments.

```
GOOGLE_API_CLIENT_ID = 'hoge.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = 'huga'
GOOGLE_SCOPE = ['https://mail.google.com/']
GOOGLE_REDIRECT_URL = 'http://localhost/callback'
```



## Repeatedly search mails and remove a specified number of times.




