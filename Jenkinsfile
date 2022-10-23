pipeline{
    agent any
    stages{
        stage("Init stage") {
            steps {
                script {
                    echo "Hello world ${BRANCH_NAME}"
                }
            }
        }
        stage("Running the server "){
            steps{
                script{
                    echo "Hello world, here i am"
                    sh "docker ps"
                }
            }
        }
        stage("Login to dockerhub and push the images"){
            steps{
                script{
                    withCredentials([usernamePassword(credentialsId:"dockerhub-repo", usernameVariable:"USER", passwordVariable:"PASS")]) {
                        sh '''
                        docker system prune -a -f
                        docker-compose -f docker-compose.dev.yaml up --build   -d
                        echo $PASS | docker login -u $USER --password-stdin
                        docker-compose -f docker-compose.dev.yaml push
                         '''
                        // sh '''
                        //  echo $PASS | docker login -u $USER --password-stdin
                        // '''
                    }
                    echo "Hello world, here i am"
                }
            }
        }
    }
    post{
        always{
            echo "Hello there"
        }
    }
}
