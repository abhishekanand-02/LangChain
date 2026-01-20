from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

model = OpenAI(name="openai", model="gpt-3.5-turbo-instruct", temperature=0)

input_text = "Tell me a joke."

# Invoke the model
response = model.invoke(input_text)
print(response)

# Streaming response
# for chunk in model.stream(input_text):
#         print(chunk, end="", flush=True)