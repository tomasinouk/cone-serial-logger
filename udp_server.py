#!/usr/bin/python           # This is client.py file

import socket               # Import socket module
import csv
import time
import datetime
import os.path
import os

csv_header_text = "Date;Time;Data\n"
date_str = str(datetime.datetime.now().strftime("%Y-%m-%d"))
# file_name = "/mnt/usb/" + date_str + "_error_report.csv"
file_name =  date_str + "_error_report.csv"

if os.path.isfile(file_name):
	print "File " , file_name, " existst"
	output_file = open(file_name, 'a')
	a = csv.writer(output_file, delimiter=';')

	file_content = f.readlines()
	# print file_content
else:
	print "File ", file_name, " does not existst"
	fo = open(file_name, 'a')
	fo.write(csv_header_text)
	fo.close()
	output_file = open(file_name, 'a')
	a = csv.writer(output_file, delimiter=';')

	file_content = f.readlines()
	# print file_content


values = []

# going through each line of the file and parsing and appending to the list/array
# for line in file_content:
# 	print parse(line)
	values.append(parse(line))

# adding router date and time
date_str = str(datetime.datetime.now().strftime("%Y.%m.%d"))
values.append(date_str)
time_str = str(datetime.datetime.now().strftime("%H:%M:%S"))
values.append(time_str)

# append Cellular metrics



# Needs to be writerow, writerows inserts delimiter after every char in the list
a.writerow(values)
output_file.close()

host = "127.0.0.1"
port = 4001  

# TCP socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
# host = socket.gethostname() # Get local machine name
              # Reserve a port for your service.

# s.connect((host, port))


# UDP socket
# sock = socket.socket(socket.AF_INET, # Internet
#                       socket.SOCK_DGRAM) # UDP

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
s.bind((host, port))
# print s.recv(1024)

# Look for the response
amount_received = 0    
while True:
    # data = s.recv(1024) #TCP
    data, addr = sock.recvfrom(1024) # UDP buffer size is 1024 bytes
    amount_received += len(data)
    print 'received "%s"' % data
    # append serial data
    values.append(data)
    a.writerow(values)
	output_file.close()


# s.close                     # Close the socket when done