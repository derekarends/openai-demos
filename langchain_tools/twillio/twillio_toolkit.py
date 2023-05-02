"""Twillio Toolkit."""
from typing import List

from langchain.agents.agent_toolkits.base import BaseToolkit
from langchain.tools import BaseTool
from twillio_tool import TwillioAction
from twillio_api import TwillioApiWrapper


class TwillioToolKit(BaseToolkit):
    """Twillio Toolkit."""

    tools: List[BaseTool] = []

    @classmethod
    def from_twillio_api_wrapper(cls, twillio_api_wrapper: TwillioApiWrapper) -> "TwillioToolKit":
        actions = twillio_api_wrapper.list()
        tools = [
            TwillioAction(
                name=action["name"],
                description=action["description"],
                mode=action["mode"],
                api_wrapper=twillio_api_wrapper,
            )
            for action in actions
        ]
        return cls(tools=tools)

    def get_tools(self) -> List[BaseTool]:
        """Get the tools in the toolkit."""
        return self.tools
