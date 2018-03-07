# Zaki G. Lindo
# CIS 410 - Computer Networks
# Programming Assingment 1 - UDPPinger
# March 2018

# We will need to record current times and we will need open sockets 
# to communicate with a Server
import time
from socket import *

# We need a UDP socket and the IP of the localhost
clientSocket = socket(AF_INET, SOCK_DGRAM)
localhost = '127.0.0.1'

# We need to record our sequence number(we will count up as our client runs)
seq_num = 0

# 1 seconds - Time the Client waits for a message
clientSocket.settimeout(1)

# We need to record our minimum, maximum, and average roundtriptimes(rtts)
rtt = 0 				# Round Trip Time of each Ping
minrtt = 1 				# This works since our timeout is 1 second and every rtt should 
						# be less than 1 second if successful 
maxrtt = 0 				# Will be reset every time we have a higher rtt than 0 seconds
sumrtt = 0 				# Will add to this to help calculate the average
successes = 0 			# Counts number of successful pings
failures = 0 			# Counts number of failed pings

# This loop runs 10 times, using the seq_num to cycle through each iteration
while seq_num < 10:
    seq_num += 1		# Add 1 to the loop counter
    message = "Ping"	# Message to be sent to Server
    # Send message to server
    date = time.asctime(time.localtime())
    start = time.clock()
    clientSocket.sendto(message.encode(),(localhost, 12000))
    try:
    	
    	# Get message from server side
        message, address = clientSocket.recvfrom(1024) 
        current = time.clock()
        
        # Print message from the Server
        # Should Print out "Ping seq_num 1 Sun Jan"
        print ("%s %s %s" %(message, seq_num, date))

        # Calculate rtt
        rtt = current - start
        if (rtt > maxrtt):
        	# If there is a new maxrtt, set the new maxrtt
            maxrtt = rtt
        if (rtt < minrtt):
        	# If there is a new minrtt, set the new minrtt
            minrtt = rtt

        # Add to the total rtt
        sumrtt += rtt
        print ('Round Trip Time = ' + str(rtt) + " seconds\n")
        successes += 1

        # Timeout exception for when rtt > time
    except timeout:
    	# Timeout message
        print ("Request timed out...Try again!\n\n\n")
        # Add one to the sum of failures
        failures += 1
avgrtt = sumrtt/successes
# Print out Avg, min, and max rtt
print ("Average Round Trip Time: "+ str(avgrtt) + "\nMinimum Round Trip Time: "+ str(minrtt) +"\nMaximum Round Trip Time: " + str(maxrtt))
# Failure Rates
print ("Packets lost: " + str(failures))
print ("Loss Percentage: " + str(failures*10) + "%")