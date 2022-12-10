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



## Repeatedly search specified size of mails in each batch.

```bash
# python batch_delete_messages.py {Gmal query string} {batching size}

$ python batch_delete_messages.py 'category:promotions after:2022/3/1 before:2022/9/2' 100
```


## Remove messages at once.

```bash
# python delete_messages.py {Gmal query string} {limit}

$ python delete_messages.py 'category:promotions' 1000
```



# Preparation

### 1. Enable Gmail API on GCP.

<img width="1118" src="https://user-images.githubusercontent.com/9652531/204491169-3dcbee69-4047-443c-9d38-66afc2ba2886.png">

### 2. Create OAuth Client.

<img width="1053" src="https://user-images.githubusercontent.com/9652531/204492487-09e1c1d7-b2e1-47a6-9603-96080bf61534.png">

Choose OAuth client ID.

<img width="960" src="https://user-images.githubusercontent.com/9652531/204492524-ee8e3e5f-5407-4fd1-bbc3-3afc46d6dc4b.png">

Choose Desktop App.

<img width="983" src="https://user-images.githubusercontent.com/9652531/204492392-69fa67c3-666e-414a-96d2-2a45ec3974a8.png">

Download `client_secret.json`

<img width="525" src="https://user-images.githubusercontent.com/9652531/204492348-72a59232-724b-4225-a151-81ccbdf4a443.png">



### 3. Put your `client_secret.json` into repository root dir or wherever.

<img width="783" src="https://user-images.githubusercontent.com/9652531/204493387-1951ae82-9f7c-4d0c-8e49-49393cd87f96.png">


