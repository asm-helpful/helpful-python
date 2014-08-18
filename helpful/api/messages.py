class Messages(object):

    """Messages in a conversation
    """

    def __init__(self, client):
        self.client = client

    def get(self, message_id, options={}):
        """Get a message the user has access to

        '/messages/:message_id' GET

        Args:
            message_id: Identifier of the message
        """
        body = options['query'] if 'query' in options else {}

        response = self.client.get('/messages/' + message_id + '', body, options)

        return response

