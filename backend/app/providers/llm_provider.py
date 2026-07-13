from app.core.config import settings
from app.providers.gemini_provider import gemini_provider


class LLMProvider:
    def generate(self, prompt: str) -> str:

        print("LLM Provider called")

        provider_name = settings.MODEL_PROVIDER.lower()

        print("Provider selected:", provider_name)

        if provider_name == "gemini":
            return gemini_provider.generate(prompt)

        raise ValueError(
            f"Unsupported provider: {provider_name}"
        )


llm_provider = LLMProvider()