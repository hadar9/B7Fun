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
        timeout(time: 30, unit: 'MINUTES')
    }
    stages {
        stage('Install Application Dependencies') {
            steps {
				withEnv(["HOME=${env.WORKSPACE}"]) {
					sh 'pip3 install -r requirements.txt --user'
				}
            }
        }
        stage('Run Tests') {
            steps {
				dir("B7FunDjango") {
					withEnv(["HOME=${env.WORKSPACE}"]) {
						sh 'python manage.py makemigrations'
						sh 'python manage.py migrate'
						sh 'python manage.py test accounts.tests'
					}
				}
			}
        }
    }
	post {
		always {
			deleteDir()
		}
		success {
			sh 'echo Test ${BUILD_NUMBER} SUCCESS'
		}
		failure {
			sh 'echo Test ${BUILD_NUMBER} Failure'
		}
	}
}