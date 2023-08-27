import logging
from typing import Dict, Any


class Humor:
    """Module to experiment with humor. TBD"""

    def process(self, data: Dict[str, Any], **aux) -> Dict[str, Any]:
        humor_data = {**data, **aux}

        logging.info(f"Humor Module Data in: {humor_data}")

        return {"friends_data": humor_data}
