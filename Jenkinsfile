pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh '''
                echo "Building Docker image..."
                docker build -t bnsp-app:latest .
                '''
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                echo "Stopping old container..."
                docker stop bnsp-app || true
                docker rm bnsp-app || true
                '''
            }
        }

        stage('Run New Container') {
            steps {
                sh '''
                echo "Running new container..."
                docker run -d --name bnsp-app -p 80:5000 bnsp-app:latest
                '''
            }
        }
    }
}

