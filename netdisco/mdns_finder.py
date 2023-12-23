
from zeroconf import Zeroconf, ZeroconfServiceTypes

def get_all_service_types():
    zc = Zeroconf()
    service_types = ZeroconfServiceTypes.find(zc)
    zc.close()
    return service_types

print(get_all_service_types())




