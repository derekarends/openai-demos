# flake8: noqa
SLACK_READ_CHANNELS = """
    This tool is a wrapper around Slack's get channels API, useful when you need to find what channels exist in Slack.
    No input is needed for this tool and will call into Slack's `channels_read` function.
    """

SLACK_WRITE_MESSAGE_TO_CHANNEL = """
    This tool is a wrapper around Slacks's chat write API, useful when you need to create or post a Slack message. 
    The input to this tool is a dictionary specifying the fields of the Slack channel and message, and will be passed into Slacks's `chat_write` function.
    For example, to create a slack message with the text "hello world", you would pass in the following string: 
    {{"channel": "a channel", "message": "hello world"}}
    """