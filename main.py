from pipeline import Pipeline
from interfaces.chat_interface import ChatInterface
from modules.input_module import InputModule
from modules.lobby import Lobby
from modules.base_llm import BaseLLM
from modules.open_api import OpenAPI
from modules.memory import Memory
from modules.output import Output

import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)

"""Main Module: This can act as the orchestrator. It decides the flow of data between the modules. It calls the Memory Module to get the recent turns, then passes that to the LLM API wrapper for the current turn, then sends the LLM's response to the Chat Interface for display."""
if __name__ == "__main__":
    # These settings could come from a UI or config file
    personalization_settings = {
        "user_name": "Jacob",
        "ai_name": "Catalina",
        "ai_personality": "I will give you some words to remember, then I will test your memory!",
    }
    llm_settings = {
        "llm_provider": "openai",
        "model": "gpt-3.5-turbo-16k-0613",
        "temperature": 0.1,
        "top_p": 1,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.6,
        "max_tokens": 300,
    }

    # Initialize the memory and the pipeline
    memory = Memory()
    pipeline = Pipeline(
        InputModule(),
        Lobby(),
        OpenAPI(
            model=llm_settings["model"],
            temperature=llm_settings["temperature"],
            top_p=llm_settings["top_p"],
            frequency_penalty=llm_settings["frequency_penalty"],
            presence_penalty=llm_settings["presence_penalty"],
            max_tokens=llm_settings["max_tokens"],
        ),
        memory,
        Output(),
    )

    # Initialize the chat interface
    chat_interface = ChatInterface(
        user_name=personalization_settings["user_name"],
        ai_name=personalization_settings["ai_name"],
        ai_personality=personalization_settings["ai_personality"],
    )

    # Run the CLI interface
    chat_interface.run_cli(pipeline, personalization_settings, llm_settings)


# if __name__ == "__main__":
#     # These settings could come from a UI or config file
#     personalization_settings = {
#         "user_name": "Jacob",
#         "ai_name": "Catalina",
#         "ai_personality": "I will give you some words to remember, then I will test your memory!",
#     }
#     llm_settings = {
#         "llm_provider": "openai",
#         "model": "gpt-3.5-turbo",
#         "temperature": 0.1,
#         "top_p": 1,
#         "frequency_penalty": 0.0,
#         "presence_penalty": 0.6,
#         "max_tokens": 300,
#     }

#     # Initialize the pipeline here
#     pipeline = Pipeline(
#         InputModule(), Lobby(), Memory(), Output(), llm_settings
#     )  # Update this based on your actual modules

#     chat_interface = ChatInterface(personalization_settings, llm_settings, pipeline)
#     chat_interface.run_cli()
