pipeline {
    agent {
		docker {
			image 'leorrose13/python-pillow-alpine:jenkins'
		}
	}
	triggers {
        githubPush()
    }
	options {
		skipDefaultCheckout(true)
        timeout(time: 60, unit: 'MINUTES')
    }
    stages {
		stage('Repository Fetch') {
			steps {
				checkout scm
			}
		}
        stage('Application Setup') {
            steps {
				withEnv(["HOME=${env.WORKSPACE}"]) {
					sh 'pip3 install -r requirements.txt --user'
					dir("B7FunDjango") {
						sh 'python manage.py makemigrations'
						sh 'python manage.py migrate'
					}
				}
            }
        }
		stage('Run Tests') {
            steps {
				dir("B7FunDjango") {
					withEnv(["HOME=${env.WORKSPACE}"]) {
						sh "python -m coverage run --source='.' manage.py test"
					}
				}
			}
        }
		
		stage('Metric 1 - unit test coverage') {
			steps {
				dir("B7FunDjango") {
					withEnv(["HOME=${env.WORKSPACE}"]) {
						sh 'python -m coverage xml -o ./reports/coverage.xml'
						sh 'python -m coverage report'
						//cobertura coberturaReportFile: 'reports/coverage.xml'
					}
				}
			}
		}
		
		stage('Metric 2 - pylint python code convention') {
			steps {
				dir("B7FunDjango") {
					withEnv(["HOME=${env.WORKSPACE}"]) {
						sh 'python -m pylint --load-plugins=pylint_django --disable=R0801 accounts'
					}
				}
			}
		}
		
		stage('Metric 3 - Test Trend Chart') {
			steps {
				dir("B7FunDjango") {
					junit allowEmptyResults: true, testResults: 'reports/unittest.xml'
				}
			}
		}
		
    }
	post {
		failure{
			mail to: 'B7FunService@gmail.com',
			subject: "Failed: Job '${env.JOB_NAME}' ['${env.BUILD_NUMBER}']",
			body: 'Failed: Job ${env.JOB_NAME} [${env.BUILD_NUMBER}]: Check console output at ${env.BUILD_URL} ${env.JOB_NAME} [${env.BUILD_NUMBER}]'
		}
		success{
			mail to: 'B7FunService@gmail.com',
			subject: "SUCCESS: Job '${env.JOB_NAME}' ['${env.BUILD_NUMBER}']",
			body: "SUCCESS: Job '${env.JOB_NAME}' ['${env.BUILD_NUMBER}']: Check console output at '${env.BUILD_URL}' '${env.JOB_NAME}' ['${env.BUILD_NUMBER}']"
		}
	}
}