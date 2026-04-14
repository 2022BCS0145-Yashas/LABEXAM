pipeline {
    agent any

    stages {

        stage('Run Training in Docker') {
            steps {
                sh '''
                docker build -t temp-ml .
                docker run temp-ml python train.py
                '''
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
                sh 'docker build -t yashas080504/wine-api .'
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