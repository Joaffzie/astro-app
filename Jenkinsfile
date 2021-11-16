pipeline {
    agent any

    environment {
        BRANCH = "${env.GIT_BRANCH}"
    }

    parameters {
        string(name: 'VERSION', defaultValue: 'None')
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
                sh "docker tag astro-app eu.gcr.io/astro-app-332210/astro-app"
                withDockerRegistry(credentialsId: 'gcr:astro-app', url: 'https://eu.gcr.io') {
                    sh 'docker push eu.gcr.io/astro-app-332210/astro-app'
                }
            }
        }
    }    
    post {
        always {
            cleanWs()
        }
    }
}