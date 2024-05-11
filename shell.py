import os

from pymerc.client import Client

# Define api and cache as global variables
client = None

async def main():
    global client

    client = Client(os.environ["API_USER"], os.environ["API_TOKEN"])


