from langchain_core.chat_history import InMemoryChatMessageHistory


def create_chat_history():
    return InMemoryChatMessageHistory()


def clear_chat_history(chat_history):
    chat_history.clear()