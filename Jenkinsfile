pipeline {
    agent any

    environment {
        IMAGE_NAME = 'spam-detector-app'
        DOCKER_REGISTRY = 'local' // Replace with DockerHub later if needed
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/Rajat-Dulal/spam-detector.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build(IMAGE_NAME)
                }
            }
        }

        stage('List Docker Images') {
            steps {
                sh 'docker images'
            }
        }
    }
}
