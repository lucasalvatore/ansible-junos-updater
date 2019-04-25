# ansible-junos-updater
Ansible play to upgrade junos on QFX and EX devices. <br>
There is a single yaml (run-all.yaml) file to do all the tasks below, or there is a main.yaml with each task split out in the tasks directory <br>
<p>
- Runs some commands and dumps to a file<br>
- Copies files to devices<br>
- Confirms md5sum matches local copy<br>
- Upgrades Junos<br>
- Waits for devices to be reachable again<br>
<br>

Note, I run inside a venv hence the var: ansible_python_interpreter: "/opt/ansible/ansible-venv/bin/python"

