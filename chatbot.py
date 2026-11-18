from langchain_core.messages import HumanMessage, AIMessage

from chain import chain


def get_chatbot_reply(user_message, chat_history):
    response = chain.invoke({
        "history": list(chat_history.messages),
        "user_message": user_message,
    })

    chat_history.add_messages([
        HumanMessage(content=user_message),
        AIMessage(content=response),
    ])

    return response