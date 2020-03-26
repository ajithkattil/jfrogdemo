pipeline {
  agent  any

    stages {
       stage('Create Docker Image')  {
           steps {
                  echo  'Creating Docker image of the Python tool '
                  sh "/usr/local/bin/docker build . -t jfrog_demo:1"
                }
              }
            }
          }
