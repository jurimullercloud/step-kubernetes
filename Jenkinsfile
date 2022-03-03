pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS=credentials('dockerhub-access')
    }

    stages {
        stage ("Login to DockerHub Registry") {
            steps {
                sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
            }
        }

        stage ("Update Deployment files") {
            steps {
                script {
                    env.DB_HOST_IP = sh('kubectl get svc ${DB_SERVICE_NAME} -o jsonpath=\'{.spec.clusterIP}\'')
                }
                sh 'pip3 install -r requirements.txt'
                sh 'python3 replace-container-names.py BACKEND_IMAGE_NAME=${BACKEND_IMAGE_NAME} FRONTEND_IMAGE_NAME=${FRONTEND_IMAGE_NAME} DB_IMAGE_NAME=${DB_IMAGE_NAME} DB_HOST_IP=$DB_HOST_IP'

            }
        }
        stage ("Rollout Deployments") {
            steps {
                sh 'kubectl apply -f ./deployments/phonebookapp-db.deployment.yaml'
                sh 'kubectl apply -f ./deployments/phonebookapp-backend.deployment.yaml'
                sh 'kubectl apply -f ./deployments/phonebookapp-frontend.deployment.yaml'
            }
        }

    }
}