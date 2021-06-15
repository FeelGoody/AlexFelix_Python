import paramiko
host = "opetapp101.unix.gsm1900.org"
port = 22
username = "opetolna"
password = "Amdocs11"

path = 'cd /pet/opetolna/users/felix/python_test/; ls; mkdir F1'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(path)
print(stdout.readlines())