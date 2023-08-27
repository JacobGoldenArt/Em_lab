class ChatInterface:
    """the entry and exit point for all communication. It should know nothing about the logic of conversation memory or the specifics of any LLM. It should just collect and display text."""

    def __init__(self, pipeline, memory):
        self.pipeline = pipeline
        self.memory = memory

    def cli_method(self):
        while True:
            user_message = input("You: ")

            # Initialize data and settings
            data = {"input_text": user_message}
            personalization_settings = {
                "user_name": "Jacob",
                "ai_name": "Catalina",
                "ai_personality": "I will give you some words to remember, then I will test your memory!",
            }
            llm_settings = {
                "llm_provider": "openai",
                "model": "gpt-3.5-turbo",
                "temperature": 0.1,
                "top_p": 1,
                "frequency_penalty": 0.0,
                "presence_penalty": 0.6,
                "max_tokens": 300,
            }

            # Run the pipeline
            response_data = self.pipeline.process(
                data,
                personalization_settings=personalization_settings,
                llm_settings=llm_settings,
            )

            # Extract the assistant's message from the response
            assistant_message = response_data.get(
                "formatted_output", "I don't know what to say."
            )

            # Print the assistant's message
            print(f"Catalina: {assistant_message}")

            # Add the turn to the memory
            self.memory.process(
                {"input_text": user_message, "response": assistant_message}
            )
