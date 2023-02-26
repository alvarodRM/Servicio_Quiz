#!/usr/bin/python
from subprocess import call
import time

#Instalamos haproxy
call("sudo lxc-attach --clear-env -n lb -- bash -c \"apt-get update; apt-get install haproxy\"", shell=True)

call("sudo lxc-attach --clear-env -n lb -- sudo rm /etc/haproxy/haproxy.cfg", shell=True)


#Volvemos a copiar haproxy al directorio origen
#call("sudo chmod 777 haproxy.cfg",shell=True)
call("sudo /lab/cdps/bin/cp2lxc haproxy.cfg /var/lib/lxc/lb/rootfs/etc/haproxy",shell=True)

time.sleep(5)

#Reiniciamos haproxy
call("sudo lxc-attach --clear-env -n lb -- sudo service haproxy restart", shell=True)
