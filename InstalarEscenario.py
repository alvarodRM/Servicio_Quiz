#!/usr/bin/python3
import time
import os
from subprocess import call
call("cd /mnt/tmp", shell=True)
call("wget http://idefix.dit.upm.es/cdps/pc2/pc2.tgz", shell=True)
call("sudo vnx --unpack pc2.tgz", shell=True)
time.sleep(25)
os.chdir("pc2")
call("pwd")
call("bin/prepare-pc2-labo", shell=True)
time.sleep(60)
call("sudo vnx -f pc2.xml --create", shell=True)

