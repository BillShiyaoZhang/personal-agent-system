from openai import AsyncOpenAI
import chainlit as cl

client = AsyncOpenAI(base_url="http://localhost:8080/v1", api_key="fake-key")
cl.instrument_openai()
settings = {
    "model": "mlx-community/Qwen2.5-32B-Instruct-4bit",
    "temperature": 0,
}

@cl.on_message
async def on_message(message: cl.Message):
    response = await client.chat.completions.create(
        messages=[
            {
                "content": "You are a helpful bot.",
                "role": "system"
            },
            {
                "content": message.content,
                "role": "user"
            }
        ],
        **settings
    )
    await cl.Message(content=response.choices[0].message.content).send()