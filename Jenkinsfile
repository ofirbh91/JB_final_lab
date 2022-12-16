pipeline {
    agent any
    parameters {
        string defaultValue: '300', name: 'INTERVAL'
    }
    environment {
        CRED = credentials('CRED')
    }

    stages {
        stage('Init') {
            steps {
                cleanWs()
                sh "docker kill aws || true"
                sh "docker rm aws || true"
                sh "docker rmi -f aws || true"
            }
        }
        stage('SCM') {
            steps {
                git url: 'https://github.com/ofirbh91/CICDProject.git', branch: 'main'
            }
        }
        stage('Build') {
            steps {
                sh "cat $CRED | tee credentials"
                sh "docker build -t aws ."
            }
        }
        stage('Deploy') {
            steps {
                sh "docker run -itd --name aws --env INTERVAL=${params.INTERVAL} aws"
                sh "docker logs --follow aws"
            }
        }
    }
}
