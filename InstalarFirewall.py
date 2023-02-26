#!/usr/bin/python
from subprocess import call

#Ejecutamos fw.fw
call("sudo /lab/cdps/bin/cp2lxc /mnt/tmp/fw.fw /var/lib/lxc/fw/rootfs", shell=True)
call("sudo lxc-attach --clear-env -n fw -- chmod 777 /fw.fw", shell=True)
call("sudo lxc-attach --clear-env -n fw -- /fw.fw", shell=True)
