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

	# file_content = f.readlines()
	# print file_content
else:
	print "File ", file_name, " does not existst"
	fo = open(file_name, 'a')
	fo.write(csv_header_text)
	fo.close()
	output_file = open(file_name, 'a')
	a = csv.writer(output_file, delimiter=';')

	# file_content = f.readlines()
	# print file_content


# values = []

# # going through each line of the file and parsing and appending to the list/array
# # for line in file_content:
# # 	print parse(line)
# # values.append(parse(line))

# # adding router date and time
# date_str = str(datetime.datetime.now().strftime("%Y.%m.%d"))
# values.append(date_str)
# time_str = str(datetime.datetime.now().strftime("%H:%M:%S"))
# values.append(time_str)

# append Cellular metrics



# Needs to be writerow, writerows inserts delimiter after every char in the list
# a.writerow(values)
# output_file.close()

host = ''
HOST = ''   # Symbolic name meaning all available interfaces
port = 4001  

 
# Datagram (udp) socket
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'Socket created'
except socket.error, msg :
    print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
 
 
# Bind socket to local host and port
try:
    s.bind((host, port))
    print 'Server listening, UDPserver: ' + str(host) + " / : " + str(port)
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'

# Look for the response
amount_received = 0    
while True:
	
	# receive data from client (data, addr)
   	d = s.recvfrom(1024)
   	data = d[0]
   	addr = d[1]
     
   	if not data:
   		break
   		# output_file.close()
       	# break

	values = []

	# going through each line of the file and parsing and appending to the list/array
	# for line in file_content:
	# 	print parse(line)
	# values.append(parse(line))

	# adding router date and time
	date_str = str(datetime.datetime.now().strftime("%Y.%m.%d"))
	values.append(date_str)
	time_str = str(datetime.datetime.now().strftime("%H:%M:%S"))
	values.append(time_str)




    # data = s.recv(1024) #TCP
    # data, addr = sock.recvfrom(1024) # UDP buffer size is 1024 bytes
	amount_received += len(data)
	print 'received "%s"' % data
    # append serial data
	output_file = open(file_name, 'a')
	a = csv.writer(output_file, delimiter=';')
	values.append(data)
	a.writerow(values)
    # need to solve close/open not to keep file open all the time
	output_file.close()



# s.close                     # Close the socket when done