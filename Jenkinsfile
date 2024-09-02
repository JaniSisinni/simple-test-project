// Jenkinsfile

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Check out the code from Git
                git url: 'https://github.com/JaniSisinni/simple-test-project.git'
            }
        }

        stage('Build') {
            steps {
                // No build step needed for a simple Python script
                echo 'Build step is not required for this project.'
            }
        }

        stage('Test') {
            steps {
                // Run the unit tests
                bat 'python -m unittest test_hello.py'
            }
        }

        stage('Deploy') {
            steps {
                // Simulate deployment by copying the script to a deploy directory
                bat 'if not exist deploy mkdir deploy && copy hello.py deploy/'
                echo 'Deployment complete.'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
