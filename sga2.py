import numpy as np

def metric(x, y, i, j):
	return np.sqrt(np.square(x - i) + np.square(y - j))

def radiation(x):
	return np.power(10, 6) * np.exp(-x / 2.0)

def dose(x, y):
	def calculate(i, j):
		distance = metric(x, y, i, j)
		return radiation(distance)
	return calculate

def generate_radiation(x, y, size=700):
	return np.fromfunction(dose(x, y), (size, size))

