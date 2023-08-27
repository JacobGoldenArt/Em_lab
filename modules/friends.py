import logging
from typing import Dict, Any


class Friends:
    """Module to experiment with how friends and relationships influence someones personality. TBD"""

    def process(self, data: Dict[str, Any], **aux) -> Dict[str, Any]:
        friends_data = {**data, **aux}

        logging.info(f"Friends Module Data in: {friends_data}")

        return {"friends_data": friends_data}
