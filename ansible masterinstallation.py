import sys
import os
os.system("sudo apt install software-properties-common")
os.system("sudo apt-add-repository ppa:ansible/ansible")
os.system("apt update")
os.system("sudo apt install ansible")