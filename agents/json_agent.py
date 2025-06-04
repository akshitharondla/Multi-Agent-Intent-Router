# JSON Agent
import json
class JSONAgent:
    def process(self, content, memory):
        try:
            data = json.loads(content)
            print('Processed JSON:', data)
            memory.store_data('json', data)
        except json.JSONDecodeError:
            print('Invalid JSON format')
