class ChatInterface:
    def __init__(self, user_name, ai_name, ai_personality):
        self.user_name = user_name
        self.ai_name = ai_name
        self.ai_personality = ai_personality

    def get_input_cli(self):
        user_input = input(f"{self.user_name}: ")
        return user_input

    def display_output_cli(self, ai_output):
        print(f"{self.ai_name}: {ai_output}")

    def run_cli(self, pipeline, personalization_settings, llm_settings):
        while True:
            user_message = input(f"{self.user_name}: ")

            # Initialize data
            data = {"input_text": user_message}

            # Run the pipeline
            response_data = pipeline.process(
                data,
                personalization_settings=personalization_settings,
                llm_settings=llm_settings,
            )

            # Extract the assistant's message from the response
            assistant_message = response_data.get(
                "formatted_output", "I don't know what to say."
            )

            # Print the assistant's message
            print(f"{self.ai_name}: {assistant_message}")

            # Check for exit command
            if user_message.lower() == "quit":
                print(f"{self.ai_name}: Goodbye!")
                break


# class ChatInterface:
#     def __init__(self, personalization_settings, llm_settings):
#         self.p_settings = personalization_settings
#         self.llm_settings = llm_settings

#     def get_input_cli(self):
#         user_input = input(f"{self.p_settings.get['user_name']}: ")
#         return user_input

#     def get_input_api(self, api_request):
#         # Extract user input from API request (assuming JSON payload)
#         user_input = api_request.json().get("user_input")
#         return user_input

#     def display_output_cli(self, ai_output):
#         print(f"{self.p_settings.get['ai_name']}: {ai_output}")

#     def display_output_api(self):
#         # Convert AI output to appropriate API response
#         # Return this as a FastAPI response
#         pass

#     def run_cli(self):
#         while True:
#             user_message = input(f"{self.p_settings['user_name']}: ")

#             # Initialize data
#             data = {"input_text": user_message}

#             # Run the pipeline
#             response_data = self.pipeline.process(
#                 data,
#                 personalization_settings=self.p_settings,
#                 llm_settings=self.llm_settings,
#             )

#             # Extract the assistant's message from the response
#             assistant_message = response_data.get(
#                 "formatted_output", "I don't know what to say."
#             )

#             # Print the assistant's message
#             print(f"{self.p_settings['ai_name']}: {assistant_message}")

#             # Check for exit command
#             if user_message.lower() == "quit":
#                 print(f"{self.p_settings['ai_name']}: Goodbye!")
#                 break

#     def run_api(self, api_request):
#         user_input = self.get_input_api(api_request)
#         # Logic to process user input and get AI output
#         # ...
#         self.display_output_api(ai_output)
