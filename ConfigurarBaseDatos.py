#!/usr/bin/python3
from subprocess import call

call("sudo lxc-attach --clear-env -n bbdd -- apt update", shell=True)
call("sudo lxc-attach --clear-env -n bbdd -- apt -y install mariadb-server", shell=True)
call("sudo lxc-attach --clear-env -n bbdd -- sed -i -e 's/bind-address.*/bind-address=0.0.0.0/' -e 's/utf8mb4/utf8/' /etc/mysql/mariadb.conf.d/50-server.cnf", shell=True)
call("sudo lxc-attach --clear-env -n bbdd -- systemctl restart mysql", shell=True)
call("sudo lxc-attach --clear-env -n bbdd -- mysqladmin -u root password xxxx", shell=True)
call("sudo lxc-attach --clear-env -n bbdd -- mysql -u root --password='xxxx' -e \"CREATE USER 'quiz' IDENTIFIED BY 'xxxx';\"", shell=True)
call("sudo lxc-attach --clear-env -n bbdd -- mysql -u root --password='xxxx' -e \"CREATE DATABASE quiz;\"", shell=True)
call("sudo lxc-attach --clear-env -n bbdd -- mysql -u root --password='xxxx' -e \"GRANT ALL PRIVILEGES ON quiz.* to 'quiz'@'localhost' IDENTIFIED by 'xxxx';\"", shell=True)
call("sudo lxc-attach --clear-env -n bbdd -- mysql -u root --password='xxxx' -e \"GRANT ALL PRIVILEGES ON quiz.* to 'quiz'@'%' IDENTIFIED by 'xxxx';\"", shell=True)
call("sudo lxc-attach --clear-env -n bbdd -- mysql -u root --password='xxxx' -e \"FLUSH PRIVILEGES;\"", shell=True)

