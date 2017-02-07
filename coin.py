# -*- coding: utf8 -*-

class coin:
	def __init__(self, x, y, radius):
		self.x = x
		self.y = y
		self.radius = radius
		self.value = 0.0
		self.primary_color = [0.0,0.0,0.0]
		self.secundary_color = [0.0,0.0,0.0]

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

	def get_radius(self):
		return self.radius

	def get_value(self):
		return self.value

	def set_value(self, value):
		self.value = value

	def get_primary_color(self, index):
		return self.primary_color[index]

	def set_primary_color(self, primary_color, index):
		self.primary_color[index] = primary_color

	def get_secundary_color(self, index):
		return self.secundary_color[index]

	def set_secundary_color(self, secundary_color, index):
		self.secundary_color[index] = secundary_color
