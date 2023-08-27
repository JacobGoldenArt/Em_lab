import logging
from typing import Dict, Any


# Input Module
class InputModule:
    def process(self, data: Dict[str, Any], **aux) -> Dict[str, Any]:
        try:
            input_text = data["input_text"].strip()
        except KeyError:
            raise KeyError("Input data is missing required field 'input_text'")

        logging.info(f"Processing input text: {input_text}")
        return {"input_text": input_text}
