#!/usr/bin/python3
import sys


# 2 Arguments, file to read and a list L
def read_data(file, L):
	text_file = open(file, "r")
	# GET to data section
	loop = True
	while loop:
		line = text_file.readline()
		if '@DATA' in line:
			# Get each value
			while loop:
				# Put all of the values into a list
				L = text_file.readlines()
				L = [line.rstrip() for line in L]
				if L:
					global list
					list = L
					continue
				else:
					text_file.close()
					loop = False


def process_numeric_field(L, fieldNum):
	# 2 arguments, list L, field number to process
	global min
	min = 0
	global max
	max = 0
	global average
	average = 0

	for i in range(len(L)):
		element = str(L[i])
		element = element.split(',')[fieldNum]

		if i == 0:
			min = float(element)
			max = float(element)

		if float(element) > max:
			max = float(element)

		if float(element) < min:
			min = float(element)

		average = average + float(element)
	average = average / int(len(L))
	# Returns min, max, and average
	return min, max, average


def count_iris_types(L):
	# 1 argument, list L
	setosa = 0
	versicolor = 0
	virginica = 0
	for element in range(len(L)):

		if 'Iris-setosa' in L[element]:
			setosa = setosa + 1
		elif 'Iris-versicolor' in L[element]:
			versicolor = versicolor + 1
		elif 'Iris-virginica' in L[element]:
			virginica = virginica + 1

	return setosa, versicolor, virginica
	# Returns number of Iris setosa, Iris Versicolor, and Iris Virginica.


# Command Line args
try:
	fileName = sys.argv[1]
except IndexError:
	print('There must be an argument')
	sys.exit()

# List
list = []
# Read the data from the file
read_data(fileName, list)
# Count Iris Types
distribution = count_iris_types(list)
# Process all of the fields

# Get the fields calculated
s_length = 0
s_width = 0
p_length = 0
p_width = 0
for x in range(4):
	# Get values
	min, max, average = process_numeric_field(list, x)
	if x == 0:
		average = "{:.2f}".format(average)
		s_length = min, max, average
	if x == 1:
		average = "{:.2f}".format(average)
		s_width = min, max, average
	if x == 2:
		average = "{:.2f}".format(average)
		p_length = min, max, average
	if x == 3:
		average = "{:.2f}".format(average)
		p_width = min, max, average

print('Summary Statistics:')
print('		MIN   MAX  MEAN')
print('Sepal Length: ' + str(s_length))
print('Sepal Width: ' + str(s_width))
print('Petal Length: ' + str(p_length))
print('Petal Width: ' + str(p_width))
print('Iris Types: ' + str(distribution))
