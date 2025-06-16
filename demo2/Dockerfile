FROM jenkins/jenkins:lts

# Switch to root to install Docker
USER root

# Install Docker CLI and dependencies
RUN apt-get update && \
    apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    sudo && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null && \
    apt-get update && \
    apt-get install -y docker-ce-cli docker-compose-plugin

# Create docker group and add jenkins user to it
RUN groupadd -f docker && usermod -aG docker jenkins

# Install common plugins
RUN jenkins-plugin-cli --plugins \
    ant:latest \
    antisamy-markup-formatter:latest \
    build-timeout:latest \
    credentials-binding:latest \
    docker-workflow:latest \
    email-ext:latest \
    git:latest \
    github-branch-source:latest \
    gradle:latest \
    ldap:latest \
    mailer:latest \
    matrix-auth:latest \
    pam-auth:latest \
    pipeline-github-lib:latest \
    pipeline-stage-view:latest \
    ssh-slaves:latest \
    timestamper:latest \
    workflow-aggregator:latest \
    ws-cleanup:latest

# Create docker group with specific GID (matching host)
# RUN groupadd -g 999 docker && usermod -aG docker jenkins

# Switch back to jenkins user
USER jenkins

# Skip initial setup wizard
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false

ENV JENKINS_HOME=/var/jenkins_home

EXPOSE 8080 50000