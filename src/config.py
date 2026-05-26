import os
from dotenv import load_dotenv

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
