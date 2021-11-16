pipeline {
    agent any

    environment {
        BRANCH = "${env.GIT_BRANCH}"
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                // sh 'docker build -t astro-app ./app'
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
                echo "${BRANCH}"
                withDockerRegistry(credentialsId: 'gcr:astro-app', url: 'https://eu.gcr.io') {
                    
                }
            }
        }
    }    
}