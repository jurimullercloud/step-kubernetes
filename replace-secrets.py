import sys
import base64
import yaml

if __name__ == "__main__":
    data = dict([arg.split('=', maxsplit=1) for arg in sys.argv[1:]])

    print(data)
    with open("./phonebookapp-secrets.yaml", "r") as f:
        secrets_yaml = yaml.safe_load(f)

    secrets_yaml["data"]["POSTGRES_USER"] = base64.b64encode(data["POSTGRES_USER"].encode("ascii")).decode("ascii")
    secrets_yaml["data"]["POSTGRES_PASSWORD"] = base64.b64encode(data["POSTGRES_PASSWORD"].encode("ascii")).decode("ascii")
    secrets_yaml["data"]["POSTGRES_DB"] = base64.b64encode(data["POSTGRES_DB"].encode("ascii")).decode("ascii")
    secrets_yaml["data"]["DB_SERVICE_NAME"] = base64.b64encode(data["DB_SERVICE_NAME"].encode("ascii")).decode("ascii")
    secrets_yaml["data"]["JWT_SECRET_KEY"] = base64.b64encode(data["JWT_SECRET_KEY"].encode("ascii")).decode("ascii")

    with open("./phonebookapp-secrets.yaml", "w") as f:
        yaml.dump(secrets_yaml, f)
