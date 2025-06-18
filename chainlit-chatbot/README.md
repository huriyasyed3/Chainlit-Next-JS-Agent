# 🤖 Gemini Agent Chatbot — UI for Package Testing

This project provides a simple, professional interface for testing the `gemini-agent-helper` Python package. It is built using **Chainlit** and **Uvicorn**, and allows users to interact with a Gemini-powered agent using Google Gemini API — in the style of OpenAI’s Agent SDK.

---

## 🎯 Purpose of This Project

This project is created **specifically for testing the gemini-agent-helper package**.  
It allows students, teachers, and reviewers to:

- ✅ See how the package works in a real environment
- ✅ Verify Gemini API integration
- ✅ Test agent behavior with different prompts
- ✅ Ensure there is no fake or hardcoded logic

---

## 🧰 Requirements

Before starting, make sure you have:

- Python 3.9+
- pip installed
- A valid [Google Gemini API Key](https://ai.google.dev/)
- Internet connection

---

## 🚀 Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/gemini-agent-chatbot.git
cd gemini-agent-chatbot

2. Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install Required Packages

pip install -r requirements.txt

Make sure requirements.txt contains:

chainlit
uvicorn
python-dotenv
gemini-agent-helper

🔐 Environment Setup
4. Add Your API Key in .env
Create a file named .env in the root directory:

GEMINI_API_KEY=your_actual_gemini_api_key_here

This key is read inside your package automatically, no need to pass it manually in the code.

🧠 Run the Project (Local UI)
5. Start the Chainlit Server

chainlit run app.py --port 8000

Visit http://localhost:8000 in your browser.

🧪 Testing Agent Functionality
Here is the code used for testing:

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

This uses your gemini-agent-helper package to:

Load Gemini model

Run an agent with instructions

Stream replies to the UI

Maintain user/assistant message history


📌 What Makes This Real?
🔐 API key is taken from .env file (not hardcoded)

✅ Uses your actual Python package, not mock code

🌐 Model communication goes through real Gemini endpoint

👩‍💻 Any user can test by replacing .env with their own key

🧪 Student Testing Instructions
Students can:

Download this project

Add their own Gemini API Key

Run chainlit run app.py

Ask any question — and see live streamed response

👩‍💻 Developer

Made by Huriya Syed — focused on real AI integrations and educational tools.

This project demonstrates the functionality of a real Python package — not a fake UI.

🔗 Tags
#Python #Chainlit #Uvicorn #GeminiAPI #AgentSDK #OpenSource #RealPackage #WomenInTech