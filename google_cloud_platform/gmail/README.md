# Gmail

## Dependencies:

- Python 3.8.12
- python-dotenv
- google-api-python-client
- google-auth-httplib2
- google-auth-oauthlib

```bash
$ pip install python-dotenv \
              google-api-python-client \
              google-auth-httplib2 \
              google-auth-oauthlib
```

## Environments

copy `.env-sample` to `.env`.
Update your own environments.

```
CREDENTIAL_FILE_PATH='path/to/your/client_secret.json'
```



## Repeatedly search mails and remove a specified number of times.

```bash
python batch_delete_messages.py 'category:promotions after:2021/11/1 before:2022/5/7' 10000
```



