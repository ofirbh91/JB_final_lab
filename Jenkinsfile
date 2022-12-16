pipeline {
    agent any
    parameters {
        string defaultValue: '300', name: 'INTERVAL'
    }
    environment {
        AWS_CRED = credentials('credentials')
        registry = ofirbh91/jb_final_lab
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
                sh "cat $CRED | tee credentials"
                sleep 3
                script{
                    dockerimage = docker.build(registry + ":${currentbuild.number}.0", "-f Dockerfile .")
                    echo "$(dockerimage)"
                }
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
