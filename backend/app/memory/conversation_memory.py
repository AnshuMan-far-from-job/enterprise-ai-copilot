class ConversationMemory:
    
    def __init__(self):
        self.memory = {}

    def add_message(self, user_id, role, message):

        # Create an empty conversation for a new user
        if user_id not in self.memory:
            self.memory[user_id] = []

        # Add the new message
        self.memory[user_id].append(
            {
                "role": role,
                "content": message
            }
        )