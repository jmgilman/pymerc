import os

from dotenv import load_dotenv

from pymerc.client import Client

load_dotenv()

# Define api and cache as global variables
client = None


async def main():
    global client

    client = Client(os.environ["API_USER"], os.environ["API_TOKEN"])
