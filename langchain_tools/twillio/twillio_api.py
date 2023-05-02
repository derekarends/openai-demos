""" Util that calls Twillo. """
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Extra, root_validator

from prompts import (
    TWILLIO_SEND_TEXT,
    TWILLIO_READ_CONTACTS,
)
from langchain.utils import get_from_dict_or_env


class TwillioApiWrapper(BaseModel):
    """ Wrapper for Twillo API. """

    twillio: Any  #: :meta private:
    account_sid: Optional[str] = None
    auth_token: Optional[str] = None
    from_number: Optional[str] = None

    operations: List[Dict] = [
        {
            "mode": "text_send",
            "name": "Send text message",
            "description": TWILLIO_SEND_TEXT,
        },
        {
            "mode": "contacts_read",
            "name": "Read available contacts",
            "description": TWILLIO_READ_CONTACTS,
        }
    ]

    class Config:
        """ Configuration for this pydantic object. """
        extra = Extra.forbid

    def list(self) -> List[Dict]:
        return self.operations

    @root_validator()
    def validate_environment(cls, values: Dict) -> Dict:
        """ Validate that api key and python package exists in environment. """
        account_sid = get_from_dict_or_env(
            values, "account_sid", "TWILLIO_ACCOUNT_SID")
        values["account_sid"] = account_sid

        auth_token = get_from_dict_or_env(
            values, "auth_token", "TWILLIO_AUTH_TOKEN")
        values["auth_token"] = auth_token

        from_number = get_from_dict_or_env(
            values, "from_number", "TWILLIO_FROM_NUMBER")
        values["from_number"] = from_number

        try:
            from twilio.rest import Client
        except ImportError:
            raise ImportError(
                "twilio is not installed. "
                "Please install it with `pip install twillio`"
            )

        twillio = Client(account_sid, auth_token)
        values["twillio"] = twillio

        return values

    def text_send(self, query: str) -> str:
        """ 
        Take a json object of {"phone": "phone number", "message": "message"}
        and write send it a text
        """
        try:
            import json
            params = json.loads(query)
            fields = dict(params)

            # Send the message
            self.twillio.messages.create(
                to=fields["phone"],
                from_=self.from_number,
                body=fields["message"])

            return "Successfully wrote chat message"
        except ImportError:
            raise ImportError(
                "json is not installed. " "Please install it with `pip install json`"
            )
        except Exception as e:
            print("Error: {}".format(e))
            raise Exception("Failed to write chat message")

    # Used for dummy data
    def contacts_read(self) -> str:
        """ 
        Take a string of a name and returns a json of {name, phone}
        """
        return [
            {"name": "John Doe", "phone": "5153051423"},
            {"name": "wife", "phone": "7203051424"},
            {"name": "John Smith", "phone": "5153051425"},
            {"name": "Jane Doe", "phone": "5153051426"},
        ]

    def run(self, mode: str, query: Optional[str]) -> str:
        """ Based on the mode from the caller, run the appropriate function. """
        if mode == "text_send":
            return self.text_send(query)
        elif mode == "contacts_read":
            return self.contacts_read()
        else:
            raise ValueError(f"Got unexpected mode {mode}")