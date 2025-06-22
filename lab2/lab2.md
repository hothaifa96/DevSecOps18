# peakyblinders software  

## scebario:
you work at peakyblinders software ltd 
you are the only devops in this company
you have 5 components:
- frontend : react application ---- 'node npm' runs on port 80
- API gateway: nodejs service ---- 'node npm' runs on port 5001
- user service: flask service ---- 'flask python pip' runs on port 5002
- inventory service: java spring boot service ---- 'java jdk springboot' runs on port 5003
- database: postgresql db with scripts ---- 'postgresql' open on port 5432

# request:
create a one pipline file to build and deploy the whole 5 services togather 

# stages:
- clone the code: parallel stage for pulling the 5 services codes
- check requirements: parallel stage of parallel's that check every dependency for each service please add a retry machanisim to insure the safe chack
- build stage : parallel stage to build a docker image for all of those applications
- testing: using docker compose this stage must run all the components togather to get the application up and running and the run a test.sh commands

#### please write echos for each proccess for now 

stage('build'):{
    steps{
        echo 'docker build -t name'
    }
}