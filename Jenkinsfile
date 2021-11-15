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
                sh 'docker run -d --name astro-app -p 5000:5000 astro-app'
                sh 'sleep 5'
                sh 'curl astro-app:5000'
            }
        }
        stage('Publish') {
            steps {
                echo 'Publishing...'
            }

        }
    }    
}