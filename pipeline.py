import logging
from typing import Dict, Any


# Base Pipeline Class
class Pipeline:
    def __init__(self, *steps):
        self.steps = steps

    def process(self, data: Dict[str, Any], **aux) -> Dict[str, Any]:
        for step in self.steps:
            try:
                data = step.process(data, **aux)
            except Exception as e:
                logging.error(f"Error in {step.__class__.__name__}: {e}")
        return data
