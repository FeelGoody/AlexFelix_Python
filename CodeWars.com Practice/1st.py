def Wiskey(normPrice, discount,eventPrice):
  print('this is the price of the event ={1}/{3}/{2}'.format(eventPrice,'test',6))
  print(f'the price of the discount ={eventPrice}')
  discount_amount = normPrice * discount
  bottle_quant = eventPrice / discount_amount
  # print('The number of bottles as per event budget = ', bottle_quant)
  return int(bottle_quant)

result = Wiskey (normPrice = 10, discount = 0.1, eventPrice=500)
print(result)
# Цель этого ката - выяснить, сколько бутылок виски беспошлинной торговли вам нужно будет купить, чтобы экономия по сравнению с обычной средней ценой фактически покрыла расходы на ваш отпуск.

# Вам будет предоставлена ​​стандартная цена (normPrice), скидка в дьюти-фри (скидка) и стоимость праздника.

# Например, если бутылка обычно стоит 10 фунтов стерлингов, а скидка в дьюти фри составляет 10%, вы сэкономите 1 фунт стерлингов на каждой бутылке. Если ваш отпуск стоит 500 фунтов стерлингов, ответ, который вы должны вернуть, будет 500.

# Все входные данные будут целыми. Пожалуйста, верните целое число. Округлить вниз.
