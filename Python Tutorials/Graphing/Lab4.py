#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import csv

# CPU UTILIZATION
# Make the data
num = 0
# Amount of x ticks
x_ticks=np.arange(0, 900, 10)
plt.xticks(x_ticks)

for files in range(6):
	x = []
	y = []
	num += 1
	with open('APM' + str(num) + '_metrics.csv', 'r') as file:
		lines = csv.reader(file, delimiter=',')

		for row in lines:
			x.append(row[0])
			y.append(float(row[1]))
	if num == 1:
		plt.plot(x, y, color='blue', linestyle='solid', marker='o', label="APM1")
	elif num == 2:
		plt.plot(x, y, color='black', linestyle='solid', marker='o', label="APM2")
	elif num == 3:
		plt.plot(x, y, color='red', linestyle='solid', marker='o', label="APM3")
	elif num == 4:
		plt.plot(x, y, color='green', linestyle='solid', marker='o', label="APM4")
	elif num == 5:
		plt.plot(x, y, color='yellow', linestyle='solid', marker='o', label="APM5")
	elif num == 6:
		plt.plot(x, y, color='cyan', linestyle='solid', marker='o', label="APM6")

# Settings for the graph
plt.xlabel('Seconds')
plt.ylabel('% Usage')
plt.title('CPU Utilization')
plt.legend()



# MEMORY UTILIZATION
plt.figure(2)
# Amount of x ticks
plt.xticks(x_ticks)
num = 0
for files in range(6):
	x = []
	y = []
	num += 1
	with open('APM' + str(num) + '_metrics.csv', 'r') as file:
		lines = csv.reader(file, delimiter=',')

		for row in lines:
			x.append(row[0])
			y.append(float(row[2]))
	if num == 1:
		plt.plot(x, y, color='blue', linestyle='solid', marker='o', label="APM1")
	elif num == 2:
		plt.plot(x, y, color='black', linestyle='solid', marker='o', label="APM2")
	elif num == 3:
		plt.plot(x, y, color='red', linestyle='solid', marker='o', label="APM3")
	elif num == 4:
		plt.plot(x, y, color='green', linestyle='solid', marker='o', label="APM4")
	elif num == 5:
		plt.plot(x, y, color='yellow', linestyle='solid', marker='o', label="APM5")
	elif num == 6:
		plt.plot(x, y, color='cyan', linestyle='solid', marker='o', label="APM6")

# Settings for the graph
plt.xlabel('Seconds')
plt.ylabel('% Memory')
plt.title('Memory Utilization')
plt.legend()



# BANDWIDTH UTILIZATION
plt.figure(3)
# Amount of x ticks
plt.xticks(x_ticks)
for i in range(2):
	i += 1
	x = []
	y = []
	with open('system_metrics.csv', 'r') as file:
		lines = csv.reader(file, delimiter=',')

		for row in lines:
			x.append(row[0])
			y.append(float(row[i]))
	if i == 1:
		plt.plot(x, y, color='orange', linestyle='solid', marker='o', label="RX Data Rate (kb/s)")
	elif i == 2:
		plt.plot(x, y, color='grey', linestyle='solid', marker='o', label="TX Data Rate (kb/s)")

# Settings for the graph
plt.xlabel('Seconds')
plt.ylabel('Amount of Bandwidth (kb/s)')
plt.title('Network Bandwidth Utilization')
plt.legend()	



# DISK ACCESS RATES
plt.figure(4)
# Amount of x ticks
plt.xticks(x_ticks)
x = []
y = []
with open('system_metrics.csv', 'r') as file:
	lines = csv.reader(file, delimiter=',')

	for row in lines:
		x.append(row[0])
		y.append(float(row[3]))

	plt.plot(x, y, color='blue', linestyle='solid', marker='o', label="Disk 1")

# Settings for the graph
plt.xlabel('Seconds')
plt.ylabel('Disk Access Writes (kb/s)')
plt.title('Disk Access Rates (kb/s)')
plt.legend()	



# DISK UTILIZATION
plt.figure(5)
# Amount of x ticks
plt.xticks(x_ticks)
x = []
y = []
with open('system_metrics.csv', 'r') as file:
	lines = csv.reader(file, delimiter=',')

	for row in lines:
		x.append(row[0])
		y.append(float(row[4]))

	plt.plot(x, y, color='blue', linestyle='solid', marker='o', label="Disk 1")

# Settings for the graph
plt.xlabel('Seconds')
plt.ylabel('Disk Capacity')
plt.title('Disk Utilization')
plt.legend()

# Finally, show the plots
plt.show()
