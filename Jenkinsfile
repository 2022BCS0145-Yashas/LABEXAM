pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'apt install python3.13-venv'
                sh 'python3 -m venv env'
                sh 'source env/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python scripts/train.py'
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