import collections
from urllib.parse import urljoin

import requests

CredentialPlugin = collections.namedtuple(
    "CredentialPlugin", ["name", "inputs", "backend"]
)


def generate_access_token(api_key):
    session = requests.Session()
    session.headers["Content-Type"] = "application/x-www-form-urlencoded"
    url = "https://iam.cloud.ibm.com/identity/token"
    data = f"grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey={api_key}"

    response = session.post(url, data)
    # raise_for_status(response)
    response.raise_for_status()

    json = response.json()
    return json["access_token"]


def lookup_secret(**kwargs):
    base_url = kwargs.get("url")
    uuid = kwargs.get("uuid")
    url = urljoin(base_url, f"/api/v2/secrets/{uuid}")

    api_key = kwargs.get("api_key")
    token = generate_access_token(api_key)

    session = requests.Session()
    session.headers["Authorization"] = f"Bearer {token}"
    session.headers["Accept"] = "application/json"

    response = session.get(url)
    # raise_for_status(response)
    response.raise_for_status()

    json = response.json()
    return json


ibm_secretsmanager_plugin = CredentialPlugin(
    "IBM Secrets Manager",
    inputs={
        "fields": [
            {
                "id": "url",
                "label": "Service API Endpoint",
                "type": "string",
            },
            {
                "id": "api_key",
                "label": "API Key",
                "type": "string",
                "secret": True,
            },
        ],
        "metadata": [
            {
                "id": "uuid",
                "label": "Secret UUID",
                "type": "string",
                "help_text": "The UUID of the secret to fetch from IBM Secrets Manager.",
            }
        ],
        "required": ["url", "api_key", "uuid"],
    },
    backend=lookup_secret,
)
