import os
import hvac
'''
export VAULT_URL=https://vault.example.localnet:8200/
export VAULT_TOKEN=REPLACETOKEN
export SECRET_PATH=REPLACE_PATH
'''

print(os.environ['VAULT_URL'])
print(os.environ['VAULT_TOKEN'])
print(os.environ['SECRET_PATH'])
client = hvac.Client()
client = hvac.Client(
 url=os.environ['VAULT_URL'],
 token=os.environ['VAULT_TOKEN'],
 verify=False
)
result = client.read(os.environ['SECRET_PATH'])
print(result["data"]["user"])
print(result["data"]["password"])
print(result["data"]["host"])