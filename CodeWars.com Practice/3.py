import string as s

def to_jaden_case(word1):
    ret = word1.split()
    newList = []
    for i in ret:
        newList.append(i.capitalize())
    # myword = newList.join
    newList = ' '.join(newList)
    print(newList)
    


word = "How can mirrors be real if our eyes aren't real"
print(word)
to_jaden_case(word)


    # Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
