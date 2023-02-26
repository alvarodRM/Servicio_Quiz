#!/usr/bin/python
from subprocess import call

#Instalaccion nodejs en S1-S3
call("sudo lxc-attach --clear-env -n s1 -- apt-get install nodejs", shell=True)
call("sudo lxc-attach --clear-env -n s2 -- apt-get install nodejs", shell=True)
call("sudo lxc-attach --clear-env -n s3 -- apt-get install nodejs", shell=True)
call("sudo lxc-attach --clear-env -n s1 -- apt-get install npm", shell=True)
call("sudo lxc-attach --clear-env -n s2 -- apt-get install npm", shell=True)
call("sudo lxc-attach --clear-env -n s3 -- apt-get install npm", shell=True)

#Clonar repositorio QUIZ
call("sudo lxc-attach --clear-env -n s1 -- bash -c \"git clone https://github.com/CORE-UPM/quiz_2021.git\"", shell=True)

call("sudo lxc-attach --clear-env -n s2 -- bash -c \"git clone https://github.com/CORE-UPM/quiz_2021.git\"", shell=True)

call("sudo lxc-attach --clear-env -n s3 -- bash -c \"git clone https://github.com/CORE-UPM/quiz_2021.git\"", shell=True)

call("sudo lxc-attach --clear-env -n s1 -- bash -c \"cd /quiz_2021; mkdir public/uploads; sed -i 's|app\.use(r|// app\.use(r|' app.js; npm install; npm install forever; npm install mysql2; \"", shell=True)

call("sudo lxc-attach --clear-env -n s2 -- bash -c \"cd /quiz_2021; mkdir public/uploads; sed -i 's|app\.use(r|// app\.use(r|' app.js; npm install; npm install forever; npm install mysql2; \"", shell=True)

call("sudo lxc-attach --clear-env -n s3 -- bash -c \"cd /quiz_2021; mkdir public/uploads; sed -i 's|app\.use(r|// app\.use(r|' app.js; npm install; npm install forever; npm install mysql2; \"", shell=True)

call("sudo lxc-attach --clear-env -n s1 -- bash -c \"cd /quiz_2021; export QUIZ_OPEN_REGISTER=yes; export DATABASE_URL=mysql://quiz:xxxx@20.20.4.31:3306/quiz; npm run-script migrate_env; npm run-script seed_env; ./node_modules/forever/bin/forever start ./bin/www \"", shell=True)

call("sudo lxc-attach --clear-env -n s2 -- bash -c \"cd /quiz_2021; export QUIZ_OPEN_REGISTER=yes; export DATABASE_URL=mysql://quiz:xxxx@20.20.4.31:3306/quiz; ./node_modules/forever/bin/forever start ./bin/www \"", shell=True)

call("sudo lxc-attach --clear-env -n s3 -- bash -c \"cd /quiz_2021; export QUIZ_OPEN_REGISTER=yes; export DATABASE_URL=mysql://quiz:xxxx@20.20.4.31:3306/quiz;  ./node_modules/forever/bin/forever start ./bin/www \"", shell=True)


#Enlace simbolico
call("sudo lxc-attach --clear-env -n s1 -- bash -c \"cd /quiz_2021/public; ln -s /mnt/nas uploads\"", shell=True)
call("sudo lxc-attach --clear-env -n s2 -- bash -c \"cd /quiz_2021/public; ln -s /mnt/nas uploads\"", shell=True)
call("sudo lxc-attach --clear-env -n s3 -- bash -c \"cd /quiz_2021/public; ln -s /mnt/nas uploads\"", shell=True)
