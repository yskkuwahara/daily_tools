import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

import settings

SCOPES = ['https://mail.google.com/']


def main():
    credentials = None

    if os.path.exists('token.json'):
        credentials = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                settings.CREDENTIAL_FILE_PATH, SCOPES)
            credentials = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(credentials.to_json())

    # flow = InstalledAppFlow.from_client_secrets_file(
    #     settings.CREDENTIAL_FILE_PATH,
    #     SCOPES,
    #     redirect_uri='http://localhost/callback')
    #
    # auth_uri = flow.authorization_url()
    print(credentials)


if __name__ == '__main__':
    main()
