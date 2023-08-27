from pipeline import Pipeline
from interfaces.chat_interface import ChatInterface
from modules.input_module import InputModule
from modules.lobby import Lobby
from modules.open_api import OpenAI_API
from modules.memory import Memory
from modules.output import Output

import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)

"""Main Module: This can act as the orchestrator. It decides the flow of data between the modules. It calls the Memory Module to get the recent turns, then passes that to the LLM API wrapper for the current turn, then sends the LLM's response to the Chat Interface for display."""


if __name__ == "__main__":
    memory = Memory()
    pipeline = Pipeline(InputModule(), Lobby(), OpenAI_API(), Output(), memory)
    chat_interface = ChatInterface(pipeline, memory)
    chat_interface.cli_method()
