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
                sh '''
                    docker rm -f spam-detector-prod || true
                    docker rm -f spam-detector-test || true
                    docker compose down || true
                    docker compose up -d
                '''
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
                    for (int i = 0; i < 5; i++) {
                        def status = sh(script: 'curl -s -o /dev/null -w "%{http_code}" http://localhost:5050/health', returnStdout: true).trim()
                        if (status == "200") {
                            isReady = true
                            echo "✅ App is healthy (HTTP 200)"
                            break
                        } else {
                            echo "Waiting for app to become ready (attempt ${i + 1})"
                            sleep 5
                        }
                    }

                    if (!isReady) {
                        error("❌ ALERT: App in production not responding on /health!")
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
