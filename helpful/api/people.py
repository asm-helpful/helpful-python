class People(object):

    """People who operate or interacted with the account
    """

    def __init__(self, client):
        self.client = client

    def all(self, account_id, options={}):
        """List all people in the account the user has access to

        '/accounts/:account_id/people' GET

        Args:
            account_id: Identifier of the account
        """
        body = options['query'] if 'query' in options else {}

        response = self.client.get('/accounts/' + account_id + '/people', body, options)

        return response

