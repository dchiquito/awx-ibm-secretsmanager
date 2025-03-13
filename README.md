# awx-ibm-secretsmanager
AWX credential plugin for IBM Secrets Manager

Inspired by https://github.com/ansible/awx-custom-credential-plugin-example

# Installation

```
awx-python -m pip install git+https://github.com/dchiquito/awx-ibm-secretsmanager
awx-manage setup_managed_credential_types
```

Then restart the application to pick up the changes.

In a local development docker-compose environment, prefix those commands with `docker exec -it tools_awx_1`:

```
docker exec -it tools_awx_1 awx-python -m pip install git+https://github.com/dchiquito/awx-ibm-secretsmanager
docker exec -it tools_awx_1 awx-manage setup_managed_credential_types
```

