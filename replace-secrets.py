import sys
import yaml

if __name__ == "__main__":
    data = dict([arg.split('=', maxsplit=1) for arg in sys.argv[1:]])

    print(data)
    with open("./phonebookapp-secrets.yaml", "r") as f:
        secrets_yaml = yaml.safe_load(f)

    secrets_yaml["data"]["POSTGRES_USER"] = data["POSTGRES_USER"]
    secrets_yaml["data"]["POSTGRES_PASSWORD"] = data["POSTGRES_PASSWORD"]
    secrets_yaml["data"]["POSTGRES_DB"] = data["POSTGRES_DB"]
    secrets_yaml["data"]["DB_SERVICE_NAME"] = data["DB_SERVICE_NAME"]
    secrets_yaml["data"]["JWT_SECRET_KEY"] = data["JWT_SECRET_KEY"]

    with open("./phonebookapp-secrets.yaml", "w") as f:
        yaml.dump(secrets_yaml, f)
