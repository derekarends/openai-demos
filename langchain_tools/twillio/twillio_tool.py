"""
This tool allows agents to interact with the Twillio Api
and operate on a Twillio instance.

To use this tool, you must first set as environment variables:
    SLACK_BOT_TOKEN
"""

from typing import Optional
from pydantic import Field

from langchain.tools.base import BaseTool
from twillio_api import TwillioApiWrapper


class TwillioAction(BaseTool):
    api_wrapper: TwillioApiWrapper = Field(default_factory=TwillioApiWrapper)
    mode: str
    name = ""
    description = ""

    def _run(self, instructions: Optional[str]) -> str:
        """Use the Twillio API to run an operation."""
        return self.api_wrapper.run(self.mode, instructions)

    async def _arun(self, _: str) -> str:
        """Use the Twillio API to run an operation."""
        raise NotImplementedError("TwillioAction does not support async")
