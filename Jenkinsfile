pipeline {

    agent any

    stage ("Update Deployment files") {
        steps {
            sh 'python3 replace-container-names.py BACKEND_IMAGE_NAME=${BACKEND_IMAGE_NAME} FRONTEND_IMAGE_NAME=${FRONTEND_IMAGE_NAME} DB_IMAGE_NAME=${DB_IMAGE_NAME}'
            sh 'kubectl apply -f ./deployments/phonebookapp-backend.deployment.yaml'
            sh 'kubectl apply -f ./deployments/phonebookapp-frontend.deployment.yaml'
            sh 'kubectl apply -f ./deployments/phonebookapp-db.deployment.yaml'
        }
    }
    stage ("Rollout Deployments") {

    }


}