pipeline {
    agent any
    environment {
    DOCKERHUB_CREDENTIALS = credentials('test-dockerhub')
    }
    stages {
        stage('SCM Checkout') {
            steps{
			checkout([$class: 'GitSCM', branches: [[name: '*/main']],
			userRemoteConfigs: [[url: 'https://github.com/geralyona/QA_automation.git']]])
            }
        }

        stage('Build docker image') {
            steps {
                sh 'docker build -t geralyona/qa-automation:$BUILD_NUMBER .'
            }
        }
        stage('login to dockerhub') {
            steps{
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('push image') {
            steps{
                sh 'docker push geralyona/qa-automation:$BUILD_NUMBER'
            }
        }
}
post {
        always {
            sh 'docker logout'
        }
    }
}
