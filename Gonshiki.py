# bri = set(['Russia', 'USA', 'Germany', 'Germany'])
# print(bri, type(bri))


# briNum1 = [2, 5, 8, 345]


# briNum2 = [2, 7, 21, 345]
# vasya = list(set(briNum1) - set(briNum2))
# print(vasya)


# myDict = {'John1': 'Mazda', 'Peter': 'BMW', 'Jason': 'Nissan', 'Marry': 'Toyota'}
# print('#@'.join(list(myDict.keys())))
# for key in myDict.keys():
# print(key, end=' ')

# var = ''
# var_2 = 0
# var_3 = False
# var_4 = None


# import sys
import os
import json

myDict = {}
# myDict = {'John1': 'Mazda', 'Peter': 'BMW',
#           'Jason': 'Nissan', 'Marry': 'Toyota'}

def save_json():
    global myDict
    data = json.dumps(myDict)
    with open("gonshik.json", "w") as file:
        file.write(data)

def load_json():
    global myDict
    try:
        with open("gonshik.json", "r") as file:
            myDict = json.load(file)
    except Exception as err:
        print("Error load file:", err)

def main():
    global myDict
    while(True):
        userAction = input('\n\n--MAIN MENU--\n' +
                           'Press 1. Insert new racer\n' +
                           'Press 2. Delete existed racer\n' +
                           'Press 3. To print all racers\n' +
                           'Press 4. To clean a console\n' +
                           'Press 0. To Exit\n')
        if userAction == '0':
            break
        elif userAction == '1':
            # ['John', 'Suzuki']
            userInput1 = input("please your name and car (Exm: John Suzuki): ")
            newDataSplited = userInput1.split(' ')
            
            if newDataSplited[0] in list(myDict.keys()):
                print(f'\n\n ----This racer "{newDataSplited[0]}" already exists, please enter a new racer')
                continue    
            myDict[newDataSplited[0]] = newDataSplited[1]
            print(
                f'The new racer added successful name: {newDataSplited[0]} and brand: {newDataSplited[1]}')

        elif userAction == '2':
            pointMyDict = dict()

            for myDictIndex, (myDictKey, myDictValue) in enumerate(myDict.items(), 1):
                print(f"{myDictIndex}. {myDictKey} => {myDictValue}")
                pointMyDict[str(myDictIndex)] = myDictKey

            userChoice = input(
                'Enter the number of the racer you want to delete: ')
            del myDict[pointMyDict[userChoice]]
            print(f'The racer {pointMyDict[userChoice]} successfuly deleted')
        
        elif userAction == '3':
            print(f'Here are all racers that we have:')
            for myDictIndex, (myDictKey, myDictValue) in enumerate(myDict.items(), 1):
                print(f'{myDictIndex}. {myDictKey} => {myDictValue}')

        elif userAction == '4':
            os.system('cls')
            print(f'The terminal has been cleaned.')
           


if __name__ == '__main__':
    load_json()
    main()
    save_json()
# 123