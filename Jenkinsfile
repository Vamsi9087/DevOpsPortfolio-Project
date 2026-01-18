pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t devops-portfolio .'
            }
        }
        stage('Test') {
            steps {
                sh 'docker run devops-portfolio python -m pytest'  # Add tests later
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}
