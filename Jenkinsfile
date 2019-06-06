pipeline {
	agent any
    
    stages {
        stage('Run build script'){
            parallel{
                stage('Run linux build script') {
                    agent {
                        label "linux && docker"
                    }
                    steps {
                        checkout scm
                        sh '''./build.sh'''
                    }
                }
                stage ('Run windows build script'){
                    agent {
                        label "windows"
                    }
                    steps{
                        checkout scm
                        bat '''path
                        C:\\Python37-32\\python.exe -m pip install --upgrade pip

                        pip install pipenv

                        pipenv --python 3.7
                        pipenv lock --pre
                        pipenv sync

                        pipenv install pyinstaller
                        pipenv run pyinstaller -F vropscaali.py'''

                    }
                }
            }
	}
    }
} 
