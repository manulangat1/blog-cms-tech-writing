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
        // stage("Deploy to ec2 instance and run the app") {
        //     steps{
        //         script{
        //             def dockerCmd = 'docker-compose -f docker-compose.prod.yaml up -d --build'
        //             // def dockerCmd = 'docker run redis'
        //             def shellCmd  = "bash ./server-commands.sh"
        //             sshagent(['ec2-server-key']) {
        //                 sh '''
        //                 scp server-commands.sh ec2-user@3.80.45.214:/home/ec2-user
        //                 scp docker-compose.prod.yaml ec2-user@3.80.45.214:/home/ec2-user
        //                 '''
        //                 sh "ssh  -o StrictHostKeyChecking=no ec2-user@3.80.45.214  ${shellCmd}"
        //             }
        //         }
        //     }
        // }

        stage("Deploy to k8s"){
            enviroment{
                AWS_ACCESS_KEY_ID = credentials('jenkins_aws_access_key_id')
                AWS_SECRET_ACCESS_KEY = credentials('jenkins_aws_secret_access_key')
            }
            steps{
                
                script{
                    echo "Deploying to k8s"
                    sh "kubectl create deployment nginx-deployment --image=nginx"
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
