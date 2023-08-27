import logging
import json
from typing import Dict, Any


# Output Module
class Output:
    def process(self, data: Dict[str, Any], **aux) -> Dict[str, Any]:
        output_format = aux.get("output_format", "markdown")

        if "response" not in data:
            raise ValueError("Missing response in data.")

        if output_format == "markdown":
            formatted_output = f"## {data['response']}"
        elif output_format == "json":
            formatted_output = json.dumps({"response": data["response"]})
        else:
            raise ValueError(f"Invalid output format: {output_format}")

        logging.info(f"Formatted output: {formatted_output}")
        return {"formatted_output": formatted_output}
