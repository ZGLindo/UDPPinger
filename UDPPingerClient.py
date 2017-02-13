# UDPPingerClient.py
# We will need the following module to generate randomized lost packets
import time
from socket import *
# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
clientSocket = socket(AF_INET, SOCK_DGRAM)
localHost = '137.143.59.1'
sequence_number = 0
# 5 seconds - Time the client is willing to wait for a message
clientSocket.settimeout(10)
minimum = 1
maximum = 0
sumrtt = 0
successes = 0
failures = 0
rtt = 0
while sequence_number < 10:
    # Message to send to server
    sequence_number += 1
    message = "Ping"
    # Send message to server
    date = time.asctime(time.localtime())
    start = time.clock()
    clientSocket.sendto(message.encode(),(localHost, 12000))
    try:
        # Get message from server side
        message, address = clientSocket.recvfrom(1024)
        current = time.clock()
        # Print information from server
        print ("%s %s %s" %(message, sequence_number, date))
        rtt = current - start
        if (rtt > maximum):
            maximum = rtt
        if (rtt < minimum):
            minimum = rtt
        sumrtt += rtt
        print ('Round Trip Time = ' + str(rtt) + " seconds\n")
        successes += 1
    # Timeout exception
    except timeout:
        print ("Request timed out...sorry :(\n\n\n")
        failures += 1
avgrtt = sumrtt/successes
# Print out Avg, min, and max rtt
print ("Average Round Trip Time: "+ str(avgrtt) + "\nMinimum Round Trip Time: "+ str(minimum) +"\nMaximum Round Trip Time: " + str(maximum))
# Failure Rates
print ("Packets lost: " + str(failures))
print ("Loss Percentage: " + str(failures*10) + "%")