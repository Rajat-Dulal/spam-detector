pipeline {
    agent any

    environment {
        IMAGE_NAME = 'spam-detector-app'
    }

    stages {
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
