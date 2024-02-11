class Agent:
    def __init__(self, name):
        self.name = name

    def ask_question(self, recipient, question):
        print(f"{self.name} asks {recipient.name}: {question}")
        response = recipient.answer_question(self, question)
        print(f"{recipient.name} responds to {self.name}: {response}")

    def answer_question(self, sender, question):
        if "weather" in question:
            return "It's sunny today!"
        elif "favorite color" in question:
            return "My favorite color is blue."
        else:
            return "I'm not sure about that."

# Creating two agents
agent1 = Agent("Agent 1")
agent2 = Agent("Agent 2")

# Agent 1 asks Agent 2 about the weather
agent1.ask_question(agent2, "How's the weather today?")

# Agent 2 asks Agent 1 about their favorite color
agent2.ask_question(agent1, "What's your favorite color?")

# Agent 1 asks Agent 2 a different question
agent1.ask_question(agent2, "Do you like pizza?")
