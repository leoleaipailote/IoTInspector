from. import SSDPDiscoverable

class Discoverable(SSDPDiscoverable):
    def get_entries(self):
        """Get all the frontier silicon uPnP entries."""
        entries = []
        for entry in self.netdis.ssdp.all():
            print("entry type: ", type(entry))
            print("entry: ", entry)
            print("entry.st", entry.st)
            print("info_from_entry: ", self.info_from_entry(entry))
            if entry.st and 'urn:schemas-upnp-org:device' in entry.st:
                entries.append(entry)
        print("all entries: ", entries)
        return entries
