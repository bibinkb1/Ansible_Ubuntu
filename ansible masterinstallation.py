import os
os.system("sudo apt install software-properties-common -y")
os.system("sudo apt-add-repository ppa:ansible/ansible -y")
os.system("sudo apt --fix-broken install")
os.system("sudo apt update -y")
os.system("sudo apt install ansible -y")
#configuration steps for local remote hosts
#step1:control node ssh-keygen 
#step2:ssh-copyid example@<ipaddress>(remote host)
#step3:edit the /etc/ansible/hosts file with (group which belongs/example@<ipaddress>)
#try to ping the remote host with ansible -m ping all or ping target host