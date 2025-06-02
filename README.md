📘 README: AI Agent Stack Setup
This project demonstrates a complete setup using the following tools:

uv: Lightning-fast Python package manager

openai-agents: Agent framework using OpenAI-compatible models

Chainlit: Interactive chatbot UI

LiteLLM: Unified interface for multiple LLM providers

OpenRouter: Gateway for various open-source & commercial LLMs

⚙️ Prerequisites
Python 3.10+

uv installed:

bash
Copy
Edit
pip install uv
📁 Setup Steps
1. Initialize Project
bash
Copy
Edit
uv init my_project
cd my_project
2. Install Required Packages
bash
Copy
Edit
uv add openai-agents python-dotenv chainlit litellm
🔐 Add Environment Variables
Create a .env file in your root directory:

ini
Copy
Edit
GEMINI_API_KEY=your_gemini_api_key
OPENROUTER_API_KEY=your_openrouter_api_key
OPENAI_API_KEY=your_openai_api_key
🤖 AI Agent with Gemini
File: main.py

python
Copy
Edit
import asyncio
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner

import os
from dotenv import load_dotenv

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
Run it:

bash
Copy
Edit
uv run main.py
💬 Chainlit Chatbot
File: chatbot.py

python
Copy
Edit
import chainlit as cl

@cl.on_message
async def main(message: cl.Message):
    await cl.Message(content=f"You said: {message.content}").send()
Run Chainlit:

bash
Copy
Edit
chainlit run chatbot.py
Open in browser: http://localhost:8000

🌍 LiteLLM Example
python
Copy
Edit
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
🌐 OpenRouter Example (via LiteLLM)
python
Copy
Edit
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
✅ Summary
You now have:

🔁 Gemini-powered AI Agent

💬 Chainlit-based chatbot UI

🌐 Unified LLM usage with LiteLLM

🚀 Installed & managed via uv
