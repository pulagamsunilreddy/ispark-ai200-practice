import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

endpoint = "https://fr-ai103-practice.services.ai.azure.com/openai/v1"
deployment_name = "gpt-5.5"

client = OpenAI(
    base_url=endpoint,
    api_key=os.getenv("PROJECT_API_KEY")
)

response = client.responses.create(
    model=deployment_name,
    instructions="""You are a helpful assitant.
    if you don't know the answer, just say that you don't know. don't make up an answer.""",
    input="bullet train hub in india is announced in which city?",
    tools=[{"type": "web_search"}],
    max_output_tokens=1000
)

print(f"answer: {response.output_text}")
