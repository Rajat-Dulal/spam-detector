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

        stage('Code Quality (SonarQube)') {
            environment {
                SONAR_USER_HOME = "${env.WORKSPACE}/.sonar"
            }
            steps {
                withSonarQubeEnv('LocalSonar') {
                    sh '/opt/sonar-scanner/bin/sonar-scanner'
                }
            }
        }

        stage('Security Scan (Bandit)') {
            steps {
                script {
                    docker.image(IMAGE_NAME).inside {
                        sh '''
                            bandit -r . -f json -o bandit-report.json || true
                            cat bandit-report.json
                        '''
                    }
                    archiveArtifacts artifacts: 'bandit-report.json', fingerprint: true
                }
            }
        }

        stage('Deploy to Test Environment') {
            steps {
                script {
                    echo "✅ Using working directory: ${env.WORKSPACE}"
                }
                dir("${env.WORKSPACE}") {
                sh '''
                    docker rm -f spam-detector-prod || true
                    docker rm -f spam-detector-test || true
                    docker compose down || true
                    docker compose up -d
                '''
                }
            }
        }
        
        stage('Release to Production') {
            steps {
                sh '''
                    docker rm -f spam-detector-prod || true
                    docker run -d --name spam-detector-prod -p 5050:5000 spam-detector-app
                '''
            }
        }

        stage('Monitoring & Alerting') {
            steps {
                script {
                    def isReady = false
                    def maxRetries = 5

                    for (int i = 0; i < maxRetries; i++) {
                        def statusCode = sh(
                            script: 'curl -s -o /dev/null -w "%{http_code}" http://spam-detector-prod:5000/health || echo "fail"',
                            returnStdout: true
                        ).trim()

                        echo "Response: ${statusCode}"

                        if (statusCode == "200") {
                            echo "✅ App is healthy (HTTP 200)"
                            isReady = true
                            break
                        } else {
                            echo "❌ App not ready (got '${statusCode}'), retrying (${i + 1}/${maxRetries})..."
                            sleep time: 5, unit: 'SECONDS'
                        }
                    }

                    if (!isReady) {
                        error("❌ ALERT: App not responding on /health after ${maxRetries} attempts.")
                    }
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
