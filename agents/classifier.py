# Classifier Agent
import os
from agents.json_agent import JSONAgent
from agents.email_agent import EmailAgent
from shared_memory.memory import Memory

class ClassifierAgent:
    def __init__(self):
        self.memory = Memory()

    def handle(self, filepath):
        with open(filepath, 'r') as file:
            content = file.read()
        # Naive classification
        if filepath.endswith('.json'):
            intent = 'Invoice'
            agent = JSONAgent()
        elif filepath.endswith('.pdf'):
            intent = 'Regulation'
            agent = JSONAgent()
        else:
            intent = 'RFQ'
            agent = EmailAgent()

        format_type = os.path.splitext(filepath)[1][1:].upper()
        self.memory.log(filepath, format_type, intent)
        agent.process(content, self.memory)
