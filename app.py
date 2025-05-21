import streamlit as st
from langchain_community.agent_toolkits import GmailToolkit
from langchain_community.tools.gmail.utils import (
    build_resource_service,
    get_gmail_credentials,
)
from langchain import hub
from langchain.agents import AgentExecutor, create_structured_chat_agent
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()


# Initialize Gmail Toolkit
credentials = get_gmail_credentials(
    token_file="token.json",
    scopes=["https://mail.google.com/"],
    client_secrets_file="credentials.json",
)
api_resource = build_resource_service(credentials=credentials)
toolkit = GmailToolkit(api_resource=api_resource)
tools = toolkit.get_tools()

# Define base prompt and instructions
instructions = """
You are an assistant capable of using the following tool to interact with Gmail. Your task is to use the relevant tool as per their usage.

Tools and when to use:
- GmailCreateDraft : Use this tool to compose and save a draft email in the drafts folder of user's Gmail account.
- GmailSendMessage : Use this tool to send a pre-composed email from the drafts folder of user's Gmail account.
- GmailSearch : Use this tool to find specific emails matching given criteria in the user's Gmail inbox.
- GmailGetMessage : Use this tool to retrieve and output the content of the email from the specific sender in user's Gmail inbox.
- GmailGetThread : Use this tool to retrieve and view the entire conversation thread of emails from the specific sender in user's Gmail account.

Perform these actions directly in the user's Gmail account and output the results accordingly.
When providing output, make sure to describe the action performed and the outcome in a user-friendly manner.
"""

# Pull the base prompt template
base_prompt = hub.pull("hwchase17/structured-chat-agent")

# Customize the base prompt with specific instructions
prompt = base_prompt.partial(instructions=instructions)

# Initialize AzureChatOpenAI
llm = AzureChatOpenAI(
    deployment_name=os.getenv("AZURE_DEPLOYMENT_NAME"),
    model_name=os.getenv("AZURE_MODEL_NAME"),
    azure_endpoint=os.getenv("AZURE_ENDPOINT"),
    openai_api_version=os.getenv("AZURE_API_VERSION"),
    openai_api_key=os.getenv("AZURE_API_KEY"),
    temperature=0
)

# Create agent and executor
agent = create_structured_chat_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=toolkit.get_tools(),
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=20,
    max_execution_time=700
)

# Streamlit UI components
def main():
    st.title('Gmail Assistant')

    input_command = st.text_input('Enter your command:')
    if st.button('Submit'):
        response = agent_executor.invoke({"input": input_command})
        st.write(response)

if __name__ == '__main__':
    main()
