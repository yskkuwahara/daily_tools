import pprint
import sys

import authenticate
import message


def main(query='is:unread', count=100):
    service = authenticate.get_authenticated_service()

    messages = message.get_messages(service, 'me', query, count)
    message_ids = list(map(lambda m: m['id'], messages['messages']))

    message.batch_delete_messages(service, 'me', message_ids)

    pprint.pprint(message_ids)


# python delete_messages.py 'category:promotions after:2021/11/1 before:2022/5/7' 10
if __name__ == '__main__':
    query = sys.argv[1]
    count = sys.argv[2]

    main(query=query, count=count)
