import os
from dotenv import load_dotenv
from mem0 import Memory
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

mem0_config = {
    "vector_store": {
        "provider": "chroma",
        "config": {"path": "./chroma_db", "collection_name": "wellness_chatbot"},
    },
    "llm": {
        "provider": "openai",
        "config": {
            "model": "deepseek-r1:1.5b",
            "openai_base_url": "http://localhost:11434/v1",
            "api_key": "ollama",
            "temperature": 0.1,
        },
    },
    "embedder": {
        "provider": "gemini",
        "config": {
            "model": "models/gemini-embedding-2",
            "embedding_dims": 3072,
            "api_key": os.getenv("GOOGLE_API_KEY"),
        },
    },
    "history_db_path": "./history.db",
    "custom_prompt": "Extract only essential facts about the user's identity, preferences, and emotional state. Be extremely concise.",
}

memory = Memory.from_config(mem0_config)

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7,
    groq_api_key=os.getenv("GROQ_API_KEY"),
)

WELLNESS_SYSTEM_PROMPT = """You are a compassionate, empathetic mental health and wellness companion. 
Your goal is to provide supportive listening, mindfulness techniques, and wellness coaching.

CRITICAL SAFETY POLICY: You are an AI, not a licensed therapist or medical professional. 
If the user expresses thoughts of self-harm, severe clinical depression, or a medical crisis, 
you must immediately provide standard crisis hotline resources and gently encourage them to seek professional human help.

Use the following context from previous conversations to provide personalized care without explicitly mentioning you read it from a database:
[PAST USER CONTEXT]
{user_context}

make is consis ans short answers and do not mention the context in the answer.

"""

from pprint import pprint


def chat_with_wellness_bot(user_id: str, user_message: str) -> str:
    search_results = memory.search(query=user_message, filters={"user_id": user_id})
    pprint(search_results)

    context_list = []
    if search_results and "results" in search_results:
        for item in search_results["results"]:
            context_list.append(f"- {item['memory']}")

    user_context_string = (
        "\n".join(context_list)
        if context_list
        else "No prior background context shared yet."
    )

    formatted_system_prompt = WELLNESS_SYSTEM_PROMPT.format(
        user_context=user_context_string
    )

    messages = [
        SystemMessage(content=formatted_system_prompt),
        HumanMessage(content=user_message),
    ]

    response = llm.invoke(messages)
    ai_reply = response.content

    interaction = [
        {"role": "user", "content": user_message},
        {"role": "assistant", "content": ai_reply},
    ]
    memory.add(interaction, user_id=user_id)

    return ai_reply


if __name__ == "__main__":
    user_session_id = "user_patient_456"

    print(
        "AI: Hello! I'm here to support your emotional well-being today. What's on your mind?"
    )

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["quit", "exit"]:
            print("AI: Take care of yourself. Goodbye!")
            break

        bot_response = chat_with_wellness_bot(
            user_id=user_session_id, user_message=user_input
        )
        print(f"\nAI: {bot_response}")
