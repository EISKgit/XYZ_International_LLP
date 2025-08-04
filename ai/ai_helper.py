# ai_helper.py
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

def get_ai_response(history):
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.5
    )

    lc_messages = []
    for msg in history:
        if msg["role"] == "system":
            lc_messages.append(SystemMessage(content=msg["content"]))
        elif msg["role"] == "user":
            lc_messages.append(HumanMessage(content=msg["content"]))
        elif msg["role"] == "assistant":
            lc_messages.append(AIMessage(content=msg["content"]))

    ai_message = AIMessage(content="")
    for res in llm.stream(lc_messages):
        ai_message.content += res.content

    return ai_message.content.strip()

 
