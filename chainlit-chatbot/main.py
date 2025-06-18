import chainlit as cl
from gemini_helper.core import get_gemini_model
from agents import Runner, Agent
from openai.types.responses import ResponseTextDeltaEvent  

model = get_gemini_model()

agent = Agent(
    name="Next JS Expert",
    instructions="You are a Next JS expert, please assist the user.",
    model=model
)

@cl.on_chat_start
async def handle_start():
    cl.user_session.set("history", [])
    await cl.Message(content="Hello, I'm Huriya Syed! How can I help you?").send()

@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user_session.get('history')
    history.append({"role": "user", "content": message.content})

    msg = cl.Message(content=" ")
    await msg.send()

    result = Runner.run_streamed(agent, input=history)

    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            await msg.stream_token(event.data.delta)

    history.append({"role": "assistant", "content": result.final_output})
    cl.user_session.set('history', history)

    await cl.Message(content=result.final_output).send()
