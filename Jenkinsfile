pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
        IMAGE_NAME = "yashas080504/wine-quality-api"
    }

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/2022BCS0145-Yashas/lab4'
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
                sh """
                echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                docker push $IMAGE_NAME
                """
            }
        }
    }
}