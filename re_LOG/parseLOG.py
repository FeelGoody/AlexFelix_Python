import re
from datetime import datetime
import time
# with open('./re_LOG/sourceLOG.txt', "r") as file:
    # myText = file.read()

def searchPattern(myText):
    patt_service_name = r'Starting (\w+) service. '
    patt_service_date =  r'(\d{1,2}/\d{2}/\d{2}) (\d{2}:\d{2}:\d{2})\),'
    patt_service_ban = r'Input Ban :<(\d{9})>'
    patt_to_find = patt_service_name + patt_service_date + r'.+\n.+' + patt_service_ban
    return re.findall(patt_to_find, myText)

def setFormat(textDate):
    return datetime.strptime(textDate, '%d-%b-%y').strftime("%m/%d/%y")


def changeDateFormat(myText):
    # data: ( 9-Jun-21 06:20:42), 
    patt_service_date =  r'\( (\d{1,2}-\w{3}-\d{2})'
    return re.sub(patt_service_date, 
                    lambda x: setFormat(x.group(1)),
                    myText)

# t1 = time.time()
# from_func = changeDateFormat('data: ( 9-Jun-21 06:20:42),')
# print(time.time()-t1)
# print(from_func)
# Expert to XLS