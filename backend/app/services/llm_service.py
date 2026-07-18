from app.providers.llm_provider import llm_provider
from app.memory.conversation_memory import conversation_memory
from app.services.prompt_builder import prompt_builder
class LLMService:
    
    def generate_response(self,user_id:str , message: str) -> str:
        
        conversation_memory.add_message(user_id , "user",message)
        
        history=conversation_memory.get_history(user_id)
        
        print("✅ LLM Service called")

        prompt = prompt_builder.build_prompt(history)

        response = llm_provider.generate(prompt)
        
        conversation_memory.add_message(user_id, "assistant", message=response)
        

        return response


llm_service = LLMService()