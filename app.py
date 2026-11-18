import asyncio
import chainlit as cl

from chatbot import get_chatbot_reply
from memory import create_chat_history, clear_chat_history


@cl.on_chat_start
async def on_chat_start():
    chat_history = create_chat_history()
    cl.user_session.set("chat_history", chat_history)

    await cl.Message(
        content="Hello! I am your chatbot with conversation memory. "
                "You can ask follow-up questions. Type `clear` to reset memory "
                "or `history` to view the stored conversation."
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    user_message = message.content.strip()

    if not user_message:
        await cl.Message(content="Please enter a message.").send()
        return

    chat_history = cl.user_session.get("chat_history")

    if user_message.lower() == "clear":
        clear_chat_history(chat_history)
        await cl.Message(content="Conversation memory cleared.").send()
        return

    if user_message.lower() == "history":
        if not chat_history.messages:
            await cl.Message(content="No messages are stored yet.").send()
            return

        history_lines = []

        for item in chat_history.messages:
            role = "You" if item.type == "human" else "Chatbot"
            history_lines.append(f"**{role}:** {item.content}")

        await cl.Message(content="\n\n".join(history_lines)).send()
        return

    try:
        response = await asyncio.to_thread(
            get_chatbot_reply,
            user_message,
            chat_history,
        )
        await cl.Message(content=response).send()

    except Exception as error:
        await cl.Message(
            content=f"An error occurred while contacting Gemini: {error}"
        ).send()