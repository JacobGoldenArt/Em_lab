import logging
from typing import Dict, Any


class EmoIntel:
    """Module to experiment with developing Emotional Inteligence. TBD"""

    def process(self, data: Dict[str, Any], **aux) -> Dict[str, Any]:
        emo_data = {**data, **aux}

        logging.info(f"Dreaming Module Data in: {emo_data}")

        return {"Emo data": emo_data}
