pipeline {
    agent any

    environment {
        // Define Environment Variables
        PYTHON_VERSION = '3.8'
        IMAGE_NAME = 'MaterialDashboard'
        REGISTRY_URL = 'http://192.168.33.10:5000'
        REGISTRY_CREDENTIALS_ID = 'lionelrupesh'
        REPO_URL = 'https://github.com/lionelrupesh/creativeTimDjangoAdmin.git'
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Git CheckOut"
                git "${REPO_URL}"
            }
        }

        stage('Build and Test') {
            steps {
                echo "Setting Virtual Environment"
                sh "python${PYTHON_VERSION} -m venv venv"
                sh "venv/bin/activate"
                
                echo "Installing dependencies and run tests"
                sh 'pip install -r requirements.txt'
                // sh 'python -m unittest discover -s tests -p "test_*.py"'
            }
        }

        stage('Docker Build') {
            steps {
                echo "Building Docker Image"
                sh '''
                original_pwd=$(pwd -P)
                cd webdesign/material-dashboard-master
                docker image build -t ${IMAGE_NAME}:${BUILD_NUMBER} .
                cd $original_pwd
                '''
                
            }
        }

        stage('Deploy'){
          steps {
            echo "We are deploying the app"
            sh '''
            docker container stop PythonContainer || true
            docker container rm PythonContainer || true
            docker container run -itd --name PythonContainer -p 8089:8080 $IMAGE_NAME:$BUILD_NUMBER
            '''
      }
     }
        stage('Publish to Registry') {
            steps {
                echo "Pushing Docker Image to registry"
                sh '''
                docker image tag $IMAGE_NAME:latest $REGISTRY_URL/$IMAGE_NAME:V1
                docker image push $REGISTRY_URL/$IMAGE_NAME:V1
                '''
                    }
                }
    }

        

    post {
        success {
            echo 'Pipeline successfully executed!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
