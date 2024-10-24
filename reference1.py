#!pip install --upgrade openai  # uncomment for Jupyter installing
import openai as oa;cl=oa.OpenAI();cc=cl.chat.completions.create(
messages=[
{"role": "system", "content": "You are FunnyBot"},
{"role": "assistant", "content": "relevant: farts exert force"}, # RAG
{"role": "user", "content": "Do penguin farts propel?"}
], stream=True, max_tokens=420, top_p=.69, model="gpt-3.5-turbo")
print(*(ck.choices[0].delta.content or "" for ck in cc), sep="", end="")