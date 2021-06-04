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
		                    dir("DjangoWebProject2"){
		                        sh "python manage.py test"
		                    }
		                }
		            }
		        }
		     stage('coverage') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    dir("DjangoWebProject2"){
                        sh "python -m coverage run --include='app/*' manage.py test"
                        sh "python -m coverage report"
                    }
                }
            }
        }
		    
			    stage('pylint') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    dir("DjangoWebProject2/DjangoWebProject2"){
                        sh "python -m pylint __init__.py"
		    }
		}
	    }
			    }
			    
		    }
	
	
}
