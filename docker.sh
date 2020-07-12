#!/bin/bash
echo "Updating apt-get"
sudo apt-get -qq update

echo "Installing pre req packages"
sudo apt-get -y install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common > /dev/null 2>&1

echo "Adding Docker's GPG key"
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - > /dev/null 2>&1

echo "Adding repostiory"
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable" > /dev/null 2>&1

echo "Updating apt-get"
sudo apt-get -qq update

echo "Installing docker"
sudo apt-get -y install docker-ce docker-ce-cli containerd.io > /dev/null 2>&1

