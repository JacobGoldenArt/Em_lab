from modules.base_llm import BaseLLM
import openai
import dotenv
import os

# Load the .env file
dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


class OpenAPI(BaseLLM):
    def __init__(self, *args, **kwargs):
        print(f"Debug: args in OpenAPI init: {args}")  # Debugging line
        print(f"Debug: kwargs in OpenAPI init: {kwargs}")  # Debugging line
        super(OpenAPI, self).__init__(*args, **kwargs)

    def format_prompt(self, input_text, recent_turns):
        print(f"Debug: recent_turns: {recent_turns}")  # Debugging line
        formatted_turns = ""
        if recent_turns:
            for turn in recent_turns:
                formatted_turns += f"user: {turn.get('user', 'Missing User')}\nassistant: {turn.get('assistant', 'Missing Assistant')}\n"
        else:
            print("Warning: recent_turns is empty or None")

        formatted_turns += f"user: {input_text}"
        print(f"Debug: formatted_turns: {formatted_turns}")  # Debugging line
        return formatted_turns

    def get_completion(self, input_text, recent_turns):
        print(f"Debug: input_text in get_completion: {input_text}")
        formatted_prompt = self.format_prompt(input_text, recent_turns)
        print(f"Formated Prompt {formatted_prompt}")
        completion = openai.ChatCompletion.create(
            model=self.model,
            messages=formatted_prompt,
            max_tokens=self.max_tokens,
            n=1,
            stop=None,
            temperature=self.temperature,
            top_p=self.top_p,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
        )
        return completion["choices"][0]["text"].strip()

    def process(self, data, **aux):
        print(f"Debug: Data received in OpenAPI: {data}")  # Debugging line
        print(f"Debug: Aux received in OpenAPI: {aux}")  # Debugging line

        input_text = data.get("input_text")
        recent_turns = data.get("recent_turns", [])

        if not input_text:
            print("Warning: input_text is empty or None")  # Debugging line

        response = self.get_completion(input_text, recent_turns)
        data["response"] = response

        return data
