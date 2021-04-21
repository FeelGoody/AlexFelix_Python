
def tryNow():
  try:
    # print(6/1)
    a='abcdef'
    if len(a)>5:
      raise EOFError('text is long')  
  # except Felix as text:
  #   print(text)
  except EOFError as err:
    print("the row is too long")
    print(err)
  except ZeroDivisionError:
    print("divison by zero!")
  except Exception as err:
    print('error:', err) 
  else:
    pass
    # print('try ok')
  finally:
    pass
    # print("that's all")

tryNow()