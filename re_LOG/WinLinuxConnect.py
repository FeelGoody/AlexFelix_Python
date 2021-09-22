import paramiko
# import rich
# pretty.install()
from parseLOG import searchPattern, changeDateFormat


def connectToSource():
    host = "opetapp101.unix.gsm1900.org"
    port = 22
    username = "opetolna"
    password = "Amdocs11"
    path_to_folder = '/pet/opetolna/users/felix/python_test/'
    path = 'cd /pet/opetolna/users/felix/python_test/; ls;'

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)

    fileList = ssh.exec_command(path)[1].readlines()
    for fileName in fileList:
        less = 'less ' + path_to_folder + fileName.replace('\n','')
        readFromFile = ssh.exec_command(less)[1].readlines()
        strReadFromFile = ''.join(readFromFile)
        formatDate = changeDateFormat(strReadFromFile)
        dataLOG = searchPattern(formatDate)
        print(dataLOG)

    

def connectToFile():
    path_to_folder = "D://Dropbox//Python//AlexFelix_Python//GitHub//AlexFelix_Python//re_LOG//sourceLOG.txt"
    with open(path_to_folder, 'r') as outfile:
        fileText = outfile.read()
    formatDate = changeDateFormat(fileText)
    dataLOG = searchPattern(formatDate)
    print(dataLOG)

# connectToFile()



connectToSource()