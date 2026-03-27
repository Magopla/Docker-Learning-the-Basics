Example: Portainer-ce

1) Installation

docker pull portainer/portainer-ce

2) Deployment

https://docs.portainer.io/start/install-ce/server/docker/wsl

First, create the volume that Portainer Server will use to store its database:


-> docker volume create portainer_data

Then, download and install the Portainer Server container:

docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:lts

Portainer Server has now been installed. You can check to see whether the Portainer Server container has started by running docker ps:

->root@server:~# docker ps
docker run -p 8000:8000 -p 9443:9443 --name portainer -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:lts 
Updated for coninienve

Access it using:

https://localhost:9443/

User: Admin
Pwd: adminadminadmin