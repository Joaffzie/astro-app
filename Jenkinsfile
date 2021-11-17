def TAG
pipeline {
    agent any

    environment {
        BRANCH = "${env.GIT_BRANCH}"
    }

    parameters {
        string(name: 'VERSION', defaultValue: '1.0')
    }

    stages {
        stage('Versioning') {
            steps {
                script {
                    lasttag = sh(script: "git tag -l --sort=version:refname \"${params.VERSION}.*\" | tail -1", returnStdout: true).trim()
                    if (lasttag.isEmpty()) {
                        newtag = "${params.VERSION}.0"
                        TAG = sh(script: "echo ${newtag}", returnStdout: true)
                    } else {
                        newtag = lasttag.split('\\.')
                        newtag[2] = newtag[2].toInteger() + 1
                        newtag = newtag.join('.')
                        TAG = sh(script: "echo ${newtag}, returnStdout: true")
                    }
                }
            }
        }

        stage('Build') {
            steps {
                script{
                    if (BRANCH.matches('dev')) {
                        echo 'Building...'
                        // sh 'docker build -t astro-app ./app'
                    }
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Testing...'
                // sh 'docker-compose up -d'
                // sh 'sleep 5'
                // sh 'curl app:5000'
            }
        }
        stage('Publish') {
            steps {
                echo 'Publishing...'
                echo "${TAG}"
                sh "docker tag astro-app eu.gcr.io/astro-app-332210/astro-app:${TAG}"
                withDockerRegistry(credentialsId: 'gcr:astro-app', url: 'https://eu.gcr.io') {
                    sh "docker push eu.gcr.io/astro-app-332210/astro-app:${TAG}"
                }
                sh "git tag ${TAG}"
            }
        }
    }    
    post {
        always {
            cleanWs()
        }
    }
}