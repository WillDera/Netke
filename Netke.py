from threading import Thread
import socket
import subprocess
import sys
from datetime import datetime
from pyfiglet import Figlet
from termcolor import colored

subprocess.call('pip install pyfiglet')
# Clear the screen
subprocess.call('cls||clear', shell=True)

# class for colour codes in Python and Bold text for terminal
# Final9


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


f = Figlet(font='banner3-D')
space = " "*50
print(colored(f.renderText('NETKE'), 'red'),
      colored(space + f"Netke(version 1.2)> Powered By {color.BOLD}CYBER WOKE{color.END}", 'blue'))

# Enter Host to scan
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

# Check what time the scan started
t1 = datetime.now()

# This is just a nice touch that prints out information on which host we are about to scan
# print("-" * 60)
print("\nScan started on %s(%s) (%s)" % (remoteServer, remoteServerIP, t1))
# print("-" * 60)

# Using the range function to specify ports (here it will scans all ports between 1 and 1024)

# We also put in some error handling for catching errors

try:
    print('\nPORT  SERVICE STATE')
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        protocolname = 'tcp'
        #['tcp', 'udp']
        # for port in [80, 25]:
        #     print("Port: %s => service name: %s" %
        #           (port, socket.getservbyport(port, protocolname)))
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            # if a socket is listening it will print out the port number
            # print("Port {}: Open".format(port))
            #
            print("%s/tcp  %s  " %
                  (port, socket.getservbyport(port, protocolname)) + colored('OPEN', 'green'))
        sock.close()

# Don't press any buttons or you will screw up the scanning, so i added a keyboard exception
except KeyboardInterrupt:
    print("\nYou pressed Ctrl+C")
    sys.exit()
    # Here is my host exception, incase you typed it wrong. ( i guess maybe i should have added this up top)
except socket.gaierror:
    print("\nHostname could not be resolved. Exiting")
    sys.exit()
    # finally socket error incase python is having trouble scanning or resolving the port
except socket.error:
    print("\nConnection Timed out")
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total = t2 - t1

# Printing the information to screen
print('Scanning Completed in: ', total)
