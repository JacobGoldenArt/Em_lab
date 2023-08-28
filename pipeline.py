from modules.open_api import OpenAPI
import logging


class Pipeline:
    def __init__(self, *steps):
        self.steps = steps

    def process(self, data, personalization_settings=None, llm_settings=None):
        aux = {}
        if personalization_settings:
            aux["personalization_settings"] = personalization_settings
        if llm_settings:
            aux["llm_settings"] = llm_settings

        for step in self.steps:
            try:
                data = step.process(data, **aux)
            except Exception as e:
                logging.error(f"Error in {step.__class__.__name__}: {e}")
        return data


# class Pipeline:
#     def __init__(self, input_module, lobby, memory, output, llm_settings):
#         self.input_module = input_module
#         self.lobby = lobby
#         self.memory = memory
#         self.output = output
#         self.llm_api = self.initialize_llm(llm_settings)

#     def initialize_llm(self, llm_settings):
#         llm_provider = llm_settings.get("llm_provider")

#         if llm_provider == "openai":
#             return OpenAPI(
#                 model=llm_settings.get("model"),
#                 temperature=llm_settings.get("temperature"),
#                 top_p=llm_settings.get("top_p"),
#                 frequency_penalty=llm_settings.get("frequency_penalty"),
#                 presence_penalty=llm_settings.get("presence_penalty"),
#                 max_tokens=llm_settings.get("max_tokens"),
#             )
#         # Add more elif conditions for other LLM providers like Llama, Anthropic, etc.
#         else:
#             raise ValueError("Invalid LLM provider")

#     def process(self, data, personalization_settings, llm_settings):
#         try:
#             # Step 1: Preprocess user input
#             processed_input = self.input_module.process(data)

#             # Step 2: Handle lobby logic
#             lobby_data = self.lobby.process(processed_input, personalization_settings)

#             # Step 3: Retrieve and update the memory
#             recent_turns = self.memory.retrieve_recent_turns()
#             self.memory.update_memory(lobby_data)

#             # Step 4: Get LLM completion
#             llm_response = self.llm_api.get_completion(
#                 lobby_data["input_text"], recent_turns
#             )

#             # Step 5: Post-process and format the output
#             formatted_output = self.output.process(
#                 llm_response, personalization_settings
#             )

#             return {"formatted_output": formatted_output}

#         except Exception as e:
#             logging.error(f"Pipeline error: {e}")
#             return {"error": str(e)}
