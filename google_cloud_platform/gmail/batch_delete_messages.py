import pprint
import sys

import authenticate
import message


def main(query='is:unread', count=100):
    service = authenticate.get_authenticated_service()
    messages = message.get_messages(service, 'me', query, count)

    while len(messages['messages']) > 0:
        message_ids = list(map(lambda m: m['id'], messages['messages']))
        message.batch_delete_messages(service, 'me', message_ids)

        token_key = 'nextPageToken'
        if token_key not in messages:
            break

        messages = message.get_messages(service, 'me', query, count, pageToken=messages['nextPageToken'])
        pprint.pprint('delete next: ' + str(len(messages['messages'])))


# python batch_delete_messages.py 'category:promotions after:2021/11/1 before:2022/5/7' 10000
if __name__ == '__main__':
    query = sys.argv[1]
    count = sys.argv[2]

    main(query=query, count=count)
