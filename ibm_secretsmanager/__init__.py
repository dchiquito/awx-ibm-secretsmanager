import collections
from urllib.parse import urljoin

import requests

CredentialPlugin = collections.namedtuple(
    "CredentialPlugin", ["name", "inputs", "backend"]
)


def lookup_secret(**kwargs):
    base_url = kwargs.get("url")
    iam_token = kwargs.get("iam_token")
    id = kwargs.get("id")

    print(base_url, iam_token, id)

    session = requests.Session()
    session.headers["Authorization"] = f"Bearer {iam_token}"
    session.headers["Accept"] = "application/json"
    url = urljoin(base_url, f"/api/v2/secrets/${id}")
    response = session.get(url)
    # raise_for_status(response)
    json = response.json()
    print(json)
    return json["payload"]


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
                "id": "identifier",
                "label": "Identifier",
                "type": "string",
                "help_text": "The name of the key to fetch from IBM Secrets Manager.",
            }
        ],
        "required": ["url", "iam_token", "id"],
    },
    backend=lookup_secret,
)
