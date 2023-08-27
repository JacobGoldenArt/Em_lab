import logging, os
from typing import Dict, Any
import openai
import dotenv

# Load the .env file
dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


class OpenAI_API:

    """LLM API Wrappers (e.g., OpenAI, Llama, Anthropic): These modules can be designed to accept a 'context' or 'history' parameter that they then include in their API calls. They shouldn't know where the history comes from; they should just use what they're given to make a more informed API call."""

    def process(self, data: Dict[str, Any], **aux) -> Dict[str, Any]:
        logging.info(f"Processing LLM Data: {data}")

        lobby_data = data.get("lobby_data", {})
        context = lobby_data.get("context", "No Context")
        llm_settings = aux.get("llm_settings", {})
        sys_personality = lobby_data.get("personalization_settings", {}).get(
            "ai_personality", "Default Personality"
        )

        print(context, llm_settings["model"], sys_personality)

        logging.info(f"Sending request to OpenAI API...")
        # Here would be the actual API call, which is omitted for now.

        # Create the messages list for the OpenAI API call
        completion = openai.ChatCompletion.create(
            model=llm_settings["model"],
            messages=[
                {"role": "system", "content": sys_personality},
                {"role": "user", "content": context},
            ],
            temperature=llm_settings["temperature"],
            max_tokens=llm_settings["max_tokens"],
        )

        logging.info(f"\n{self.__class__.__name__}.Completion Data: {completion}\n")

        # Return a dictionary with the OpenAI response
        return {
            "response": completion.choices[0].message["content"],
        }
