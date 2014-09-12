class Accounts(object):

    """These are like organizations which use Helpful.
    """

    def __init__(self, client):
        self.client = client

    def all(self, options={}):
        """All the accounts the user has access to

        '/accounts' GET
        """
        body = options['query'] if 'query' in options else {}

        response = self.client.get('/accounts', body, options)

        return response

    def get(self, account_id, options={}):
        """Get an account the user has access to

        '/accounts/:account_id' GET

        Args:
            account_id: Identifier of the account
        """
        body = options['query'] if 'query' in options else {}

        response = self.client.get('/accounts/' + account_id + '', body, options)

        return response

    def update(self, account_id, options={}):
        """Update an account the user has access to

        '/accounts/:account_id' PATCH

        Args:
            account_id: Identifier of the account
        """
        body = options['body'] if 'body' in options else {}

        response = self.client.patch('/accounts/' + account_id + '', body, options)

        return response

