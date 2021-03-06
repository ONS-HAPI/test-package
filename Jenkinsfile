#!groovy
// Checkout the Jenkinsfile docs at https://jenkins.io/doc/book/pipeline/jenkinsfile/
// ONS docs on Jenkins are at https://collaborate2.ons.gov.uk/confluence/pages/viewpage.action?spaceKey=REG&title=Jenkins

// Global scope required for multi-stage persistence
def artServer = Artifactory.server "art-p-01"
def buildInfo = Artifactory.newBuildInfo()
def agentPython3Version = 'python_3.6.1'

def pushToPyPiArtifactoryRepo(String projectName, String sourceDist = 'dist/*', String artifactoryHost = 'art-p-01') {
    withCredentials([usernamePassword(credentialsId: env.ARTIFACTORY_CREDS, usernameVariable: 'ARTIFACTORY_USER', passwordVariable: 'ARTIFACTORY_PASSWORD')]){
        sh "curl -u ${ARTIFACTORY_USER}:\${ARTIFACTORY_PASSWORD} -T ${sourceDist} 'http://${artifactoryHost}/artifactory/${env.ARTIFACTORY_PYPI_REPO}/${projectName}/'"
    }
}

pipeline {
    libraries {
            // Useful library from ONS internal GitLab
            lib('jenkins-pipeline-shared')
        }

    // Define env variables
    environment {
        ARTIFACTORY_CREDS = 'ARTIFACTORY_CREDS' // set in Jenkins Credentials
        ARTIFACTORY_PYPI_REPO = 'DAP-CVD19-SCH'
    }

    // Don't use default checkout process, as we define it as a stage below
    options {
        skipDefaultCheckout true
    }

    // Agent must always be set at the top level of the pipeline
    // We're not picky
    agent any

    stages {
        // Checkout stage to fetch code from  GitLab
        stage("Checkout") {
            // We have to specify an appropriate slave for each stage
            // Choose from download, build, test, deploy
            agent { label "download.jenkins.slave" }
            steps {
                colourText("info", "Checking out code from source control.")
                checkout scm
                // Stash the files that have been checked out, for use in subsequent stages
                stash name: "Checkout", useDefaultExcludes: false
            }

        }
        stage("Build") {
            agent { label "build.${agentPython3Version}" }
            steps {
                unstash name: 'Checkout'
                colourText('info', "Building package")
                sh 'pip3 install wheel==0.29.0'  // Later versions not compatible with Python 3.6
                sh 'python3 setup.py build bdist_wheel'
                stash name: "Build", useDefaultExcludes: false
            }
        }
        stage("Deploy") {
            when { tag "v*" }
            agent { label "deploy.jenkins.slave" }
            steps {
                unstash name: "Build"
                colourText('info', "Deploying to Artifactory")
                pushToPyPiArtifactoryRepo("${buildInfo.name}")
            }
        }
    }
}
