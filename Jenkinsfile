pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building Student Result Analyzer...'
                bat 'python student_result.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests...'
                bat 'python -m unittest discover -v'
            }
        }

        stage('Package') {
            steps {
                echo 'Creating project package...'
                bat 'if not exist output mkdir output'
                bat 'powershell Compress-Archive -Path *.py -DestinationPath output\\student-result.zip -Force'
            }
        }

        stage('Archive') {
            steps {
                echo 'Archiving build artifact...'
                archiveArtifacts artifacts: 'output/student-result.zip', fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'BUILD SUCCESSFUL! 🎉'
        }

        failure {
            echo 'BUILD FAILED! ❌ Check the console output.'
        }
    }
}