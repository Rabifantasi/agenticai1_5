# main.py
import os
import chainlit as cl
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner

# Load Gemini key from .env
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Gemini-compatible OpenAI-style client
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Create the agent with instructions
agent = Agent(
    name="GeminiBot",
    instructions="You are a smart assistant that answers helpfully.",
    model=OpenAIChatCompletionsModel(model="gemini-1.5-flash", openai_client=client),
)

@cl.on_message
async def on_message(message: cl.Message):
    # Get a response from the Gemini-powered agent
    result = await Runner.run(agent, message.content)

    # Send the response back to the Chainlit UI
    await cl.Message(
        content=result.final_output
    ).send()
