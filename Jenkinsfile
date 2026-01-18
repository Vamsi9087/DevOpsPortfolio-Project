pipeline {
    agent any
<<<<<<< HEAD
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
=======

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
                sh """
                    docker build -t ${IMAGE_NAME}:latest .
                """
            }
        }

        stage('Smoke Test') {
            steps {
                sh """
                    docker run --rm ${IMAGE_NAME}:latest python -c "print('App container started successfully')"
                """
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                sh """
                    docker compose down || true
                    docker compose up -d --build
                """
            }
        }
    }

    post {
        success {
            echo 'Deployment successful 🎉'
        }
        failure {
            echo 'Pipeline failed ❌'
        }
        always {
            sh 'docker system prune -f'
        }
    }
>>>>>>> b7b2497 (Updated UI and backend logic)
}
