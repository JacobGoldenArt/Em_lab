from collections import deque
import logging, os
from typing import Dict, Any
import json


class Memory:

    """responsible for managing and formatting the conversation history. It could expose methods like get_recent_turns_formatted() that return the conversation in a format that can be directly fed into an LLM."""

    def __init__(self, max_length: int = 5):
        self.turns = deque(maxlen=max_length)

    def process(self, data: Dict[str, Any], **aux) -> Dict[str, Any]:
        # Making sure you only append if both keys exist
        if "input_text" in data and "response" in data:
            self.turns.append(
                {"user": data["input_text"], "assistant": data["response"]}
            )
        data["recent_turns"] = list(self.turns)
        logging.info(
            f"\n{self.__class__.__name__}.Recent Turns Data: {data['recent_turns']}\n"
        )
        return data

    def save_to_file(self, file_path: str):
        """Save the memory to a JSON file."""
        with open(file_path, "w") as file:
            json.dump(self.turns, file)

    def load_from_file(self, file_path: str):
        """Load the memory from a JSON file."""
        with open(file_path, "r") as file:
            self.turns = deque(json.load(file), maxlen=self.turns.maxlen)
