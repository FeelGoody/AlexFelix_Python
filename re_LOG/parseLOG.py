import re

# with open('./re_LOG/sourceLOG.txt', "r") as file:
    # myText = file.read()

def searchPattern(myText):
    patt_service_name = r'Starting (\w+) service. '
    patt_service_date =  r'\( (\d{1,2}-\w{3}-\d{2}) (\d{2}:\d{2}:\d{2})\),'
    patt_service_ban = r'Input Ban :<(\d{9})>'
    patt_to_find = patt_service_name + patt_service_date + r'.+\n.+' + patt_service_ban
    return re.findall(patt_to_find, myText)