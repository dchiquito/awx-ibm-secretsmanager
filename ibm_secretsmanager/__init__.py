import collections
from urllib.parse import urljoin

import requests

CredentialPlugin = collections.namedtuple(
    "CredentialPlugin", ["name", "inputs", "backend"]
)


def lookup_secret(**kwargs):
    base_url = kwargs.get("url")
    iam_token = kwargs.get("iam_token")
    uuid = kwargs.get("uuid")
    url = urljoin(base_url, f"/api/v2/secrets/{uuid}")

    session = requests.Session()
    session.headers["Authorization"] = f"Bearer {iam_token}"
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
                "label": "Server URL",
                "type": "string",
            },
            {
                "id": "iam_token",
                "label": "IAM Token",
                "type": "string",
                "secret": True,
            },
        ],
        "metadata": [
            {
                "id": "uuid",
                "label": "Secret UUID",
                "type": "string",
                "help_text": "The name of the key to fetch from IBM Secrets Manager.",
            }
        ],
        "required": ["url", "iam_token", "uuid"],
    },
    backend=lookup_secret,
)
