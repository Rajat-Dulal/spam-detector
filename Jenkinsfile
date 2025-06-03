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

        stage('Run Unit Tests') {
            steps {
                script {
                    docker.image(IMAGE_NAME).inside {
                        sh '''
                            pytest --junitxml=results.xml || true
                        '''
                    }
                }
            }
        }

        stage('Publish Test Results') {
            steps {
                junit 'results.xml'
            }
        }

        stage('List Docker Images') {
            steps {
                sh 'docker images'
            }
        }
    }
}
