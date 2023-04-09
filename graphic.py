from random import randint

class graphic():
	def __init__(self, x: int, y: int, fill = '  '):
		self.x = x
		self.y = y
		self.fill = self.__checkFill(fill, '  ')
		self.clear()
		
	def clear(self):
		newList = []
		for i in range(self.y):
			newList.append([])
			for j in range(self.x):
				newList[i].append(self.fill)
		self.graph = newList	
		
	def __fillg(self, x, y, fill):
		if x > 0 and x <= self.x and y > 0 and y <= self.y: self.graph[self.y - y][x - 1] = fill
		
	def draw(self):
		n = 0
		for i in self.graph:
			if len(str(self.y - n)) > 1:
				print(str(self.y - n) + ''.join(i))
			else:
				print(str(self.y - n) + ' ' + ''.join(i))
			n += 1
		n = ''
		for i in range(self.x + 1):
			if len(str(i)) < 2:
				n += str(i) + ' '
			else:
				n += str(i)
		print(n)
		
	def __drawFromTo(self, begin, end, x, fill):
		if begin > end: begin, end = end, begin
		for i in range(1, end - begin):
			self.__fillg(x, begin + i, fill)
	
	def __checkFill(self, fill, defaultFill):
		if len(fill) > 2: return fill[:2] if not ('⬛' in fill[:2]) and not ('⬜' in fill[:2]) else self.__checkFill(fill[0], '##')
		elif len(fill) == 2: return fill
		elif len(fill) == 1: return fill * 2 if fill != '⬜' and fill != '⬛' else fill
		elif len(fill) == 0: return defaultFill
	
	def function(self, f, leftLimit = 1, rightLimit = 9999, fill = ''):
			if rightLimit > self.x: rightLimit = self.x
			if leftLimit < 1: leftLimit = 1
			fill = self.__checkFill(fill, '##')
			try: Prev = f(0)
			except: yPrev = self.x
			for i in range(self.x):
				if i + 1 <= rightLimit and i + 1 >= leftLimit:
					y = int(f(i + 1))
					if y <= len(self.graph) and y > 0:
						self.__fillg(i + 1, y, fill)
						if i + 1 != leftLimit:
							self.__drawFromTo(int(yPrev), int(y), i, fill)
					elif y >= yPrev and ((yPrev >= 1 and yPrev <= self.y) or (y >= 1 and y <= self.y)):
						self.__drawFromTo(self.y + 1, yPrev - 1, i, fill)
					elif y < yPrev and ((yPrev > 0 and yPrev <= self.y) or (y > 0 and y <= self.y)):
						self.__drawFromTo(0, yPrev, i, fill)
					yPrev = y
						
	def randomGraphic(self, leftLimit = 1, rightLimit = 9999, fill = '', randomK = 7, firstAngle = 1010):
		if rightLimit > self.x: rightLimit = self.x
		if leftLimit < 1: leftLimit = 1
		fill = self.__checkFill(fill, '##')
		if firstAngle == 1010:
			yPrev = randint(1, self.y)
		else: yPrev = firstAngle
		for i in range(self.x):
			if i + 1 <= rightLimit and i + 1 >= leftLimit:
				y = yPrev + randint(-randomK, randomK)
				y = int(y)
				if y <= len(self.graph) and y > 0:
					self.__fillg(i + 1, y, fill)
					if i + 1 != leftLimit:
						self.__drawFromTo(int(yPrev), int(y), i, fill)
				elif y >= yPrev and ((yPrev >= 1 and yPrev <= self.y) or (y >= 1 and y <= self.y)):
					self.__drawFromTo(self.y + 1, yPrev - 1, i, fill)
				elif y < yPrev and ((yPrev > 0 and yPrev <= self.y) or (y > 0 and y <= self.y)):
					self.__drawFromTo(0, yPrev, i, fill)
				yPrev = y
			
	def graphicFromList(self, list: list, leftLimit = 1, rightLimit = 9999, fill = ''):
			if rightLimit > self.x: rightLimit = self.x
			if leftLimit < 1: leftLimit = 1
			fill = self.__checkFill(fill, '##')
			yPrev = 0
			for i in range(self.x):
				if i + 1 <= rightLimit and i + 1 >= leftLimit and i <= len(list):
					y = list[i]
					if y <= len(self.graph) and y > 0:
						self.__fillg(i + 1, y, fill)
						if i + 1 != leftLimit:
							self.__drawFromTo(int(yPrev), int(y), i, fill)
					elif y >= yPrev and ((yPrev >= 1 and yPrev <= self.y) or (y >= 1 and y <= self.y)):
						self.__drawFromTo(self.y + 1, yPrev - 1, i, fill)
					elif y < yPrev and ((yPrev > 0 and yPrev <= self.y) or (y > 0 and y <= self.y)):
						self.__drawFromTo(0, yPrev, i, fill)
					yPrev = y