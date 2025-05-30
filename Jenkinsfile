pipeline {
    agent any
    options {
        skipDefaultCheckout(true)
    }
    stages {
        stage('Clean') {
            steps {
                deleteDir()
                checkout scm
            }
        }
    }
}
