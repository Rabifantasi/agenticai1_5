# 🤖 AI Agent Stack Setup

This project demonstrates a full stack using:

- `uv`: Fast Python package manager
- `openai-agents`: Framework for building LLM agents
- `Chainlit`: Chatbot interface
- `LiteLLM`: Unified wrapper for OpenAI-compatible LLMs
- `OpenRouter`: API gateway for multiple LLMs

---

## ⚙️ Requirements

- Python 3.10+
- `uv` installed:

```bash
pip install uv
```

---

## 📁 Project Initialization

```bash
uv init my_project
cd my_project
uv add openai-agents python-dotenv chainlit litellm
```

---

## 🔐 .env Configuration

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_gemini_api_key
OPENROUTER_API_KEY=your_openrouter_api_key
OPENAI_API_KEY=your_openai_api_key
```

---

## 🤖 Gemini Agent (OpenAI-Compatible)

`main.py`:

```python
import asyncio
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner
from dotenv import load_dotenv
import os

load_dotenv()

client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

async def main():
    agent = Agent(
        name="GeminiBot",
        instructions="Only respond in haikus.",
        model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
    )
    result = await Runner.run(agent, "Explain recursion in programming.")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
```

Run it:

```bash
uv run main.py
```

---

## 💬 Chainlit Chatbot

`chatbot.py`:

```python
import chainlit as cl

@cl.on_message
async def main(message: cl.Message):
    await cl.Message(content=f"You said: {message.content}").send()
```

Run with:

```bash
chainlit run chatbot.py
```

Open: [http://localhost:8000](http://localhost:8000)

---

## 🌍 LiteLLM with Gemini

```python
from litellm import completion
import os
from dotenv import load_dotenv

load_dotenv()

response = completion(
    model="gemini/gemini-1.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
    messages=[{ "role": "user", "content": "Tell me a joke." }]
)

print(response)
```

---

## 🌐 OpenRouter via LiteLLM

```python
from litellm import completion
import os
from dotenv import load_dotenv

load_dotenv()

response = completion(
    model="openrouter/mistralai/mixtral-8x7b",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    messages=[{ "role": "user", "content": "What is AI?" }]
)

print(response)
```

---

## ✅ Summary

You now have:

- ⚡ Fast package management with `uv`
- 🧠 Gemini agent using OpenAI Agents SDK
- 🗨️ Interactive chatbot via Chainlit
- 🌍 Unified LLM calls with LiteLLM
- 🔗 Access to many LLMs via OpenRouter
