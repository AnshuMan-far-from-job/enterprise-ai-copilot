class PromptBuilder:
    
    def __init__(self):
        with open("app/prompts/system_prompt.txt", "r", encoding="utf-8") as file:
            self.system_prompt = file.read().strip()

    def build_prompt(self, history):
        prompt = self.system_prompt + "\n\n"

        for message in history:
            role = message["role"].capitalize()
            content = message["content"]

            line = f"{role}: {content}"
            prompt += line + "\n"

        return prompt.strip()


prompt_builder = PromptBuilder()