pipeline {
    agent any

    environment {
        IMAGE_NAME = 'spam-detector-app'
    }

    tools {
        sonarQube 'SonarScanner'  // Name from Jenkins Global Tool Config
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

        stage('Code Quality (SonarQube)') {
            environment {
                SONAR_USER_HOME = "${env.WORKSPACE}/.sonar" // prevent issues with permissions
            }
            steps {
                withSonarQubeEnv('LocalSonar') {
                    sh '/opt/sonar-scanner/bin/sonar-scanner'
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
