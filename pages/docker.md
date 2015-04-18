title: Docker study notes
date: 2015-04-18
tags: [docker]


****Best definition of what is docker:

"Today the vast majority of enterprise applications are slow-evolving monoliths that are bound to a specific infrastructure, let-alone a specific server.

Dockerized distributed applications in contrast are composed of modular components providing for constant real-time innovations which can be ported across any infrastructure, whether on premise or in the cloud, without any modification.. Modularity means that Dockerized distributed applications are evolutionary; they can blend the old with the new."

reference: https://blog.docker.com/2014/10/docker-microsoft-partner-distributed-applications/

CHEATSHEET:

    Test with this example:
        http://www.damagehead.com/docker-gitlab/

        docker pull <image-name>
        docker images
        docker run <image-name> <command>
        docker ps
        docker logs
        docker stats [container_id]
        docker top  [container_id]

        Port forwarding:
            docker run -d -p host:container django-docker

        Volumes - Mount folders - host/container
            docker run -v host_path:container_path django

        Links - Service discovery through env vars
            docker run --link mysql:db --name webapp django

Dokku VS Flynn: Dokku is single hosted and simpler. Flynn had a kickstarter. Flynn: manages databases and escalation.

Fat VS Thin containers

    A minimal Ubuntu base image modified for Docker-friendliness (fat container - similar to a virtual machine): https://github.com/phusion/baseimage-docker/blob/master/README.md .

    An alternative approach to the fat container above is a thin container: http://blog.docker.com/2014/06/why-you-dont-need-to-run-sshd-in-docker/

Web interface to monitor containers:

    https://github.com/tobegit3hub/seagull

---

TIPS:
- When using fig, the container name will also be the hostname. So, to communicate between hosts, I can use the container name as if it the machine hostname / ip.

- A way to speedup your builds is to create a local docker registry (recipe "A" below) or to mirror the official registry locally (recipe "B" below).

    - Recipe A: Create a local docker registry:

        1) Get the image to create the local docker registry from the official registry (DockerHub):

            $ docker pull registry

        2) Start the docker daemon manually [*].

            $ docker run -d --insecure-registry localhost:5000 -e STORAGE_PATH=/home/tiago/registry -p 5000:5000 registry

            By default it expects the protocol to be https. To avoid that on the development environments, you must start your docker daemon with "--insecure-registry localhost:5000"

            [*] If you want to keep using the start daemon provided by your distribution, you will need to pass the extra parameters above to it. See: http://unix.stackexchange.com/questions/28209/how-can-i-run-a-daemon-with-custom-parameters.
            Alternatively, If your distribution uses systemd, you can disable the daemon created on docker installation and make a new unit file to create a new custom daemon with the parameters above. The systemd unit files probably begin with "/usr/lib/systemd/system/docker*":
                $ systemctl stop docker
                $ systemctl disable docker
                (edit the new service file here and put it with the other ones)
                $ systemctl start docker
                If it is correctly started:
                    $ systemctl enable docker

        3) Pull a sample image from the official docker registry (you could make one yourself, as an alternative):

            $ docker pull busybox

        4) Tag the image for copying it into the local registry:

            $ docker tag busybox localhost:5000/busybox

             IMPORTANT: When you use a local registry, you have to specify the hostname of the private registry as part of the image name. For example, if my private registry is running at registry.example.com, I would 'docker push registry.example.com/imagename

        5) Copies the image to the local registry:

            $ docker push localhost:5000/busybox

        6) Pull the new image from your local registry to test:

            $ docker pull localhost:5000/busybox

        7) To get a list of your images:

            $ docker images

        8) To delete an image:

            $ docker rmi [image_name]


    - Recipe B: Creating a local mirror of the official registry:

        That way each time a new image is pulled, it will be pulled from the internet. The subsequent times, it will be pulled from your mirror (locally and faster). If you opt for a mirror don't worry, it will not mirror "all" the official repository, but just mirror the image at the first pull.

        https://github.com/docker/docker/blob/master/docs/sources/articles/registry_mirror.md

- On the Dockerfile:
    - 'RUN' is used during build
    - mounts are used during run (not on the build process)

RESOURCES:
    Videos:
        - Supercharge your development environment using Docker: https://www.youtube.com/watch?v=-l9xH1X_rvg
        - Be a happier developer with Docker: Tricks of the trade Nicola Paolucci (Atlassian): https://www.youtube.com/watch?v=XCVOxht34Hs
        - Austin Docker - Developer workflows using Docker: https://www.youtube.com/watch?v=I2jLviFHjX0
        - Lessons from using Docker to improve web developer productivity: https://www.youtube.com/watch?v=PBBUnNS4dRw
        - Orchestrating Docker containers in production using Fig: https://www.youtube.com/watch?v=SEtRg8siQWw
    Links:
        - http://www.activestate.com/blog/2014/01/deploying-your-own-private-docker-registry
        - https://docs.docker.com/installation/#installation
        - https://blog.rainforestqa.com/2014-11-19-docker-in-action-from-deployment-to-delivery-part-1-local-docker-setup/
        - https://github.com/wsargent/docker-cheat-sheet/blob/master/README.md

---

I finally got something close to a "good workflow" - something I
really wanted to for a start. Here is a shell script:
 
https://github.com/amitsaha/docker_files/blob/master/dev_workflow/restraint.sh
 
What it does is to creates a docker image with all the dependencies
for a particular project I was setting this up for, changes the user
in docker to my current host user (so that all my host files are
seamlessly synced between the host + container), and starts the
container. So i have my entire home available in the container.
(Thanks to the person who pointed me the simple trick of setting up a
user with the same UID/GID in the container on this list).
 
On Fedora, I needed to set SELinux to permissive for the file sharing
between host and container to work properly.

---

Flocker handles the set up of data volumes for your containers and allows 
you to do things like migrate a data volume between nodes (for instance if 
you need to upgrade your database to a larger machine with more RAM) with 
minimal downtime. 

---

http://www.tech-d.net/2014/11/18/data-only-container-madness/
http://www.tech-d.net/2014/11/03/docker-indepth-volumes/

Deis: self-hosted heroku on docker. Has a docker registry built-in.
---

Videos:
http://go.docker.com/webmail/44082/198799545/5d02056091232d601e061dfae62ed743
