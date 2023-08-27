import logging
from typing import Dict, Any


class Dreaming:
    """Module to process recent conversations, summarizes them, and simulates dreaming to handle memory.. TBD"""

    def process(self, data: Dict[str, Any], **aux) -> Dict[str, Any]:
        dreaming_data = {**data, **aux}

        logging.info(f"Dreaming Module Data in: {dreaming_data}")

        return {"dreaming data": dreaming_data}
