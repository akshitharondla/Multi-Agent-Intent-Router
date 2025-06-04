# Entry point for the multi-agent system
from agents.classifier import ClassifierAgent
from shared_memory.memory import Memory

if __name__ == '__main__':
    agent = ClassifierAgent()
    sample_file = 'samples/sample_email.txt'
    agent.handle(sample_file)
#hello