import os

import pytest
from dotenv import load_dotenv

from pymerc.client import Client

load_dotenv()

@pytest.fixture()
def client():
    api_token = os.environ.get("API_TOKEN")
    user = os.environ.get("API_USER")

    if not api_token:
        pytest.fail("API_TOKEN environment variable not set")
    elif not user:
        pytest.fail("API_USER environment variable not set")

    client = Client(user, api_token)
    return client