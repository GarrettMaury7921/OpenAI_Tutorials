#!/usr/bin/python3
import os
import csv
import re

# Garrett Maury, 11/30/2021

# Clear Terminal
clear = 'clear'
os.system(clear)

with open('linux_users.csv', 'r') as file:
    # read each row into a dictionary
    reader = csv.DictReader(file)
    data = {}
    for row in reader:
        for header, value in row.items():
            try:
                data[header].append(value)
            except KeyError:
                data[header] = [value]

# Extract all of the variables needed
Employee_ID = data['EmployeeID']
Last_Name = data['LastName']
First_Name = data['FirstName']
Office = data['Office']
Phone = data['Phone']
Department = data['Department']
Group = data['Group']

# Make User Names
all_users = []
for i in range(7):
    first_initial = First_Name[i]
    # Get first index of string
    try:
        first_initial = first_initial[0]
        user_name = first_initial + Last_Name[i]
    except IndexError:
        user_name = "Insufficient data."

    # Check for Duplicate Names
    if all_users.count(user_name) > 0:
        user_name = user_name + str(1)  # Make a unique username
    if all_users.count(user_name) > 1:
        user_name = user_name + str(2)  # Make a unique username
    elif all_users.count(user_name) > 2:
        last_char = user_name[-1]
        num = int(last_char) + 1
        user_name = user_name + num

    # Check for Duplicate IDs
    if Employee_ID.count(Employee_ID[i]) > 0:
        Employee_ID[i] = Employee_ID[i] + str(1)  # Make a unique id
    if Employee_ID.count(Employee_ID[i]) > 1:
        Employee_ID[i] = Employee_ID[i] + str(2)  # Make a unique id
    elif Employee_ID.count(Employee_ID[i]) > 2:
        last_char = Employee_ID[i]
        last_char2 = last_char[-1]
        num = int(last_char2) + 1
        Employee_ID[i] = Employee_ID[i] + num

    # Check if Last Names have a illegal character
    for element in range(len(Last_Name)):
        # Check if a string contains only alphabetical letters
        if Last_Name[element].isalpha():
            pass
        else:
            Last_Name[element] = re.sub(r"[^a-zA-Z0-9]", "", Last_Name[element])
    # Add to a list of all users
    all_users.append(user_name)

# Add groups if they don't exist
for element in range(len(Group)):
	os.system('groupadd -f ' + Group[element])

# Check for empty fields in the csv file and make sure to note the one's that don't work
bad_numbers = []
for element in range(len(Group)):
    if len(Employee_ID[element]) == 0 or len(Last_Name[element]) == 0 or len(First_Name[element]) <= 0 or len(Office[element]) == 0 or len(Phone[element]) == 0 or len(Department[element]) == 0 or len(Group[element]) == 0:
        bad_numbers.append(element)

# Try to add the users
print("Adding new users to the system.")
for i in range(7):
	# If there is a bad addition
	if i in bad_numbers:
		id = Employee_ID[i]
		username = all_users[i]
		print('Cannot process employee ID ' + id + '.		' + username + ' NOT added to system.')
	else:
		id = Employee_ID[i]
		username = all_users[i]
		cmd = 'sudo useradd ' + username
		# execute command to add users
		os.system(cmd)
		# Assign users to a group
		os.system('sudo usermod -a -G ' + Group[i] + ' ' + username)
		# Assign users a home dir
		os.system('usermod -d /home/' + Group[i] + ' ' + username)
		# assign a default shell
		os.system('chsh -s /usr/local/bin/bash ' + username)
		# assign a default password
		os.system('echo ' + username + ':password | chpasswd')
		# expire password
		os.system('passwd --expire ' + username)
		# Accept the user notification
		print('Processing employee ID ' + id + '.		' + username + ' added to system.')
