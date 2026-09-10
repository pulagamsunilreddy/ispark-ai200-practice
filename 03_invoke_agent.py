import os
from dotenv import load_dotenv
load_dotenv()
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

az_credential = DefaultAzureCredential()
client = AIProjectClient(endpoint=os.getenv("AZURE_PROJECT_ENDPOINT"), credential=az_credential)

openai = client.get_openai_client()
responses = openai.responses.create(
    input="how to make function key always on on amkette bluetooth keyboard?",
    extra_body={"agent_reference": {"name": "IT-Helpdesk-Agent", "type": "agent_reference"}}
    )

print(responses.output_text)