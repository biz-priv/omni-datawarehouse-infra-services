pipeline {
    agent { label 'ecs' }
    stages {
        stage('Set parameters') {
            steps {
                script{
                    echo "GIT_BRANCH: ${GIT_BRANCH}"
                    echo sh(script: 'env|sort', returnStdout: true)
                    if ("${GIT_BRANCH}".startsWith("PR-")){
                        if("${CHANGE_TARGET}".contains("develop")){
                            env.ENVIRONMENT=env.getProperty("environment_develop")
                        } else if("${CHANGE_TARGET}".contains("devint")){
                            env.ENVIRONMENT=env.getProperty("environment_devint")
                        } else if("${CHANGE_TARGET}".contains("master")){
                            env.ENVIRONMENT=env.getProperty("environment_prod")
                        }
                    } else if ("${GIT_BRANCH}".contains("feature") || "${GIT_BRANCH}".contains("bugfix") || "${GIT_BRANCH}".contains("devint") || "${GIT_BRANCH}".contains("task/devintEnvironment")){
                        env.ENVIRONMENT=env.getProperty("environment_devint")
                    } else if("${GIT_BRANCH}".contains("develop")){
                        env.ENVIRONMENT=env.getProperty("environment_develop")
                    } else if ("${GIT_BRANCH}".contains("master") || "${GIT_BRANCH}".contains("hotfix")) {
                        env.ENVIRONMENT=env.getProperty("environment_prod")
                    }
                    sh """
                    echo "Environment: "${env.ENVIRONMENT}
                    """
                }
            }
        }
        stage('Omni Deploy'){
            when {
                anyOf {
                    branch 'master';
                    branch 'develop'
                }
                expression {
                    return true;
                }
            }
            steps {
                withAWS(credentials: 'omni-aws-creds'){
                    sh """
                    sceptre launch ${env.ENVIRONMENT} --yes
                    """
                }
            }
        }
        stage('Bizdev Deploy'){
            when {
                anyOf {
                    branch 'devint';
                    branch 'bugfix/*';
                    branch 'feature/*';
                    branch 'task/*';
                }
                expression {
                    return true;
                }
            }
            steps {
                withAWS(credentials: 'bizdev-aws-creds'){
                    sh """
                    sceptre launch ${env.ENVIRONMENT} --yes
                    """
                }
            }
        }
    }
}