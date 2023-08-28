from abc import ABC, abstractmethod


from abc import ABC, abstractmethod


class BaseLLM(ABC):
    def __init__(
        self, model, temperature, top_p, frequency_penalty, presence_penalty, max_tokens
    ):
        self.model = model
        self.temperature = temperature
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        self.max_tokens = max_tokens

    @abstractmethod
    def format_prompt(self, input_text, recent_turns):
        pass

    @abstractmethod
    def get_completion(self, input_text, recent_turns):
        pass
