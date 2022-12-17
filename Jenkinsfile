pipeline {
    agent any
    parameters {
        string defaultValue: '300', name: 'INTERVAL'
    }
    environment {
        AWS_CRED = credentials('credentials')
        registry = "ofirbh91/jb_final_lab"
        dockerimage = ''
        DOCKERHUB_CRED = credentials('DOCKER_CRED')
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
                script {
                    dockerImage = docker.build(registry + ":${currentBuild.number}.0","-f Dockerfile .")
                }
        }

    }
        stage('Deploy') {
            steps {
                sh "docker run -itd --log-driver=json-file --name aws --env INTERVAL=${params.INTERVAL} $registry:${currentBuild.number}.0"
                sh "docker logs --follow aws"
            }
        }
        stage('Deploy log') {
            steps {
                echo "Printing docker output"
                sleep 2
                sh "docker logs aws"
            }
        }
        
        stage('Login to dockerhub'){
            steps{
                sh 'docker login -u $DOCKERHUB_CRED_USR -p $DOCKERHUB_CRED_PSW'
            }
        }
        stage('Push image to registry'){
            steps{
                sh (script : """docker push aws $registry:${currentBuild.number}.0""", returnStdout: false)
                sleep 5
                sh 'docker logout'
            }
        }
        
}
}
