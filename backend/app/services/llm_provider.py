from app.core.config import settings
from app.providers.gemini_provider import gemini_provider


class LLMProvider:

    def generate(self, prompt: str) -> str:

        print("✅ LLM Provider called")

        provider = settings.MODEL_PROVIDER.lower()

        print("Provider =", provider)

        if provider == "gemini":
            return gemini_provider.generate(prompt)

        raise ValueError("Unsupported provider")


llm_provider = LLMProvider()