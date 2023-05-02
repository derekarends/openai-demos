# flake8: noqa
TWILLIO_SEND_TEXT = """
    This tool is a wrapper around Twillios's send text API, useful when you need to send a text message. 
    The input to this tool is a dictionary specifying the fields of the phone number and text message, and will be passed into Twillios's `text_send` function.
    For example, to create a text message with the phone number "5153051423" and a text message of "hello world", you would pass in the following string: 
    {{"number": "a phone number", "message": "a text message"}}
    """

TWILLIO_READ_CONTACTS = """
    This tool is a wrapper around Twillio's get contacts API, useful when you need to find what contacts you have available.
    No input is needed for this tool and it will call into Twillio's `contacts_read` function.
    """
