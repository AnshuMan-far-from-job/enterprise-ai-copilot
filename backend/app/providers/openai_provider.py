class OpenAIProvider:
    """
    Handles communication with the OpenAI API.
    """

    def generate(self, prompt: str) -> str:
        """
        Generates a response from OpenAI.
        (Mock implementation for now.)
        """

        return f"[OpenAI] {prompt}"


openai_provider = OpenAIProvider()
