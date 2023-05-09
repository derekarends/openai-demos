# flake8: noqa
SEND_GRID_SEND_EMAIL = """
    This tool is a wrapper around Send Grid's send email API, useful when you need to create and send an email. 
    The input to this tool is a dictionary specifying the fields of the Slack channel and message, and will be passed into Send Grid's `email_send` function.
    For example, to create an email with the subject "hello world" with a body "To whom it may concern." from "jd@acme.com" to "box@me.com" you would pass in the following string: 
    {{"subject": "hello world", "body": "To whom it may concern.", "from_email": "jd@acme.com", "to_emails": ": "box@me.com"}}
    """
