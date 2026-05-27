# MemAgent

MemAgent is an AI-powered wellness companion that remembers user context across conversations to provide more personalized, empathetic interactions. The project is designed for fast local development with `uv` and is structured for straightforward extension.

## Overview

MemAgent combines:
- conversational AI for supportive responses
- memory-backed context retrieval
- local vector storage for persistent user memory
- a simple CLI interface for interactive use

This repository is intended as a practical starting point for building memory-enabled assistants with Python.

## Features

- Persistent memory for user interactions
- Context-aware responses using prior conversation history
- Local development workflow with `uv`
- Easy configuration through environment variables
- Minimal project structure for rapid iteration

## Tech Stack

- Python 3.12+
- `uv` for dependency and environment management
- `langchain` and `langchain-groq` for LLM orchestration
- `mem0ai` for memory integration
- `dotenv` for environment configuration
- Chroma-backed vector storage for memory retrieval

## Project Structure

```text
memagent/
├── src/
│   ├── config.py      # Memory and embedding configuration
│   └── main.py        # CLI application entry point
├── pyproject.toml     # Project metadata and dependencies
├── uv.lock            # Locked dependency graph
└── README.md          # Project overview and usage guide
```

## Quick Start

### 1. Install `uv`

If you do not already have `uv` installed, follow the official installation guide:

https://docs.astral.sh/uv/getting-started/installation/

### 2. Create the environment and install dependencies

From the repository root:

```bash
uv sync
```

This will create the project environment and install the dependencies defined in `pyproject.toml`.

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

> The application uses the configured API keys for runtime access to the LLM and embedding providers.

### 4. Run the application

```bash
uv run python src/main.py
```

You can then chat with the assistant in the terminal.

## Development Notes

- The app writes local memory artifacts such as `chroma_db/` and `history.db/` during runtime.
- The current entry point is defined in `src/main.py`.
- If you add dependencies, update the project with:

```bash
uv add <package-name>
```

## Configuration

Core runtime settings are defined in `src/config.py`, including:
- vector store configuration
- embedding provider configuration
- history database path
- memory prompt behavior

## Roadmap

Potential next steps for this project:
- add a web interface or API endpoint
- improve memory summarization and retrieval quality
- add tests and CI/CD automation
- package the app for production deployment

## License

This project is currently unlicensed. Add a license file if you plan to share or distribute it publicly.
