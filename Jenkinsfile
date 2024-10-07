node {
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    // Replace 'SonarScanner' with the actual name you gave to the SonarQube Scanner tool in Jenkins
    def scannerHome = tool 'SonarScanner';
    withSonarQubeEnv() {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
}

