pipeline {
    agent any

    environment {
        BRANCH = "${env.GIT_BRANCH}"
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'docker build -t astro-app .'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
        stage('Publish') {
            steps {
                echo 'Publishing...'
            }

        }
    }    
}