# Email Agent
class EmailAgent:
    def process(self, content, memory):
        sender = 'user@example.com'  # mock
        urgency = 'High' if 'urgent' in content.lower() else 'Normal'
        result = {'sender': sender, 'urgency': urgency, 'body': content[:100]}
        print('Processed Email:', result)
        memory.store_data('email', result)
