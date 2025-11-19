pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main',
                    url: 'https://github.com:LulukDWiKuncoro/BNSP.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t bnsp-app:latest .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop bnsp-app || true'
                sh 'docker rm bnsp-app || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d --name bnsp-app -p 80:5000 bnsp-app:latest'
            }
        }
    }
}
