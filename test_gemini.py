import os
from dotenv import load_dotenv

load_dotenv('.env')
api_key = os.getenv("GEMINI_API_KEY")
print(f"✅ API key found: {api_key[:10]}...{api_key[-4:]}")

import litellm

models_to_try = [
    "gemini/gemini-1.5-flash-latest",
    "gemini/gemini-1.5-pro-latest",
    "gemini/gemini-pro-latest",
]

for model in models_to_try:
    try:
        print(f"\n🔍 Trying model: {model}")
        response = litellm.completion(
            model=model,
            messages=[{"role": "user", "content": "Say hi"}],
            api_key=api_key
        )
        print(f"✅ SUCCESS with {model}!")
        print(f"Response: {response.choices[0].message.content}")
        break
    except Exception as e:
        print(f"❌ Failed: {str(e)[:150]}...")
