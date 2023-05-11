import streamlit as st
from langchain.agents import AgentType, initialize_agent
from langchain.llms import OpenAI
from langchain.agents.agent_toolkits.file_management import FileManagementToolkit

from dotenv import load_dotenv

import os

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')

llm = OpenAI(temperature=0)

file_managmenet_toolkit = FileManagementToolkit(
    root_dir="./code/",
    selected_tools=["file_search", "read_file", "write_file"]
)

tools = file_managmenet_toolkit.get_tools()

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True)

st.title("Product Owner AI")
st.write("This is a demo of the Product Owner AI. It is a tool that can help you manage your project. It can help you with the following tasks:")

input = st.text_input("As a user you would like to ...")

result = agent.run(input)

st.write(result)