pipeline {
    agent {
        docker {
            image 'python:3.11.4'
        }
    }
    
    stages {
        stage("Install Build Dependencies") {
            sh 'python -m pip install -U setuptools wheel hatch'
        }
        
        stage("Build Python Project") {
            sh 'python -m hatch build'
        }
        
        stage("Publish to PyPi") {
            sh 'python -m hatch publish -r test -u Nater0214'
        }
    }
}