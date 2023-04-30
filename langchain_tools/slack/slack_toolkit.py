"""Slack Toolkit."""
from typing import List

from langchain.agents.agent_toolkits.base import BaseToolkit
from langchain.tools import BaseTool
from slack_tool import SlackAction
from slack_api import SlackApiWrapper


class SlackToolKit(BaseToolkit):
    """Slack Toolkit."""

    tools: List[BaseTool] = []

    @classmethod
    def from_slack_api_wrapper(cls, slack_api_wrapper: SlackApiWrapper) -> "SlackToolKit":
        actions = slack_api_wrapper.list()
        tools = [
            SlackAction(
                name=action["name"],
                description=action["description"],
                mode=action["mode"],
                api_wrapper=slack_api_wrapper,
            )
            for action in actions
        ]
        return cls(tools=tools)

    def get_tools(self) -> List[BaseTool]:
        """Get the tools in the toolkit."""
        return self.tools
