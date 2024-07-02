# Enhanced IoT Inspector for MDNS, SSDP, and UPNP

This project focuses on improving the IoT Inspector, an open-source tool initially incapable of identifying key IoT device protocols such as MDNS, SSDP, and UPNP due to the deprecation of the netdisco library. Our enhancements ensure these devices are now detectable, significantly advancing the app's functionality for cybersecurity purposes.

## Introduction

The IoT Inspector tool is designed to identify devices connected to a local network to enhance network security. However, its inability to detect a significant portion of IoT devices (MDNS, SSDP, and UPNP) limited its utility. Our project rectifies this by modifying the underlying netdisco library, thereby broadening the scope of detectable devices.

## Key Features

- **Device Detection Enhancement**: Introduces support for MDNS, SSDP, and UPNP devices, previously undetectable.
- **Data Extraction**: Extracts and logs device details like IP addresses and device types into a CSV file for further processing.
- **Custom Implementation**: Uses custom scripts to override the outdated functions of the netdisco library, enhancing the detection process.

## Methodology

1. **Identified Issues**: Through testing with a raspberry pi and local router setup, identified that the discovery functions of netdisco were not operational.
2. **Custom Fixes**: Modified the source code to implement correct detection mechanisms for MDNS, SSDP, and UPNP protocols.
3. **Validation**: Used extensive logging and real-time debugging to ensure that the devices were accurately detected and relevant information was captured.

## Solutions Implemented

- **General SSDP/UPNP Solution**: Implemented a generalized detection method by identifying common tags in the device information strings.
- **MDNS Specific Solution**: Developed a new function leveraging the ZeroConf library to detect and catalogue MDNS devices effectively.

## Future Work

- **Expand Device Templates**: Integrate more comprehensive lists of device types for MDNS and SSDP protocols.
- **Enhance Data Processing**: Develop clustering and classification algorithms to analyze collected data, aiding in the identification of commonalities and categorization of devices.

## Discussion

The experience revealed that modifying the existing IoT Inspector could be more complex than building a new solution from scratch due to the cumbersome and convoluted process of the existing netdisco implementation.

## Conclusion

Our modifications have significantly enhanced the IoT Inspector's functionality by enabling the detection of a broader range of IoT devices. Future improvements should focus on refining these detection capabilities and utilizing machine learning for data analysis.

## References

- Huang, Danny et al. "IoT Inspector: Crowdsourcing Labeled Network Traffic from Smart Home Devices at Scale"
  [IoT Inspector Paper](https://iotinspector.org/papers/ubicomp-20.pdf)
