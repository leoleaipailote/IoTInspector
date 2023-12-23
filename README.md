# IoT Inspector

This repository includes the changes I made to the original [Smart Home Inspector](https://github.com/nyu-mlab/iot-inspector-client/tree/cr-dev) project as part of an independent research opportunity with Professor Noah Apthorpe.

In in the IoT Inspector’s current state, there exists a major flaw in its functionality: MDNS SSDP and UPNP devices, which make up a large portion of IoT devices, are not being properly identified. After analyzing the source code of the IoT Inspector, the root cause of this error was found in a python file labeled ‘netdiscowrapper.py’ that is supposed to be responsible for extracting naming information about devices on a network. The reason behind this is that the ‘netdisco’ library, which ‘netdiscowrapper.py’ utilizes is deprecated. To address this problem, we first identified the
underlying issue through experimentation with a raspberry pi and a local router. We then modified the source code in netdisco accordingly in a way that made UPNP, MDNS, and SSDP devices discoverable to
the inspector. In addition to this, we collected important characteristics of each device such as the IP address, which was outputted in a csv file that contains all relevant information, ready to be processed for
future use.

The changes we made can be summarized as follows:
- Removed the templates used to find certain devices like Google Home in the Discoverables folder
- Created a general solution for UPNP/SSDP devices in general_devices.py
- Created a general solution for MDNS devices through a function called discover_mdns_devices in netdiscowrapper.py
- Produced a csv file upon running the code that contains each device detected with fields that include device name, type, and IP Address
