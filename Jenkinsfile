pipipeline{
    agent any
    stages{
         stage("GitHub checkout....") {
            steps {
                script {
 
                    git branch: 'main', url: 'https://github.com/Docalexix/Python-Flask.git' 
                }
            }
        }
        stage("Build docker connecting....."){
            steps{
                sh 'printenv'
                sh 'git version'
                sh 'docker build . -t Docalexix/silverimg'
            }
        }
         stage("push image to DockerHub"){
            steps{

               script {
                
                  
                 withCredentials([string(credentialsId: 'DOCKERID', variable: 'DOCKERID')]) {
                    sh 'docker login -u Docalexix -p ${DOCKERID}'
            }
              sh 'docker push Docalexix/silverimg:latest'
            }
        }
    }
    
      }

    }
}