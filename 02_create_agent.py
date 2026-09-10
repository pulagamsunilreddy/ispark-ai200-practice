import os
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv
load_dotenv()

az_credential = DefaultAzureCredential()
project_client = AIProjectClient(endpoint=os.getenv("AZURE_PROJECT_ENDPOINT"), credential=az_credential)

agent = project_client.agents.create_version(
    agent_name="IT-Helpdesk-Agent",
    definition=PromptAgentDefinition(
        model="gpt-5.4",
        instructions=("You are a helpful assistant that can help with IT helpdesk requests" 
        "Give step-by-step instructions"
        "say don't know if you don't have the answer" ),
        tools=[]
    )
)
print(agent.id)
print(agent.name)
print(agent.version)