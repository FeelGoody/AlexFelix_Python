import paramiko
from parseLOG import searchPattern



host = "opetapp101.unix.gsm1900.org"
port = 22
username = "opetolna"
password = "Amdocs11"
path_to_folder = '/pet/opetolna/users/felix/python_test/'
path = 'cd /pet/opetolna/users/felix/python_test/; ls; mkdir F1'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

fileList = ssh.exec_command(path)[1].readlines()
for fileName in fileList:
    less = 'less ' + path_to_folder + fileName.replace('\n','')
    readFromFile = ssh.exec_command(less)[1].readlines()
    strReadFromFile = ''.join(readFromFile)
    dataLOG = searchPattern(strReadFromFile)
    print(dataLOG)