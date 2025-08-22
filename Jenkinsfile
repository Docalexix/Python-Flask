pipeline{
    agent any
    stages{
         stage("GitHub checkout") {
            steps {
                script {
 
                    git branch: 'main', url: 'https://github.com/Docalexix/Python-Flask.git' 
                }
            }
        }
        stage("Build docker on going"){
            steps{
                sh 'printenv'
                sh 'git version'
                sh 'docker build . -t Docalexix/silverimg'
            }
        }
         stage("push image to DockerHub"){
            steps{

               script {
                  
                 withCredentials([string(credentialsId: 'alexID', variable: 'alexID')]) {
                    sh 'docker login -u Docalexix -p ${alexID}'
            }
              sh 'docker push Docalexix/silverimg:latest'
            }
        }
    }
    }
}

    

