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
        stage("Running the server 3 "){
            steps{
                script{
                    echo "Hello world, here i am"
                }
            }
        }
    }
}
