def sp_eng(sentence, word):
  if word.lower() in sentence.lower():
    return True
  else: return False
    
print(sp_eng(input("Please enter your word:  "), 'english'))


# c = ', world'
# if 'Hello' in c:
#   print("OK")
# else:
#   print("No")
# a = [1, 2, 3]
# b = 4
# if b in a:
#   print("yes")
# else:
#   print('not')