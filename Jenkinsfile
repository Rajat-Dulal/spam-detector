pipeline {
    agent any

    environment {
        IMAGE_NAME = "spam-detector"
        IMAGE_TAG = "latest"
    }

    stages {
        stage('Clean Workspace') {
            steps {
                echo "🧹 Cleaning workspace before start..."
                cleanWs()
            }
        }

        stage('Build') {
            steps {
                echo "🔧 Building Docker image..."
                sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
            }
        }

        stage('Test') {
            steps {
                echo "🧪 Running Python tests..."
                sh '''
                python -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                python -m unittest discover -s tests
                '''
            }
        }

        stage('Code Quality') {
            steps {
                echo "🧼 Running SonarQube scan..."
                withSonarQubeEnv('MySonarQubeServer') {
                    sh 'sonar-scanner'
                }
            }
        }

        stage('Security Scan') {
            steps {
                echo "🔐 Running Bandit security scan..."
                sh 'bandit -r app'
            }
        }

        stage('Deploy to Test') {
            steps {
                echo "🚀 Deploying container to test environment..."
                sh 'docker run -d -p 5000:5000 --name test-spam-detector $IMAGE_NAME:$IMAGE_TAG'
            }
        }

        stage('Release to Production') {
            steps {
                echo "📦 Tagging image for release..."
                sh '''
                docker tag $IMAGE_NAME:$IMAGE_TAG $IMAGE_NAME:prod
                docker stop test-spam-detector && docker rm test-spam-detector
                docker run -d -p 5001:5000 --name prod-spam-detector $IMAGE_NAME:prod
                '''
            }
        }

        stage('Monitoring') {
            steps {
                echo "📊 Monitoring placeholder (Datadog/Prometheus integration goes here)"
            }
        }
    }

    post {
        always {
            echo "🧹 Cleaning up Docker containers..."
            sh 'docker ps -aq --filter name=spam-detector | xargs -r docker stop | xargs -r docker rm || true'
            echo "🧼 Cleaning workspace after pipeline..."
            cleanWs()
        }
    }
}
