import os

from dotenv import find_dotenv, load_dotenv
from langchain_openai import AzureChatOpenAI

load_dotenv(find_dotenv())


def get_model():
    return AzureChatOpenAI(
        azure_endpoint=os.environ["OPENAI_DEPLOYMENT_ENDPOINT"],
        azure_deployment=os.environ["OPENAI_DEPLOYMENT_NAME"],
        openai_api_version=os.environ["OPENAI_API_VERSION"],
        api_key=os.environ["OPENAI_API_KEY"],
    )
