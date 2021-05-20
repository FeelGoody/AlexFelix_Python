class Cars():
	
	def __init__(self, color,door, hight, weight):
		self.color = color
		self.door = door
		self.hight = hight
		self.weight = weight
		print("The initialization succ")	
	
	def	setColor(self, carColor):
		self.color = carColor

	def	getColor(self):
		print('<<<<<<<<<get Cars color')
		return self.color
		
# obj1 = Cars('Blue', 5, 185, 3000)
# obj1.getColor.
# print(f"The color", obj1.getColor())
# # obj1.setColor('Red')
# obj1.color = 'Yellow'
# print(f"The color", obj1.getColor())


class Toyota(Cars):
	def __init__(self, clr, door, hight, weight, color_wheels=None):
		super().__init__(clr, door, hight, weight)
		print(self.color)
		self.__vasya = 'vasya'
		self._test = 'test'
		
		
	def setDoor(self, Door):
		self.door = Door

	def getDoor(self):
		return self.door


objToyota = Toyota("Green", 10, 1800, 1500)
print(objToyota._test)
print(objToyota._Toyota__vasya)
# objCars = Cars("objCarsGreen", 10, 1800, 1500)
# print(objToyota.getColor())		
# print(objCars.getColor())		


# print(objToyota.getDoor())		
# objToyota.setDoor(4)
# print(objToyota.getDoor())


