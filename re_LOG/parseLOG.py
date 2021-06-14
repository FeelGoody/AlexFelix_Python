import re
import os
import datetime
# print(os.getcwd())
with open('./re_LOG/sourceLOG.txt', "r") as file:
    myText = file.read()


patt_service_name = r'Starting (\w+) service. '
patt_service_date =  r'\( (\d{1,2}-\w{3}-\d{2}) (\d{2}:\d{2}:\d{2})\),'
patt_service_ban = r'Input Ban :<(\d{9})>'
patt_to_find = patt_service_name + patt_service_date + r'.+\n.+' + patt_service_ban
result = re.findall(patt_service_name, myText)
result1 = re.findall(patt_service_date, myText)
result2 = re.findall(patt_service_ban, myText)
result_all = re.findall(patt_to_find, myText)

print(result)
# print(result1)
# regex = ur"\[P\] (.+?) \[/P\]+?"
# line = "President [P] Barack Obama [/P] met Microsoft founder [P] Bill Gates [/P], yesterday."
# person = re.findall(regex, line)

# Starting (\w+) service. \( (\d{1,2}-\w{3}-\d{2}) (\d{2}:\d{2}:\d{2})\),.+Input Ban :<(\d{9})>
# Input Ban :<(\d{9})>
# Starting evGtPrimSub service. ( 9-Jun-21 06:20:53), Operator ID: 12372.
#    Input Ban :<968618102>

file_path_list

data = list()
for file_path in file_path_list:
    with open(file_path, "r") as file:
        
        myText = file.read()

        patt_service_name = r'Starting (\w+) service. '
        patt_service_date =  r'\( (\d{1,2}-\w{3}-\d{2}) (\d{2}:\d{2}:\d{2})\),'
        patt_service_ban = r'Input Ban :<(\d{9})>'
        patt_to_find = patt_service_name + patt_service_date + r'.+\n.+' + patt_service_ban
        result_all = re.findall(patt_to_find, myText)
        data.append(result_all)