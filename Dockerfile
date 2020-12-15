FROM dosel/zalenium
WORKDIR /test
USER root
VOLUME //var/run/docker.sock
VOLUME /home/seluser/videos
EXPOSE 5000

