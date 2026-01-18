pipeline {
    agent any

    environment {
        IMAGE_NAME = "devops-portfolio"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-portfolio:latest .'
            }
        }

        stage('Smoke Test') {
            steps {
                sh 'docker run --rm devops-portfolio:latest python -c "print(\'Container is running\')"'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker compose down || true
                    docker compose up -d --build
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Deployment successful'
        }
        failure {
            echo '❌ Deployment failed'
        }
        always {
            sh 'docker system prune -f'
        }
    }
}
