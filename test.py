import os
import openai
import dotenv
dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
a = openai.Completion.create(
  model="text-davinci-002",
  prompt="Say this is a test",
  max_tokens=6,
  temperature=0
)
print(a.to_dict()["choices"][0]["text"])