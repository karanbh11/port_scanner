# Port scanner works for a single host for scanning multiple ports
from socket import *

# Host address could be ip or hostname . Works fine for both .
HOST_ADDR = input("Enter the host \n")
lower_bound = int(input("Enter the lower bound for the ports to be scanned\n"))
upper_bound = int(input("Enter the upper bound for the ports to be scanned\n"))
OPEN_PORT_LIST = []
setdefaulttimeout(5)

print("Wanna just find open ports or wanna grab banners too ???\n")

# Choose 1 for a simple port scan . It runs faster too than banner grabber .
option = int(input("Enter 1 for simple port scan or 2 for grabbing banners too\n"))
if option == 1:
    for i in range(lower_bound, upper_bound + 1):
        sock = socket(AF_INET, SOCK_STREAM)
        try:
            sock.connect((HOST_ADDR, i))
            print("Port no: " + str(i) + " is open")
            OPEN_PORT_LIST.append(i)
            sock.close()
        except:
            print("Port no: " + str(i) + " is closed")
elif option == 2:
    for i in range(lower_bound, upper_bound + 1):
        sock = socket(AF_INET, SOCK_STREAM)
        try:
            sock.connect((HOST_ADDR, i))
            print("Port no: " + str(i) + " is open")
            sock.sendall(b'hello')
            print(sock.recv(1024))
            OPEN_PORT_LIST.append(i)
            sock.close()
        except:
            print("Port no: " + str(i) + " is closed")

else:
    print("Please enter a valid choice next time...")

print("The list of open ports is : ")

for j in OPEN_PORT_LIST:
    print(j, end=" ")
