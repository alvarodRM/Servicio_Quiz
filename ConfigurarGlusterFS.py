#!/usr/bin/python
from subprocess import call


#Configuracion NAS
call("sudo lxc-attach --clear-env -n nas1 -- gluster peer probe 20.20.4.22", shell=True)
call("sudo lxc-attach --clear-env -n nas1 -- gluster peer probe 20.20.4.23", shell=True)
call("sudo lxc-attach --clear-env -n nas1 -- gluster peer status", shell=True)
call("sudo lxc-attach --clear-env -n nas1 -- gluster volume create nas replica 3 nas1:/nas nas2:/nas nas3:/nas force", shell=True)
call("sudo lxc-attach --clear-env -n nas1 -- gluster volume start nas", shell=True)
call("sudo lxc-attach --clear-env -n nas1 -- gluster volume info", shell=True)
call("sudo lxc-attach --clear-env -n nas1 -- gluster volume set nas network.ping-timeout 5", shell=True)
call("sudo lxc-attach --clear-env -n nas2 -- gluster volume set nas network.ping-timeout 5", shell=True)
call("sudo lxc-attach --clear-env -n nas3 -- gluster volume set nas network.ping-timeout 5", shell=True)

#Configuracion S1-S3
call("sudo lxc-attach --clear-env -n s1 -- mkdir /mnt/nas", shell=True)
call("sudo lxc-attach --clear-env -n s1 -- mount -t glusterfs 20.20.4.21:/nas /mnt/nas", shell=True)
call("sudo lxc-attach --clear-env -n s2 -- mkdir /mnt/nas", shell=True)
call("sudo lxc-attach --clear-env -n s2 -- mount -t glusterfs 20.20.4.21:/nas /mnt/nas", shell=True)
call("sudo lxc-attach --clear-env -n s3 -- mkdir /mnt/nas", shell=True)
call("sudo lxc-attach --clear-env -n s3 -- mount -t glusterfs 20.20.4.21:/nas /mnt/nas", shell=True)
