from .http_client import HttpClient

# Assign all the api classes
from .api.accounts import Accounts
from .api.people import People
from .api.conversations import Conversations
from .api.messages import Messages


class Client(object):

    def __init__(self, auth={}, options={}):
        self.http_client = HttpClient(auth, options)

    def accounts(self):
        """These are like organizations which use Helpful.
        """
        return Accounts(self.http_client)

    def people(self):
        """People who operate or interacted with the account
        """
        return People(self.http_client)

    def conversations(self):
        """Conversations in an account
        """
        return Conversations(self.http_client)

    def messages(self):
        """Messages in a conversation
        """
        return Messages(self.http_client)

