import subprocess
import os,sys
import docker

DropDBSQL = "/Users/nirav/mariadb/conf/DockerGravDBREstore/DroPDB.sql"

oscmd2 = 'docker exec -d mariadb mysql -uroot -pgravitant <%s' %DropDBSQL
subprocess.call(["/usr/local/bin/docker","ps"])
#call('docker exec -d mariadb mysql -uroot -pgravitant </Users/nirav/mariadb/conf/DockerGravDBREstore/DroPDB.sql')
os.system('/usr/local/bin/docker ps')

#client = docker.from_env()
#print client.containers.list()
#print client.images.list()
client = docker.APIClient(base_url='unix://var/run/docker.sock')
print client.version()
print client.exec_create("mariadb","mysql -uroot -pgravitant < /etc/mysql/conf/DockerGravDBREstore/DroPDB.sql")