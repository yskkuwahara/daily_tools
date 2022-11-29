from googleapiclient.errors import HttpError


def get_messages(service, user_id, query, count, pageToken=None):
    try:
        messages = (
            service.users()
                .messages()
                .list(userId=user_id, maxResults=count, q=query, pageToken=pageToken)
                .execute()
        )

        if messages['resultSizeEstimate'] == 0:
            print('No DATA')
            return []

        return messages

    except HttpError as error:
        print(f'An error occurred: {error}')


def get_message_informations(service, user_id, query, count):
    messages = []
    try:
        message_ids = (
            service.users()
                .messages()
                .list(userId=user_id, maxResults=count, q=query)
                .execute()
        )

        if message_ids['resultSizeEstimate'] == 0:
            print('No DATA')
            return []

        for message_id in message_ids['messages']:
            detail = (
                service.users()
                    .messages()
                    .get(userId='me', id=message_id['id'])
                    .execute()
            )
            message = {
                'id': message_id['id'],
                'subject': [
                    header['value']
                    for header in detail['payload']['headers']
                    if header['name'] == 'Subject'
                ][0],
                'from': [
                    header['value']
                    for header in detail['payload']['headers']
                    if header['name'] == 'From'
                ][0]
            }

            messages.append(message)
        return messages

    except HttpError as error:
        print(f'An error occurred: {error}')


# https://googleapis.github.io/google-api-python-client/docs/dyn/gmail_v1.users.messages.html#batchDelete
def batch_delete_messages(service, user_id, message_ids):
    body = {'ids': message_ids}

    try:
        service.users()\
            .messages()\
            .batchDelete(userId=user_id, body=body)\
            .execute()

    except HttpError as error:
        print(f'An error occurred: {error}')
