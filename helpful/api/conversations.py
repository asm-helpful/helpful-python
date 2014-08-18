class Conversations(object):

    """Conversations in an account
    """

    def __init__(self, client):
        self.client = client

    def list(self, account_id, options={}):
        """List all conversations in an account the user has access to

        '/accounts/:account_id/conversations' GET

        Args:
            account_id: Identifier of the account
        """
        body = options['query'] if 'query' in options else {}

        response = self.client.get('/accounts/' + account_id + '/conversations', body, options)

        return response

    def create(self, account_id, options={}):
        """Create an empty conversation in account the user has access to

        '/accounts/:account_id/conversations' POST

        Args:
            account_id: Identifier of the account
        """
        body = options['body'] if 'body' in options else {}

        response = self.client.post('/accounts/' + account_id + '/conversations', body, options)

        return response

    def get(self, conversation_id, options={}):
        """Get a conversation the user has access to

        '/conversations/:conversation_id' GET

        Args:
            conversation_id: Identifier of the conversation
        """
        body = options['query'] if 'query' in options else {}

        response = self.client.get('/conversations/' + conversation_id + '', body, options)

        return response

