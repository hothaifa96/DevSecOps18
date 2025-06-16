FROM jenkins/jenkins:lts

USER root

# Install Docker CLI (optional: full Docker CE if required)
RUN apt-get update -qq && \
    apt-get install -qqy apt-transport-https ca-certificates curl gnupg2 software-properties-common && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian bullseye stable" > /etc/apt/sources.list.d/docker.list && \
    apt-get update -qq && \
    apt-get install -qqy docker-ce docker-ce-cli containerd.io && \
    apt-get clean

# Add Jenkins user to docker group
RUN usermod -aG docker jenkins

USER jenkins
