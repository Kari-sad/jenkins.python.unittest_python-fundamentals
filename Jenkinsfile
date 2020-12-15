// Powered by Infostretch 

timestamps {

node () {

	stage ('Freestyle Project with python - Checkout') {
 	 checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '', url: 'https://github.com/Kari-sad/jenkins.python.unittest_python-fundamentals.git']]]) 
	}
	stage ('Freestyle Project with python - Build') {
 	
             powershell "python -m unittest discover -s ./src/test/ -p '*_test.py'"
	}
}
}