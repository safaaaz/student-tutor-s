pipeline {
agent {
		        docker {
		            image 'python:3.7.0'
		

		        }
		    }
		    stages {
		        stage('build') {
		            steps {
		                withEnv(["HOME=${env.WORKSPACE}"]) {
		                    sh "python -m pip install -r DjangoWebProject2/requirements.txt --user"
		                }
		            }
		        }
		        stage('test') {
		            steps {
		                withEnv(["HOME=${env.WORKSPACE}"]) {
		                    dir("DjangoWebProject2/app"){
		                        sh "python manage.py test"
		                    }
		                }
		            }
		        }
		    }
