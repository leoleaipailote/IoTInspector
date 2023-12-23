from zeroconf import ServiceBrowser, Zeroconf
import socket
import time

class MyListener:
    def __init__(self):
        self.devices = []

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        if info:
            device = {}
            device["name"] = info.server
            device["addresses"] = [socket.inet_ntoa(address) for address in info.addresses]
            self.devices.append(device)

def discover_devices():
    service_list = ["_http._tcp.local.", "_test._tcp.local."]
    #service_type = "_http._tcp.local."
    return_list = []
    for service_type in service_list:
        listener = MyListener()

    # Start the Zeroconf service browser and wait for the listener to get the device information
        zeroconf = Zeroconf()
        browser = ServiceBrowser(zeroconf, service_type, listener)
        time.sleep(1)

    # Collect and return the list of discovered devices
        devices = listener.devices
        return_list.append(devices)

    # Clean up
        zeroconf.close()

    return return_list

devices = discover_devices()
print(devices)
'''
from zeroconf import ServiceBrowser, Zeroconf
import socket
import time

class MyListener:
    def __init__(self):
        self.name = None
        self.addresses = []

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        if info:
            self.name = info.server
            for address in info.addresses:
                self.addresses.append(socket.inet_ntoa(address))
        
    

# Replace 'example_service' with the mDNS service name you want to discover
service_type = "_http._tcp.local."
listener = MyListener()

# Start the Zeroconf service browser and wait for the listener to get the device information
zeroconf = Zeroconf()
browser = ServiceBrowser(zeroconf, service_type, listener)
time.sleep(1)
#input("Press enter to exit...\n")

# Print the name and IP addresses of the discovered device
print("Device name: ", listener.name)
print("Device IP addresses: ", listener.addresses)

# Clean up
zeroconf.close()
'''
