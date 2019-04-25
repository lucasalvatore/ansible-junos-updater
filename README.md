# ansible-junos-updater
single yaml file for all the below <br>
Runs some commands and dumps to a file<br>
Copies files to devices<br>
confirms md5sum matches local copy<br>
Upgrades Junos<br>
waits for devices to be reachable again<br>
<br>
Runs inside a venv hence the ansible_python_interpreter: "/opt/ansible/ansible-venv/bin/python"
