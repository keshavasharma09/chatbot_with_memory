Chatbot with Conversation Memory
This project is a multi-file Python application that implements a chatbot with conversation memory using a Chainlit browser-based interface. 
It uses LangChain to connect to OpenAI language model.   
Key FeaturesLanguage Model: Uses GPT 4.1 as the core language model.   
Framework: Uses LangChain to build the prompt and model chain.   
Conversation Memory: Stores the current chat's messages using InMemoryChatMessageHistory.   
Few-Shot Prompting: Uses few-shot examples within the system prompt to demonstrate how to remember details and handle unknown details appropriately.   
User Interface: Uses Chainlit to provide a browser-based chat interface.  

chatbot_with_memory/
├── app.py             # Chainlit UI and event handlers
├── config.py          # Gemini model configuration
├── memory.py          # Create and clear conversation history
├── prompt.py          # System prompt and few-shot examples
├── chain.py           # Connect prompt + Gemini + output parser
├── chatbot.py         # Generate reply and save messages
└── requirements.txt   # Required Python packages