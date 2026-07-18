import google.generativeai as genai

from app.core.config import settings


class GeminiProvider:

    def __init__(self):

        print("✅ Gemini initialized")

        genai.configure(api_key=settings.GEMINI_API_KEY)

        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def generate(self, prompt):

        print("✅ Gemini generate() called")

        response = self.model.generate_content(prompt)

        print("✅ Gemini finished")
        print("AI Response:")
        print(response.text)
        return response.text
gemini_provider = GeminiProvider()