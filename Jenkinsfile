pipeline {
    agent any
    parameters {
        string defaultValue: '300', name: 'INTERVAL'
    }
    environment {
        AWS_CRED = credentials('credentials')
        registry = "ofirbh91/jb_final_lab"
        dockerimage = ''
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
                git url: 'https://github.com/ofirbh91/JB_final_lab.git', branch: 'main'
            }
        }
        stage('Build') {
            steps {
                sh "cat $AWS_CRED | tee credentials"
                sleep 3
                script{
                    dockerImage = docker.build(registry + ":${currentBuild.number}.0","-f Dockerfile .")
                }
            }
        }

    }
}
