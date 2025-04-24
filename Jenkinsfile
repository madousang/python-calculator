pipeline {
    agent { label 'node1' }

    tools {
        git 'DefaultGit' // le nom défini dans Global Tool Configuration
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checkout...'
                git branch: 'main', url: 'https://github.com/madousang/python-calculator.git'
            }
        }

//         stage('Compile') {
//             steps {
//                 echo 'Compilation...'
//                 sh "./gradlew compileJava"
//             }
//         }

        stage("Unit test") {
            steps {
                echo 'Test...'
                sh "pytest"
            }
        }
    }
}
