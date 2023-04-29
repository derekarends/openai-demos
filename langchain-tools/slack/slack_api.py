"""Util that calls Slack."""
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Extra, root_validator
from slack_sdk.errors import SlackApiError

from prompts import (
    SLACK_WRITE_MESSAGE_TO_CHANNEL,
    SLACK_READ_CHANNELS,
)
from langchain.utils import get_from_dict_or_env


class SlackApiWrapper(BaseModel):
    """Wrapper for Slack API."""

    slack: Any  #: :meta private:
    bot_token: Optional[str] = None

    operations: List[Dict] = [
        {
            "mode": "channels_read",
            "name": "Read the channels",
            "description": SLACK_READ_CHANNELS,
        },
        {
            "mode": "chat_write",
            "name": "Write a chat message to the channel",
            "description": SLACK_WRITE_MESSAGE_TO_CHANNEL,
        }
    ]

    class Config:
        """Configuration for this pydantic object."""

        extra = Extra.forbid

    def list(self) -> List[Dict]:
        return self.operations

    @root_validator()
    def validate_environment(cls, values: Dict) -> Dict:
        """Validate that api key and python package exists in environment."""
        bot_token = get_from_dict_or_env(values, "bot_token", "SLACK_BOT_TOKEN")
        values["bot_token"] = bot_token

        try:
            from slack_sdk import WebClient
        except ImportError:
            raise ImportError(
                "tweepy is not installed. "
                "Please install it with `pip install tweepy`"
            )

        slack = WebClient(token=bot_token)
        values["slack"] = slack

        return values

    def channels_read(self) -> str:
        try:
            import json
            # Call the conversations.list method using the WebClient
            response = self.slack.conversations_list()
            channels = []

            for channel in response["channels"]:
                channels.append({"name": channel["name"], "id": channel["id"]})

            json_channels = json.dumps(channels)
            return json_channels

        except ImportError:
            raise ImportError(
                "json is not installed. " "Please install it with `pip install json`"
            )
        except SlackApiError as e:
            print("Error: {}".format(e))
            raise Exception("Failed to write chat message")

    def chat_write(self, query: str) -> str:
        try:
            import json
            params = json.loads(query)
            fields = dict(params)
            response = self.slack.chat_postMessage(
                channel=fields["channel"],
                text=fields["message"]
            )
            return "Successfully wrote chat message"
        except ImportError:
            raise ImportError(
                "json is not installed. " "Please install it with `pip install json`"
            )
        except SlackApiError as e:
            print("Error: {}".format(e))
            raise Exception("Failed to write chat message")

    def run(self, mode: str, text: str) -> str:
        if mode == "channels_read":
            return self.channels_read()
        elif mode == "chat_write":
            return self.chat_write(text)
        else:
            raise ValueError(f"Got unexpected mode {mode}")
