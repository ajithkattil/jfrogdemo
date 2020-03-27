### This Jenkinsfile has been checked in to capture the groovy based pipeline code configured in the Jenkins pipeline job

pipeline {
  #!/usr/bin/env groovy

node ('master') {

    //Clone jfrog_demo  project from GitHub repository
    git url: 'https://github.com/ajithkattil/jfrogdemo', branch: 'master'
    def rtServer = Artifactory.server SERVER_ID
    def buildDepInfo = Artifactory.newBuildInfo()
    def buildInfo = Artifactory.newBuildInfo()
    def tagDockerApp
    def rtDocker
    buildDepInfo.env.capture = true
    // buildDepInfo.env.collect()
    buildInfo.env.capture = true
    // buildInfo.env.collect()
    
    //Build docker image named docker-app 
    stage ('create Docker image') {
           
            tagDockerApp = "${ARTDOCKER_REGISTRY}/jfrog-demo:${env.BUILD_NUMBER}"
            docker.build(tagDockerApp)
            withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: CREDENTIALS, usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD']]) {
                rtDocker = Artifactory.docker server: rtServer
                rtDocker.push(tagDockerApp, REPO, buildInfo) 
                buildInfo.append(buildDepInfo)
                rtServer.publishBuildInfo buildInfo
             }
             // end of with Credentials tag

           }
           //end of stage create Docker image
           
         
     
     //Test docker image
     stage ('Test') {
            
            sh 'docker rmi '+tagDockerApp+' || true'
            rtDocker.pull (tagDockerApp)
            if (testApp(tagDockerApp)) {
                  println "Setting property and promotion"
                  sh 'docker rmi '+tagDockerApp+' || true'
             } else {
                  currentBuild.result = 'UNSTABLE'
                  return
             }
            
     }
     // end of stage test
     
     
     //Scan Build Artifacts in Xray
    stage('Xray Scan') {
         if (XRAY_SCAN == "YES") {
             def xrayConfig = [
                'buildName'     : env.JOB_NAME,
                'buildNumber'   : env.BUILD_NUMBER,
                'failBuild'     : false
              ]
              def xrayResults = rtServer.xrayScan xrayConfig
              echo xrayResults as String
         } else {
              println "No Xray scan performed. To enable set XRAY_SCAN = YES"
         }
         sleep 30
     } 


 stage 'Deploy to GKE Cluster'
    
   // if (KUBE-CLUSTER-DEPLOY == "YES") {
            
//                sh "sed -i 's/hello:latest/hello:${env.BUILD_ID}/g' deployment.yaml"
//                step([$class: 'KubernetesEngineBuilder', projectId: env.PROJECT_ID, clusterName: env.CLUSTER_NAME_TEST, location: env.LOCATION, manifestPattern: 'deployment.yaml', credentialsId: env.CREDENTIALS_ID, verifyDeployments: true])
//            }
    


     
}
// node block close

def testApp (tag) {
    docker.image(tag).withRun('-p 4035:5035') {c ->
        sleep 10
        sh "docker logs ${c.id}"
        
         }
      }


  }
