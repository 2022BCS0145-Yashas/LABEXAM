pipeline {
    agent any

    environment {
        IMAGE_NAME = "yashas080504/wine-quality-api"
    }

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/2022BCS0145-Yashas/LABEXAM'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python train.py'
            }
        }

        stage('Evaluate Model') {
            steps {
                sh 'python evaluate.py'
            }
        }

        stage('Print Details') {
            steps {
                echo "Name: Yashas Kumar S"
                echo "Roll No: 2022BCS0145"
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

    stage('Push to DockerHub') {
        steps {
            withCredentials([usernamePassword(
                credentialsId: 'dockerhub-creds',
                usernameVariable: 'DOCKER_USER',
                passwordVariable: 'DOCKER_PASS'
            )]) {
                sh '''
                echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                docker push yashas080504/wine-api
                '''
            }
        }
    }
    }
}