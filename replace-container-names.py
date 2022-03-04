import sys
import yaml


if __name__ == "__main__":
    data = dict([arg.split('=', maxsplit=1) for arg in sys.argv[1:]])

    with open("./deployments/phonebookapp-backend.deployment.yaml", "r") as f:
        backend_deployment = yaml.safe_load(f)

    with open("./deployments/phonebookapp-frontend.deployment.yaml", "r") as f:
        frontend_deployment = yaml.safe_load(f)

    with open("./deployments/phonebookapp-db.deployment.yaml", "r") as f:
        db_deployment = yaml.safe_load(f)

    backend_deployment["spec"]["template"]["spec"]["containers"][0]["image"] = data["BACKEND_IMAGE_NAME"]
    backend_deployment["spec"]["template"]["spec"]["containers"][0]["env"][3]["value"] = data["DB_HOST_IP"]

    frontend_deployment["spec"]["template"]["spec"]["containers"][0]["image"] = data["FRONTEND_IMAGE_NAME"]

    db_deployment["spec"]["template"]["spec"]["containers"][0]["image"] = data["DB_IMAGE_NAME"]


    with open("./deployments/phonebookapp-backend.deployment.yaml", "w") as f:
        yaml.dump(backend_deployment, f)

    with open("./deployments/phonebookapp-frontend.deployment.yaml", "w") as f:
        yaml.dump(frontend_deployment, f)

    with open("./deployments/phonebookapp-db.deployment.yaml", "w") as f:
        yaml.dump(db_deployment, f)